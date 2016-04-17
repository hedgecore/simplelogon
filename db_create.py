from project import db
from project.models import User

#create the database and the db tables
db.create_all()

# insert
#db.session.add(aboutme("user1", "user1@notmail.com"))
#db.session.add(BlogPost("well", "I\'m well."))
#db.session.add(BlogPost("postgres", "local postgres instance"))



#commit the changes
db.session.commit()
