from dWo import app
from dWo.models import db, User, Course

with app.app_context():
    rel1 = Course.query.filter_by(course_name='Cloud Intro').first()
    rel1.owner = User.query.filter_by(username='syed').first().id
    db.session.add(rel1)
    db.session.commit()