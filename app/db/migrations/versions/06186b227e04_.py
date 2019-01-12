"""Added Initial Models

Revision ID: 06186b227e04
Revises: 56b6e1247ced
Create Date: 2019-01-12 17:12:39.013102

"""
from alembic import op
import sqlalchemy as sa
import app


# revision identifiers, used by Alembic.
revision = "06186b227e04"
down_revision = "56b6e1247ced"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("wins", sa.Integer(), nullable=False),
        sa.Column("losses", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "trick",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("dealer_id", sa.Integer(), nullable=False),
        sa.Column("room_id", sa.Integer(), nullable=False),
        sa.Column("trump_suit", app.models.columns.suit.Suit(), nullable=True),
        sa.ForeignKeyConstraint(["dealer_id"], ["user.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["room_id"], ["room.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "hand",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("trick_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["trick_id"], ["trick.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "round",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("trick_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["trick_id"], ["trick.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user_team_join",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("team_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["team_id"], ["team.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "card_hand_join",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("card_id", sa.Integer(), nullable=False),
        sa.Column("hand_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["card_id"], ["card.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["hand_id"], ["hand.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "play",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("round_id", sa.Integer(), nullable=False),
        sa.Column("card_hand_join_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["card_hand_join_id"], ["card_hand_join.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["round_id"], ["trick.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("play")
    op.drop_table("card_hand_join")
    op.drop_table("user_team_join")
    op.drop_table("round")
    op.drop_table("hand")
    op.drop_table("trick")
    op.drop_table("user")
