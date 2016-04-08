#Statement for enabling the development environment
#TODO change it to false after dev
DEBUG = True

#Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#Define the database
#TODO
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')

#Applications threads
THREADS_PER_PAGE = 2

#Enable protection against CSRF
CSRF_ENABLED = True

