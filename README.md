# StonerIndia
The Website is based on Django v2.0.2 on python3 

INSTALL DJANGO:

$ sudo apt update
$ sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
$ pip3 install virtualenv

# Now create a folder to clone the repo into.
$ mkdir StonerIndiaDev
$ git clone https://github.com/ShlokParida/StonerIndia.git

#Now create Virtual Environment
$ cd StonerIndiaDev
$ pip3 install virtualenv
$ virtualenv <Virtual env name>
# to activate virtual env
$ source <Virtual env name>/bin/activate



#Install requirements
Activate venv
$ sudo pip3 install django==2.0.2
$ sudo pip3 install Pillow
$ sudo pip3 install psycopg2

#Once Installed everything you need to create a database in postgres
$ sudo -u postgres psql
CREATE DATABASE stonerdb;
\password postgres
admin1234

# now navigate to the directory of the clone after activating venv
# once inside
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py runserver

localhost:8000 in browser will take you to webpage.
