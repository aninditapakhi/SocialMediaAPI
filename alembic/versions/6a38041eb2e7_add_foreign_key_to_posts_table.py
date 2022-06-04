"""add foreign key to posts table

Revision ID: 6a38041eb2e7
Revises: 66086647d5cc
Create Date: 2022-06-04 14:56:16.991947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a38041eb2e7'
down_revision = '66086647d5cc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table='users',
    local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts','owner_id')
    pass
