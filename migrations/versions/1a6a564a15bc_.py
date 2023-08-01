"""empty message

Revision ID: 1a6a564a15bc
Revises: 731b03ac4a64
Create Date: 2023-07-31 12:17:25.153815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a6a564a15bc'
down_revision = '731b03ac4a64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bio', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('current_company', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('socials', sa.String(), nullable=True))
        batch_op.drop_column('password')
        batch_op.drop_column('telephone')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('telephone', sa.VARCHAR(length=10), nullable=True))
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=200), nullable=True))
        batch_op.drop_column('socials')
        batch_op.drop_column('current_company')
        batch_op.drop_column('bio')

    # ### end Alembic commands ###