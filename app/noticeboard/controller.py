from datetime import datetime

# Standard library imports
import json
import traceback
from sqlalchemy.exc import SQLAlchemyError

from flask import (
    jsonify,
    request,
)

# Local app specific imports
from app import (
    db,
)

from app.noticeboard.models import (
    Notice,
)


def create_notice():
    title = request.form['title']
    poster_url = request.form['poster_url']
    description = request.form['description']
    created_by = request.form['created_by']

    notice = Notice.create(created_by, title, poster_url, description)
    if not notice:
        return "Error creating Notice", 400
    return jsonify({"id": notice.id}), 200


def fetch_notice(notice_id):
    notice = db.session.query(Notice)\
        .filter(Notice.id == notice_id).one_or_none()
    if not notice:
        return "Invalid Notice ID", 404
    notice_data = {
        "id": notice.id,
        "title": notice.name,
        "desc": notice.description,
        "poster": notice.poster_url,
        "posted_by": notice.created_by,
        "posted_on": notice.created_at,
        "updated": "True" if notice.is_updated is True else "False",
    }
    return jsonify(notice_data), 200


# def update_notice(notice_id):


def delete_notice(notice_id):
    notice = db.session.query(Notice)\
        .filter(Notice.id == notice_id).one_or_none()
    if not notice:
        return "Invalid Notice ID", 404
    try:
        db.session.delete(notice)
        db.session.commit()
        return "Notice Deleted", 200
    except SQLAlchemyError as e:
        print(e)
        traceback.print_exc()
        db.session.rollback()
        return "Unable to delete Notice", 400
