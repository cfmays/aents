"""empty message

Revision ID: 1951c01cfbba
Revises: 8bad0d4fbf8e
Create Date: 2020-01-27 15:27:29.795722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1951c01cfbba'
down_revision = '8bad0d4fbf8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('persons', sa.Column('email', sa.String(length=80), nullable=True))
    op.create_index(op.f('ix_persons_email'), 'persons', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_persons_email'), table_name='persons')
    op.drop_column('persons', 'email')
    # ### end Alembic commands ###
