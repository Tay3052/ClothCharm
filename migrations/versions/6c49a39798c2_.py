"""empty message

Revision ID: 6c49a39798c2
Revises: b75a8facec99
Create Date: 2023-12-09 16:49:38.138627

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6c49a39798c2'
down_revision = 'b75a8facec99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sexual', sa.Integer(), nullable=True))
        batch_op.drop_constraint('user_images_ibfk_5', type_='foreignkey')
        batch_op.create_foreign_key(None, 'sexuals', ['sexual'], ['id'])
        batch_op.drop_column('sex')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sex', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('user_images_ibfk_5', 'sexuals', ['sex'], ['id'])
        batch_op.drop_column('sexual')

    # ### end Alembic commands ###