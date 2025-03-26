from flask import Blueprint

cache_bp = Blueprint('cache', __name__, url_prefix='/cache')

@cache_bp.route('/status')
def cache_status():
    """获取缓存模块状态
    ---
    tags:
      - Cache
    responses:
      200:
        description: 缓存模块状态信息
        schema:
          properties:
            status:
              type: string
              description: 模块运行状态
    """
    return {'status': 'Cache module is running'}