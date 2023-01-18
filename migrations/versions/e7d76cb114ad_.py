"""empty message

Revision ID: e7d76cb114ad
Revises: 
Create Date: 2023-01-18 18:06:27.900282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7d76cb114ad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('type', sa.Enum('customer', 'manager', name='type_types'), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('comercial_places',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('address', sa.String(length=150), nullable=False),
    sa.Column('url', sa.String(length=150), nullable=True),
    sa.Column('telf', sa.String(length=15), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('location', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=120), nullable=False),
    sa.Column('cambiador', sa.Boolean(), nullable=False),
    sa.Column('trono', sa.Boolean(), nullable=False),
    sa.Column('childs', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('location')
    )
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('gender', sa.Enum('female', 'male', name='gender_types'), nullable=True),
    sa.Column('subscription', sa.Boolean(), nullable=True),
    sa.Column('address', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('managers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('comercial_place_id', sa.Integer(), nullable=False),
    sa.Column('comment_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('comment', sa.String(length=1000), nullable=False),
    sa.ForeignKeyConstraint(['comercial_place_id'], ['comercial_places.id'], ),
    sa.ForeignKeyConstraint(['comment_id'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('comercial_place_id', sa.Integer(), nullable=False),
    sa.Column('state', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['comercial_place_id'], ['comercial_places.id'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('photos_comercial_place',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comercial_place_id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['comercial_place_id'], ['comercial_places.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('location')
    )
    op.create_table('rates_customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('customer', sa.Integer(), nullable=False),
    sa.Column('comercial_place_id', sa.Integer(), nullable=False),
    sa.Column('rate', sa.Enum('1', '2', '3', '4', '5', name='rate_types'), nullable=False),
    sa.ForeignKeyConstraint(['comercial_place_id'], ['comercial_places.id'], ),
    sa.ForeignKeyConstraint(['customer'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('photos_comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment_id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=1000), nullable=False),
    sa.ForeignKeyConstraint(['comment_id'], ['comments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('photos_comments')
    op.drop_table('rates_customers')
    op.drop_table('photos_comercial_place')
    op.drop_table('favorits')
    op.drop_table('comments')
    op.drop_table('managers')
    op.drop_table('customers')
    op.drop_table('comercial_places')
    op.drop_table('users')
    # ### end Alembic commands ###
