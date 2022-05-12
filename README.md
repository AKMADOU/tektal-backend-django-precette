# Backend

Template django qui qui intègre l'authentification token

How do I get set up?

####1. Create a python environment####
The environement setup process depends on your system. Do some research to find out how to do it on OS.
For Ubuntu you can use the following commands
#!bash
virtualenv -p python3 env
source env/bin/activate

####2. Clone the repo and move to the project folder####
#!bash
git clone *repo_url*
cd django_backend

####3. Install required python packages####
#!python
pip install -r requirements.txt

####4. Apply database migrations####
#!bash

python manage.py makemigrations
python manage.py migrate


####5. Run the app####
#!bash

python manage.py runserver

The api should now be running at http://127.0.0.1:8000/

Troubleshooting
If there is any problem during the installation of the python package, just install each them one by one using pip install package_name.
The most important packages are django, djangorestframework, djangorestframework-jwt and mixer.