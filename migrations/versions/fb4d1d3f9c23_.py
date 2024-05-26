"""empty message

Revision ID: fb4d1d3f9c23
Revises: 70ac123543f0
Create Date: 2023-12-07 19:18:44.011889

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fb4d1d3f9c23'
down_revision = '70ac123543f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sendproducts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('send', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8mb4'
    )
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.add_column(sa.Column('send', sa.Integer(), nullable=True))
        batch_op.alter_column('explain',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.Text(),
               existing_nullable=True)
        batch_op.create_foreign_key(None, 'sexuals', ['sex'], ['id'])
        batch_op.create_foreign_key(None, 'sizes', ['size'], ['id'])
        batch_op.create_foreign_key(None, 'categorynames', ['category'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('explain',
               existing_type=sa.Text(),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.drop_column('send')

    op.drop_table('sendproducts')
    # ### end Alembic commands ###