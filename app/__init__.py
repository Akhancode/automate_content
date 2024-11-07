from flask import Flask
from .config import Config
import threading
from .services.monitor import  ArticleMonitor
from .models import db


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
    # detecting new articles
    start_monitoring(app)
    return app
def start_monitoring(app):
    try:

        # Run detect_change in a thread with app context
        def run_in_context():
            with app.app_context():
                detect_change()
        monitor_thread = threading.Thread(target=run_in_context)
        monitor_thread.daemon = True
        monitor_thread.start()
    except Exception as e:
        print(e)
def detect_change():
    try:
        #Load article  and define function of scanning change
        monitor = ArticleMonitor()
        monitor.detect_new_articles()
    except Exception as e:
        print(e)
