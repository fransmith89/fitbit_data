from flask import Blueprint


core_api = Blueprint('core_api', __name__)


@core_api.route('/')
def status():
    return 'Running'
