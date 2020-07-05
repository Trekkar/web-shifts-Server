"""add externalId and sourceId columns to Clients table

Revision ID: 90f85c1fef2a
Revises: fe0535c434b5
Create Date: 2020-07-05 18:22:53.957449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90f85c1fef2a'
down_revision = 'fe0535c434b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clients', sa.Column('externalId', sa.Integer(), nullable=True))
    op.add_column('clients', sa.Column('sourceId', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('clients', 'sourceId')
    op.drop_column('clients', 'externalId')
    # ### end Alembic commands ###