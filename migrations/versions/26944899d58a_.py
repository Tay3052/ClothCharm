"""empty message

Revision ID: 26944899d58a
Revises: 463c9df04bd7
Create Date: 2023-11-30 18:21:19.191659

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '26944899d58a'
down_revision = '463c9df04bd7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categoryname',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('categoryname', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8mb4'
    )
    op.create_table('sexuals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sex', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8mb4'
    )
    op.drop_table('categorynames')
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'sexuals', ['sex'], ['id'])
        batch_op.create_foreign_key(None, 'sizes', ['size'], ['id'])
        batch_op.create_foreign_key(None, 'conditions', ['condition'], ['id'])
        batch_op.create_foreign_key(None, 'categoryname', ['category'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')

    op.create_table('categorynames',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('categoryname', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('sexuals')
    op.drop_table('categoryname')
    # ### end Alembic commands ###
