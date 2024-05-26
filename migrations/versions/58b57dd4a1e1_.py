"""empty message

Revision ID: 58b57dd4a1e1
Revises: 2628831ef10e
Create Date: 2023-11-30 17:37:17.550859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58b57dd4a1e1'
down_revision = '2628831ef10e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'conditions', ['condition'], ['id'])
        batch_op.create_foreign_key(None, 'categorynames', ['category'], ['id'])
        batch_op.create_foreign_key(None, 'sizes', ['size'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
