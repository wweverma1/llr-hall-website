from flask import Blueprint

from app.noticeboard.controller import (
    create_notice,
    fetch_notice,
    # update_notice,
    delete_notice,
)

noticeboard_api = Blueprint('noticeboard', __name__)

noticeboard_api.add_url_rule(rule='/noticeboard/create', view_func=create_notice, methods=['POST', ])
# noticeboard_api.add_url_rule(rule='/noticeboard/<int:notice_id>/edit', view_func=update_notice, methods=['PUT', ])
noticeboard_api.add_url_rule(rule='/noticeboard/<int:notice_id>/fetch', view_func=fetch_notice, methods=['GET', ])
noticeboard_api.add_url_rule(rule='/noticeboard/<int:notice_id>/delete', view_func=delete_notice, methods=['GET', ])
