from app import create_app
from app.services.monitor import ArticleMonitor

app = create_app()


if __name__ == "__main__":

    # Start Flask application
    app.run(debug=False,use_reloader=False)
