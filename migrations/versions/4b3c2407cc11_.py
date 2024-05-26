"""empty message

Revision ID: 4b3c2407cc11
Revises: 4fcbf9918a0f
Create Date: 2023-11-30 18:26:28.643149

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4b3c2407cc11'
down_revision = '4fcbf9918a0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'conditions', ['condition'], ['id'])
        batch_op.create_foreign_key(None, 'sizes', ['size'], ['id'])
        batch_op.create_foreign_key(None, 'categorynames', ['category'], ['id'])
        batch_op.drop_column('color')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.add_column(sa.Column('color', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
