"""add message field

Revision ID: fe0cb775f9a9
Revises: 2998bba34c69
Create Date: 2021-08-05 14:16:16.716095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe0cb775f9a9'
down_revision = '2998bba34c69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('message', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'message')
    # ### end Alembic commands ###
