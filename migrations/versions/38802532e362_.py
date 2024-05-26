"""empty message

Revision ID: 38802532e362
Revises: 28246e41c8f7
Create Date: 2023-12-01 23:21:44.547663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38802532e362'
down_revision = '28246e41c8f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rental', sa.Boolean(), nullable=True))
        batch_op.create_foreign_key(None, 'colors', ['color'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('rental')

    # ### end Alembic commands ###