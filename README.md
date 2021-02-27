# Once you clone the repo

Change the password there to your own password

If on windows make changes to the config.py 

- with open(f'{BASDIR}\password.txt', 'r', encoding='utf-8') as f:
    password = f.readline()

# If you don't have the postgress
Use the sqlite and change your database config to

 "
 SQLALCHEMY_DATABASE_URI = os.path.join('sqlite:///temp/app.db')
 "

# Then run the following commands

- $ cd blog/
- $ pipenv shell
- $ pipenv install -r requirements.txt
- $ export FLASK_APP=server.py
- $ flask db init 
- $ flask db migrate -m "Creating initial tables"
- $ flask db upgrade
- $ python server.py
- $ 