from flask import Blueprint

cache_bp = Blueprint('cache', __name__, url_prefix='/cache')

@cache_bp.route('/status')
def cache_status():
    return {'status': 'Cache module is running'}