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

## Posting shapes and colors
### Shapes
Endpoint:
`/challenge1/shapes`

Payload body format:
`{"name": "<shape name>", "fa_class": "<FontAwesome class names>"}`

Example:
```
fetch('/challenge1/shapes', {
    method: "POST",
    mode: "same-origin",
    headers: {
        "Content-Type": "application/JSON",
        "X-CSRFToken": <your token>
    },
    body: JSON.stringify({"name": "circle", "fa_class": "fa-solid fa-circle"})
}).then(response => {return response.json()})
```

### Colors
Endpoint:
`/challenge1/colors`

Payload body format:
`{"color1": "<hexcode or HTML color name>", "color2": "<hexcode or HTML color name>", "color3": "<hexcode or HTML color name>", "color4": "<hexcode or HTML color name>"}`

Example:
```
fetch('/challenge1/shapes', {
    method: "POST",
    mode: "same-origin",
    headers: {
        "Content-Type": "application/JSON",
        "X-CSRFToken": <your token>
    },
    body: JSON.stringify({"color1": "#D3D3D3", "color2": "#A9A9A9", "color3": "#696969", "color4": "#202020"})
}).then(response => {return response.json()})
```