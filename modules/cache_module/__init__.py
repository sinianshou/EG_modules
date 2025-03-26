# 使用绝对导入路径
from .routes import cache_bp

def init_cache_module(app):
    # 注册路由
    app.register_blueprint(cache_bp)
    app.logger.info("✅ [Cache] 缓存模块已加载")