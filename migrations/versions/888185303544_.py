"""empty message

Revision ID: 888185303544
Revises: 1a6a564a15bc
Create Date: 2023-07-31 12:24:35.498353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '888185303544'
down_revision = '1a6a564a15bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('telephone', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('password', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_column('password')
        batch_op.drop_column('telephone')

    # ### end Alembic commands ###
