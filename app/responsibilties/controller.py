# Related third party imports
from flask import (
    jsonify,
)

from app.responsibilties.constants import (
    RESPONSIBILITY,
)


def fetch_responsibilty():
    return jsonify(RESPONSIBILITY)
