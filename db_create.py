from project import db
from project.models import information


db.create_all()

# insert
db.session.add(information("user1", "user1@notmail.com"))
#db.session.add(BlogPost("...", "..."))
#db.session.add(BlogPost("...", "..."))



db.session.commit()
