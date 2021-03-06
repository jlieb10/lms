from datetime import datetime
import sqlalchemy as sa
from lms.db import BASE


class LtiLaunches(BASE):
    """Track each LTI launch."""

    __tablename__ = "lti_launches"

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    created = sa.Column(sa.TIMESTAMP, default=datetime.utcnow())
    context_id = sa.Column(sa.String)
    lti_key = sa.Column(sa.String)
