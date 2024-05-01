"""create_tables

Revision ID: 9ac866fb1ea1
Revises: 
Create Date: 2024-05-01 11:49:36.548276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ac866fb1ea1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column('username', sa.String, primary_key=True),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('password', sa.String(50), nullable=False))

    op.create_table(
        "builds",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('class_name', sa.String(50), nullable=False),
        sa.Column('level', sa.Integer, nullable=False),
        sa.Column('items_equipped', sa.String(50), nullable=False),
        sa.Column('skill_gems_used', sa.String(50), nullable=False),
        sa.Column('passive_tree', sa.String, nullable=False),
        sa.Column('notes', sa.String, nullable=True)
    )

def downgrade() -> None:
    op.drop_table("users")
    op.drop_table("builds")