"""add relationship between the tables

Revision ID: 0f87c94b093f
Revises: a7048d69039a
Create Date: 2025-03-05 13:45:50.152604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f87c94b093f'
down_revision = 'a7048d69039a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companyDevs',
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('dev_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name=op.f('fk_companyDevs_company_id_companies')),
    sa.ForeignKeyConstraint(['dev_id'], ['devs.id'], name=op.f('fk_companyDevs_dev_id_devs')),
    sa.PrimaryKeyConstraint('company_id', 'dev_id')
    )
    with op.batch_alter_table('freebies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dev_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('company_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_freebies_dev_id_devs'), 'devs', ['dev_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_freebies_company_id_companies'), 'companies', ['company_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freebies', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_freebies_company_id_companies'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_freebies_dev_id_devs'), type_='foreignkey')
        batch_op.drop_column('company_id')
        batch_op.drop_column('dev_id')

    op.drop_table('companyDevs')
    # ### end Alembic commands ###
