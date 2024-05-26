"""empty message

Revision ID: 418f36207ef6
Revises: 60e336a8e8a7
Create Date: 2023-11-02 00:09:21.052733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '418f36207ef6'
down_revision = '60e336a8e8a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.add_column(sa.Column('explain', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.drop_column('explain')

    # ### end Alembic commands ###
