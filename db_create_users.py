from project import db
from project.models import User

# insert data
db.session.add(User("user1", "user1@notemail.com", "this is a password"))
db.session.add(User("admin", "ad@min.com", "admin"))
db.session.add(User("tom", "tom@tomstuff", "1qaz2wsx!QAZ@WSX"))

# commit the changes
db.session.commit()