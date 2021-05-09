from website import db, create_app, models
import os
app = create_app()
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # code for mac
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    # code for Linux
    # app.run(debug=True)
