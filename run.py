from pack import app
from pack.init_db import init_db

if __name__ == '__main__':
    init_db()  # Initialize database and add sample movies
    app.run(debug=True)  