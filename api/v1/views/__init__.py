from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from . import amenities
from . import cities
from . import index
from . import places
from . import states
from . import users
