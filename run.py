from app import create_app
from app.monitor import ArticleMonitor
import threading

app = create_app()

def start_monitoring():
    monitor = ArticleMonitor()
    monitor.detect_new_articles()

if __name__ == "__main__":
    # Run the article monitor in a separate thread
    monitor_thread = threading.Thread(target=start_monitoring)
    monitor_thread.start()

    # Start Flask application
    app.run(debug=True,use_reloader=False)
