"""empty message

Revision ID: 70ac123543f0
Revises: 86b8085bf28d
Create Date: 2023-12-07 18:10:48.220581

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '70ac123543f0'
down_revision = '86b8085bf28d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.alter_column('explain',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=255),
               existing_nullable=True)
        batch_op.create_foreign_key(None, 'categorynames', ['category'], ['id'])
        batch_op.create_foreign_key(None, 'sizes', ['size'], ['id'])
        batch_op.create_foreign_key(None, 'sexuals', ['sex'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('explain',
               existing_type=sa.String(length=255),
               type_=mysql.TEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###