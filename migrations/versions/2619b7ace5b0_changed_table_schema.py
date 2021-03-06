"""changed table schema

Revision ID: 2619b7ace5b0
Revises: 12c504d6cf84
Create Date: 2020-04-29 16:34:59.496223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2619b7ace5b0'
down_revision = '12c504d6cf84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venue_artists')
    op.add_column('Artist', sa.Column('venue_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'Artist', 'Venue', ['venue_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Artist', type_='foreignkey')
    op.drop_column('Artist', 'venue_id')
    op.create_table('venue_artists',
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], name='venue_artists_artist_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], name='venue_artists_venue_id_fkey'),
    sa.PrimaryKeyConstraint('venue_id', 'artist_id', name='venue_artists_pkey')
    )
    # ### end Alembic commands ###
