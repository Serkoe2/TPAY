"""Added required tables

Revision ID: b73bc823541d
Revises: 8c11cf489be2
Create Date: 2022-04-12 23:17:49.762692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b73bc823541d'
down_revision = '8c11cf489be2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('payment_url', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'payment_url')
    # ### end Alembic commands ###
