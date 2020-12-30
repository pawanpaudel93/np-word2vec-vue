from server.app import app
from werkzeug.serving import run_simple

if __name__ == "__main__":
  run_simple("0.0.0.0", 5000, app, use_debugger=True, use_reloader=True)