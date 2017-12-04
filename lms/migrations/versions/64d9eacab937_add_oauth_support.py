"""
Add oauth support

Revision ID: 64d9eacab937
Revises: a6a78f338d4a
Create Date: 2017-11-28 13:56:48.270643

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '64d9eacab937'
down_revision = 'a6a78f338d4a'


def upgrade():
    op.create_table(
      'users',
      sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
      sa.Column('lms_guid', sa.String, index=True),
      sa.Column('email', sa.String),
      sa.Column('lms_id', sa.String),
      sa.Column('lms_provider', sa.String),
      sa.Column('lms_url', sa.String),
    )

    op.create_table(
      'tokens',
      sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
      sa.Column('access_token', sa.String),
      sa.Column('refresh_token', sa.String),
      sa.Column('expires_in', sa.String),
      sa.Column('user_id', sa.Integer),
      sa.Column('created', sa.TIMESTAMP, default=datetime.utcnow)
    )

    op.create_table(
      'oauth_state',
      sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
      sa.Column('guid', sa.String),
      sa.Column('user_id', sa.Integer),
      sa.Column('auth_done_url', sa.String),
      sa.Column('lti_params', sa.String)
    )


def downgrade():
    pass