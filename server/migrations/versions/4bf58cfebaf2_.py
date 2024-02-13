"""empty message

Revision ID: 4bf58cfebaf2
Revises: 3389a3844a64
Create Date: 2024-02-13 09:35:09.024408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bf58cfebaf2'
down_revision = '3389a3844a64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('adventurers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('adventurer_class', sa.String(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('experience', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_adventurers')),
    sa.UniqueConstraint('name', name=op.f('uq_adventurers_name'))
    )
    op.create_table('quests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('difficulty', sa.String(), nullable=True),
    sa.Column('adventurer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['adventurer_id'], ['adventurers.id'], name=op.f('fk_quests_adventurer_id_adventurers')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_quests')),
    sa.UniqueConstraint('title', name=op.f('uq_quests_title'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quests')
    op.drop_table('adventurers')
    # ### end Alembic commands ###
