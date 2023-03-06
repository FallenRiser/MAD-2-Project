"""added posts model and tinkered with boolean in posts model to force migration backup

Revision ID: 309b8ea6bf99
Revises: 3857ccef4cdd
Create Date: 2023-03-07 04:29:58.796855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '309b8ea6bf99'
down_revision = '3857ccef4cdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hidden', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('hidden')

    # ### end Alembic commands ###
