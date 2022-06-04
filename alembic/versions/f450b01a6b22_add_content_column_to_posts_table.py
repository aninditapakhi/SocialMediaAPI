"""add content column to posts table

Revision ID: f450b01a6b22
Revises: 0dbd517dd9ea
Create Date: 2022-06-03 00:26:21.171790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f450b01a6b22'
down_revision = '0dbd517dd9ea'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('Content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'Content')
    pass
