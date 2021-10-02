# Related third party imports
from flask import Blueprint

from app.responsibilties.controller import (
    fetch_responsibilty,
)

responsibilties_api = Blueprint('responsibilties', __name__)

responsibilties_api.add_url_rule(rule='/responsibilties/fetch_responsibilty_type',
                                 view_func=fetch_responsibilty, methods=['GET', ])
