"""empty message

Revision ID: 25ff5af7c054
Revises: ac9ce37ca581
Create Date: 2019-11-11 11:43:30.988174

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '25ff5af7c054'
down_revision = 'ac9ce37ca581'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    op.drop_table('comments')
    op.add_column('ipath_namelist', sa.Column('points', sa.Integer(), server_default='0', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ipath_namelist', 'points')
    op.create_table('comments',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('comment', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('creation_date', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name='comments_category_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='comments_pkey')
    )
    op.create_table('categories',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='categories_pkey'),
    sa.UniqueConstraint('name', name='categories_name_key')
    )
    # ### end Alembic commands ###
