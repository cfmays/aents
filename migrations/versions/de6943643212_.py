"""empty message

Revision ID: de6943643212
Revises: 76b7d09760f8
Create Date: 2020-02-20 19:17:26.084721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de6943643212'
down_revision = '76b7d09760f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('encounters', sa.Column('facility_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'encounters', 'facilities', ['facility_id'], ['id'])
    op.add_column('persons', sa.Column('is_facility', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('persons', 'is_facility')
    op.drop_constraint(None, 'encounters', type_='foreignkey')
    op.drop_column('encounters', 'facility_id')
    # ### end Alembic commands ###
