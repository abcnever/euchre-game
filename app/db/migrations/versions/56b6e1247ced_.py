"""Initial Set up

Revision ID: 56b6e1247ced
Revises:
Create Date: 2018-11-11 21:51:03.097852

"""
from alembic import op
import sqlalchemy as sa
from app.models.columns.card_name import CardName
from app.models.columns.suit import Suit

# revision identifiers, used by Alembic.
revision = "56b6e1247ced"
down_revision = None
branch_labels = None
depends_on = None

cards = []

for card in CardName.Enum:
    for suit in Suit.Enum:
        if card.name != "_CardName" and suit.name != "_Suit":
            cards.append({"name": card.value.card_name, "suit": suit.value.suit_name})

def upgrade():
    card_table = op.create_table(
        "card",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("suit", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "room", sa.Column("id", sa.Integer(), autoincrement=True, nullable=False), sa.PrimaryKeyConstraint("id")
    )
    op.create_table(
        "team",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("room_id", sa.Integer(), nullable=False),
        sa.Column("wins", sa.Integer(), nullable=False),
        sa.Column("losses", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["room_id"], ["room.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )

    op.bulk_insert(card_table, cards)


def downgrade():
    op.drop_table("team")
    op.drop_table("room")
    op.drop_table("card")
