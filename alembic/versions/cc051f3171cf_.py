"""empty message

Revision ID: cc051f3171cf
Revises: 
Create Date: 2024-10-12 17:22:52.902179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc051f3171cf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('uChat_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uChat_id')
    )
    op.create_table('channels',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('channelTG_id', sa.String(), nullable=False),
    sa.Column('uChat_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uChat_id'], ['users.uChat_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('channelTG_id')
    )
    op.create_table('keywords',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('keyword', sa.String(), nullable=True),
    sa.Column('uChat_id', sa.Integer(), nullable=True),
    sa.Column('channelTG_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['channelTG_id'], ['channels.channelTG_id'], ),
    sa.ForeignKeyConstraint(['uChat_id'], ['users.uChat_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('keywords')
    op.drop_table('channels')
    op.drop_table('users')
    # ### end Alembic commands ###
