# final_project/blog/models.py

from . import db
import datetime
from faker import Faker

# MODEL
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.datetime.utcnow)
    is_published = db.Column(db.Boolean, default=False)

# FAKER
fake = Faker()

def generate_entries(how_many=10):
    for _ in range(how_many):
        entry = Entry(
            title=fake.sentence(nb_words=6),
            body='\n'.join(fake.paragraphs(3)),
            is_published=True
        )
        db.session.add(entry)
    db.session.commit()


