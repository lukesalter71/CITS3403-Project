import os, unittest
import sqlite3

import sqlalchemy.exc

from website.models import User, Score
from website import db, create_app, models
import os


def load_database(num_entries):
    name = "Abdi"
    score = 111
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    for i in range(num_entries):
        c.execute('INSERT INTO Score (name, score) VALUES (?, ?)', [name, score])
    conn.commit()


class UserTestCase(unittest.TestCase):

    def setUp(self):
        app = create_app()
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        app_ctx = app.app_context()
        app_ctx.push()
        db.create_all()
        s1 = User(name="Abdi", email="Abdi@gmail.com", password=1234)
        s2 = User(name="Farshad", email="Farshad@gmail.com", password=123)
        score1 = Score(name="Abdi", score=180)
        score2 = Score(name="Farshad", score=180)

        db.session.add(s1)
        db.session.add(s2)
        db.session.add(score1)
        db.session.add(score2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_details(self):
        user = User.query.get(1)
        self.assertEqual(user.name, "Abdi")
        self.assertEqual(user.email, "Abdi@gmail.com")
        self.assertEqual(user.password, '1234')

        user = User.query.get(2)
        self.assertEqual(user.name, "Farshad")
        self.assertEqual(user.email, "Farshad@gmail.com")
        self.assertEqual(user.password, '123')

    def test_user_scores(self):
        score = Score.query.get(1)
        self.assertEqual(score.name, "Abdi")
        self.assertEqual(score.score, 180)

        score = Score.query.get(2)
        self.assertEqual(score.name, "Farshad")
        self.assertEqual(score.score, 180)

    def test_duplicate_user_entry(self):
        s1 = User(name="Abdi", email="Abdi@gmail.com", password=1234)
        s2 = User(name="Farshad", email="Farshad@gmail.com", password=123)
        score1 = Score(name="Abdi", score=180)
        score2 = Score(name="Farshad", score=180)

        db.session.add(s1)
        db.session.add(s2)
        db.session.add(score1)
        db.session.add(score2)
        with self.assertRaises(Exception) as context:
            self.assertRaises(sqlalchemy.exc.IntegrityError, db.session.commit())

    def test_multiple_score_entries(self):
        expected_marks = [{'name': 'Abdi', 'submissions': 26, 'average': 113.65384615384616}]
        name = "Abdi"
        conn = sqlite3.connect('test.db')
        load_database(num_entries=25)
        c = conn.cursor()
        c.execute(
            'SELECT name AS student_name, COUNT(*) AS sumbissions, AVG(score) FROM score WHERE name = ? GROUP BY name',
            [name])
        actual_marks = [dict(name=row[0], submissions=row[1], average=row[2]) for row in c.fetchall()]
        self.assertEqual(expected_marks, actual_marks)


if __name__ == "main":
    unittest.main()