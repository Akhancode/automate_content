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

    # Initialize the database with the app
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Import and register routes
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
def start_monitoring():
    try:
        # get load and define function of scanning change
        monitor = ArticleMonitor()

        # Run the article monitor in a separate thread
        monitor_thread = threading.Thread(target=monitor.detect_new_articles())
        monitor_thread.daemon = True
        monitor_thread.start()
    except Exception as e:
        print(e)
