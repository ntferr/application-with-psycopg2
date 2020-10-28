from user import User
from database import Database

Database.initialise(database='', user='', password='', host='')
my_user = User('joão@teste.com', 'João', 'Mundi', None)
my_user.save_to_db()

user_from_db = User.load_from_db_by_email('joão@teste.com')

print(user_from_db)

