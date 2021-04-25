from website import db, create_app, models

app = create_app()
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # code for mac
    # app.run(host='0.0.0.0', port=5000, debug=True)

    # code for Linux
    app.run(debug=True)
