"""add user table

Revision ID: 66086647d5cc
Revises: f450b01a6b22
Create Date: 2022-06-04 14:31:40.990283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66086647d5cc'
down_revision = 'f450b01a6b22'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
            sa.Column('id',sa.Integer(), nullable=False),
            sa.Column('email',sa.String(), nullable=False),
            sa.Column('password',sa.String(), nullable=False),
            sa.Column('created_at',sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
