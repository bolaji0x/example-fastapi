"""add content column to posts table

Revision ID: 0f5127ea11cc
Revises: 2ac000da838a
Create Date: 2024-01-02 23:16:51.690629

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f5127ea11cc'
down_revision: Union[str, None] = '2ac000da838a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
