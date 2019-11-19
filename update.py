import json
import requests
from apscheduler.schedulers.background import BackgroundScheduler
import psycopg2
import sys

def CheckExist():
    parameters = {"token":" WXpKc2RXSXpRbWhaZHowOQ "}
    response = requests.post("http://boostfit.org/StampedeAPI/index.php/Game/GameRecord/queryRecordedId/", json=parameters)
    if response.json()["success"] == "true":
        return response.json()["result"]["sinopac"]
    else:
        return None

def callAPI(nickname):
    parameters = {"token":" WXpKc2RXSXpRbWhaZHowOQ ","user_id":nickname}
    response = requests.post("http://boostfit.org/StampedeAPI/index.php/Game/GameRecord/queryGameRecord/", json=parameters)
    if type(response.json()["result"]) is list:
        return response.json()["result"]
    else:
        return "no record"

def execute(connection,cursor):
    
    existlist = CheckExist()
    postgreSQL_select_Query = "select * from ipath_namelist where nickname = %s"
    postgreSQL_update_Query = "update ipath_namelist set record = %s ,calories = %s where nickname = %s"
    if existlist:  
        print("updating...")
        for nickname in existlist:
            resultlist = callAPI(nickname)
            if nickname == '0051':
                total_record = 120
            else:
                total_record = 100        
            total_calories = 0
            for namedict in resultlist:
                total_record += int(namedict['record'])
                total_calories += int(namedict['calories'])
            cursor.execute(postgreSQL_select_Query, (nickname,))
            local_data = cursor.fetchall()
            for row in local_data:
                local_record = row[3]
                local_calories = row[2]
                if int(total_record) != local_record or int(total_calories) != local_calories:
                    cursor.execute(postgreSQL_update_Query, (total_record,total_calories,nickname,))
                    connection.commit()
    else:
        print("No update")

def check(connection,cursor):
    postgreSQL_select_Query = "select * from ipath_namelist where nickname = %s"
    existlist = CheckExist()
    for id in existlist:
        cursor.execute(postgreSQL_select_Query, (id,))
        print(cursor.fetchall())

if __name__ == "__main__":
    connection = psycopg2.connect(user="netdb",password="netdb2602",host="127.0.0.1",port="5432",database="ipathdb")
    cursor = connection.cursor()
    execute(connection,cursor)
    # check(connection,cursor)
    scheduler = BackgroundScheduler()
    scheduler.add_job(execute, 'interval',[connection,cursor], minutes=5,max_instances=10, replace_existing=True)
    scheduler.start()
    while True:
        pass

    
        
    

