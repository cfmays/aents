"""empty message

Revision ID: 3dd3c2f5a8fe
Revises: 38df2a3bf51c
Create Date: 2020-01-27 20:59:51.013434

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3dd3c2f5a8fe'
down_revision = '38df2a3bf51c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('persons', sa.Column('username', sa.String(length=60), nullable=True))
    op.create_index(op.f('ix_persons_username'), 'persons', ['username'], unique=True)
    op.drop_index('ix_persons_user_name', table_name='persons')
    op.drop_column('persons', 'user_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('persons', sa.Column('user_name', mysql.VARCHAR(collation='utf8mb4_general_ci', length=60), nullable=True))
    op.create_index('ix_persons_user_name', 'persons', ['user_name'], unique=True)
    op.drop_index(op.f('ix_persons_username'), table_name='persons')
    op.drop_column('persons', 'username')
    # ### end Alembic commands ###
