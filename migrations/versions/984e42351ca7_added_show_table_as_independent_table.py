"""added show table as independent table

Revision ID: 984e42351ca7
Revises: c59aef8a979c
Create Date: 2020-04-05 20:37:46.131530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '984e42351ca7'
down_revision = 'c59aef8a979c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Shows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Shows',
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('start_time', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], name='Shows_artist_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], name='Shows_venue_id_fkey'),
    sa.PrimaryKeyConstraint('artist_id', 'venue_id', name='Shows_pkey')
    )
    op.drop_table('Show')
    # ### end Alembic commands ###
