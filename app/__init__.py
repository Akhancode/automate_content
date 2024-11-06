from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
import threading
from .services.monitor import  ArticleMonitor
# Initialize the SQLAlchemy instance
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    try:
        # Run the article monitor in a separate thread
        monitor_thread = threading.Thread(target=start_monitoring)
        monitor_thread.daemon = True
        monitor_thread.start()
    except Exception as e :
        print(e)

    # Initialize the database with the app
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Import and register routes
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
def start_monitoring():
        monitor = ArticleMonitor()
        monitor.detect_new_articles()