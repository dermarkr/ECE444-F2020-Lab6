# create_db.py


from project.app import db
from project.models import Post


# create the database and the db table
db.create_all()

# commit the changes
db.session.commit()