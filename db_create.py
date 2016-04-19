from project import db
from project.models import BlogPost


db.create_all()

# insert
#db.session.add(BlogPost("user1", "user1@notmail.com"))
#db.session.add(BlogPost("...", "..."))
#db.session.add(BlogPost("...", "..."))



db.session.commit()
