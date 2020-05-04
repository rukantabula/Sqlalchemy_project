"""Show table.

Revision ID: 9580f385e62e
Revises: 625d4d9af2dc
Create Date: 2020-04-10 12:31:45.865780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9580f385e62e'
down_revision = '625d4d9af2dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Show', type_='foreignkey')
    # ### end Alembic commands ###
