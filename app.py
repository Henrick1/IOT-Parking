from controllers.app_controller import create_app
from utils.create_db import create_db

if __name__ == "__main__":
    app = create_app()
    create_db(app)
    app.run(host='127.0.0.1', port=5000)
