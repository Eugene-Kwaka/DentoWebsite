# DentoWebsite
A landing Page for Dento Dental Clinic where one can view the services offered and blogs written by the dentists. It als 

# Table of Contents
- [Background](#background)
- [Minimum Requirements](#minimum-requirements)
- [Quickstart](#quickstart)
- [Database SetUp](#database-setup)
- [Database Migration](#database-migration)
- [Deployment](#deployment)

## Background
This project is a landing page for Dento Dental Clinic with a Patient Appointment Management functionality and Blog functionality. The website displays the clinic's services and their prices, dental blog posts and the appointment function where logged in users can book and edit appointments.
The project applies Django's MVT(Model View Templates) architecture. It has a CRUD (Create Read Update Delete) application for the Appointments, Services, Blog posts and their Comments. Authentication and Authorization requires users to register and login so that they can make appointments as well as comment to the blog articles posted.
The project is written with Function-Based Views (FBV) with focus on core fundamentals which are easy to read, understand and implement.
Images uploaded in the project are stored using Amazon AWS S3 buckets helping the project to scale.


## Minimum Requirements
This project supports Ubuntu Linux 20.04 and Windows OS with their previous stable releases. It has not been tested on Mac OS.

- [Python3](https://www.python.org/downloads/)
- [Django 3.2](https://www.djangoproject.com/)
- [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
- [PostgreSQL 14.2+](http://www.postgresql.org/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [Git](https://git-scm.com/downloads)
- [AWS S3](https://www.google.com/aclk?sa=L&ai=DChcSEwjw-OrX0uj3AhWHj2gJHR2tA1MYABAAGgJ3Zg&sig=AOD64_1dIz703lEW0QpX4fG74DGCYFcZ5Q&q&adurl&ved=2ahUKEwjGheLX0uj3AhU0SvEDHUjgDnEQ0Qx6BAgCEAE)


## Quickstart
```bash
$ mkdir dentodental
$ cd dentodental
$ git init
$ git clone https://github.com/Eugene-Kwaka/DentoWebsite.git
$ cd DentoWebsite
$ sudo apt install python3-pip python3-django
$ sudo apt install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Database Setup
``` settings.py
'ENGINE': 'django.db.backends.postgresql',
'NAME': ('DB_NAME'),
'USER': ('DB_USER'),
'PASSWORD': ('DB_PASSWORD'),
'HOST': ('DB_HOST'),
'PORT': ('DB_PORT')
```

## Database Migration
```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

## Deployment
We'll deploy our application to Heroku. Heroku is a cloud hosting platform that I have used with Amazon Web Services (AWS) infrastructure with rapid scaling capabilities, offering flexible deployment services for all kinds of applications. Its ease of use makes it particularly suitable for fast development cycles.

```bash
$ git init
$ heroku login
$ heroku create <your_app_name>
$ heroku config:set DISABLE_COLLECTSTATIC=1
$ heroku config:set SECRET_KEY=<your_secret_key>
$ heroku config:set AWS_ACCESS_KEY_ID=<your_access_key>
$ heroku config:set AWS_SECRET_ACCESS_KEY=<your_secret_access>
$ heroku config:set AWS_STORAGE_BUCKET_NAME=<your_bucket_name>
$ heroku config:set DATABASE_NAME=dentodental
$ heroku config:set DATABASE_USER=postgres
$ heroku config:set DEBUG_VALUE=True
$ heroku run python manage.py migrate
$ heroku open #the app should be served in your browser
```
