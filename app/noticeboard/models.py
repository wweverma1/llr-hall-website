# Standard library imports
from datetime import datetime
import traceback

# Related third party imports
from sqlalchemy.exc import SQLAlchemyError

# Local app specific imports
from app import (
    db,
    SCHEMA_NAME,
)


class Notice(db.Model):
    __table_args__ = ({"schema": SCHEMA_NAME})
    __tablename__ = 'notice'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.String(100))
    title = db.Column(db.String(100))
    poster_url = db.Column(db.Text)
    description = db.Column(db.Text)
    is_updated = db.Column(db.Boolean)

    @staticmethod
    def create(created_by=None, title=None, poster_url=None, description=None):
        try:
            notice = Notice(
                created_at=datetime.now(),
                created_by=created_by,
                title=title,
                poster_url=poster_url,
                description=description,
                is_updated=False,
            )
            db.session.add(notice)
            db.session.commit()
            return notice
        except SQLAlchemyError as e:
            print(e)
            traceback.print_exc()
            db.session.rollback()
            return False
