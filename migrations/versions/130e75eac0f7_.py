"""empty message

Revision ID: 130e75eac0f7
Revises: None
Create Date: 2017-04-14 17:51:12.533272

"""

# revision identifiers, used by Alembic.
revision = '130e75eac0f7'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_post',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('markdown', sa.Text(), nullable=True),
    sa.Column('html', sa.Text(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('published', sa.Boolean(), nullable=True),
    sa.Column('published_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_post')
    # ### end Alembic commands ###