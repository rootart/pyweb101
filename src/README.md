# Pyweb101#
## Prerequisites ##

- python >= 2.5
- pip
- virtualenv/wrapper (optional)

## Installation ##
### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv --no-site-packages pyweb101-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages --disctribute pyweb101-env
cd pyweb101-env
source bin/activate
```

### Clone the code ###
Obtain the url to your git repository.

```bash
git clone <URL_TO_GIT_RESPOSITORY> pyweb101
```

### Install requirements ###
```bash
cd pyweb101
pip install -r requirements.txt
```

### Configure project ###
```bash
cp pyweb101/__local_settings.py pyweb101/local_settings.py
vi pyweb101/local_settings.py
```

### Sync database ###
```bash
python manage.py syncdb
```

### Apply database migrations ###
```bash
python manage.py migrate
```

## Running ##
```bash
python manage.py runserver
```
or 
```
make run
```

Open browser to http://127.0.0.1:8000
