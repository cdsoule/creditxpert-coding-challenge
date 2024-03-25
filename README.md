# CreditXpert Coding Challenges

## Requirements
- Python3 (tested on 3.12.2)

## Set up environment (macOS/Linux)
1. Clone repo
- `$ git clone git@github.com:cdsoule/creditxpert-coding-challenge.git`
2. Enter directory
- `$ cd creditxpert-coding-challenge`
3. Create virtual environment
- `$ python -m venv venv`
4. Activate venv
- `$ . venv/bin/acitvate`
5. Install requirements
- `$ python -m pip install -r requirements.txt`

## Local deployment
1. Migrate
- `$ python manage.py migrate`
2. Run server
- `$ python manage.py runserver`
3. Open application
- http://localhost:8000

Optional:
1. Create superuser
- `$ python manage.py createsuperuser`
- This allows you to add new shapes and color schemes through the admin page. Adding shapes and color schemes can also be done through the POST method