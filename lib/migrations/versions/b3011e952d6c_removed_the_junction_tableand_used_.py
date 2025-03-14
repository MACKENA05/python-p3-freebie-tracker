"""removed the junction tableand used freebies table as the junction table

Revision ID: b3011e952d6c
Revises: 6585dc1bb536
Create Date: 2025-03-05 18:30:22.748102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3011e952d6c'
down_revision = '6585dc1bb536'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('companyDevs')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companyDevs',
    sa.Column('company_id', sa.INTEGER(), nullable=False),
    sa.Column('dev_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['dev_id'], ['devs.id'], ),
    sa.PrimaryKeyConstraint('company_id', 'dev_id')
    )
    # ### end Alembic commands ###
