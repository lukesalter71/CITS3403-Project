export FLASK_APP=./main.py
flask db init
flask db migrate -m "Running migrations"
flask db upgrade