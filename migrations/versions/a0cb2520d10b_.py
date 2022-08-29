"""empty message

Revision ID: a0cb2520d10b
Revises: 2992c543d1f0
Create Date: 2022-08-13 08:43:59.377037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0cb2520d10b'
down_revision = '2992c543d1f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('school')
    op.drop_table('program')
    op.drop_table('year_group')
    op.drop_table('login')
    op.drop_column('person', 'next_of_kin')
    op.drop_column('person', 'class_designaiton')
    op.drop_column('person', 'nationality')
    op.drop_column('person', 'status_doa')
    op.drop_column('person', 'primary_phone_number')
    op.drop_column('person', 'brithdate')
    op.drop_column('person', 'marital_status')
    op.drop_column('person', 'extra_curriculum_activities')
    op.drop_column('person', 'current_place_of_work')
    op.drop_column('person', 'home_address')
    op.drop_column('person', 'Year_group')
    op.drop_column('person', 'picture')
    op.drop_column('person', 'student_id')
    op.drop_column('person', 'health_status')
    op.drop_column('person', 'secondary_phone_number')
    op.drop_column('person', 'guardian')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('guardian', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('secondary_phone_number', sa.INTEGER(), nullable=True))
    op.add_column('person', sa.Column('health_status', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('student_id', sa.INTEGER(), nullable=False))
    op.add_column('person', sa.Column('picture', sa.VARCHAR(), nullable=False))
    op.add_column('person', sa.Column('Year_group', sa.INTEGER(), nullable=False))
    op.add_column('person', sa.Column('home_address', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('current_place_of_work', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('extra_curriculum_activities', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('marital_status', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('brithdate', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('primary_phone_number', sa.INTEGER(), nullable=True))
    op.add_column('person', sa.Column('status_doa', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('nationality', sa.VARCHAR(length=100), nullable=False))
    op.add_column('person', sa.Column('class_designaiton', sa.VARCHAR(), nullable=True))
    op.add_column('person', sa.Column('next_of_kin', sa.VARCHAR(), nullable=True))
    op.create_table('login',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=20), nullable=True),
    sa.Column('password', sa.VARCHAR(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('year_group',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=200), nullable=False),
    sa.Column('program', sa.VARCHAR(length=200), nullable=True),
    sa.Column('total_number', sa.INTEGER(), nullable=True),
    sa.Column('people_completed', sa.INTEGER(), nullable=True),
    sa.Column('people_admitted', sa.INTEGER(), nullable=True),
    sa.Column('Year_group', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('program',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=200), nullable=False),
    sa.Column('program_name', sa.VARCHAR(length=200), nullable=True),
    sa.Column('program_department', sa.VARCHAR(), nullable=True),
    sa.Column('program_code', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('school',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=200), nullable=False),
    sa.Column('name_of_school', sa.VARCHAR(length=200), nullable=True),
    sa.Column('programs', sa.VARCHAR(), nullable=True),
    sa.Column('total_number', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###