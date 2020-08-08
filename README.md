# ttt-terriblytinytales

> Frequency computation app built by using Django and html

## Usage

Insatll [python](https://www.python.org/) and other essentials
```
apt-get install python3
apt-get install python3-pip
pip3 install virtualenv

```


Install [Django](https://docs.djangoproject.com/en/3.0/topics/install/) 

```
cd ~
mkdir django-apps
cd django-apps
virtualenv env
source env/bin/activate
pip install django

```

Config Django

```
cd ~/django-apps
django-admin startproject mysite
```

Confirm that debug mode is enabled: `DEBUG = True`

Locate the ALLOWED_HOSTS line and then modify xxx.xxx.xxx.xxx with the IP address of your server `ALLOWED_HOST =["XXXX.XXXX.XXXX.XXXX"]`

To start the server 

```
python manage.py runserver
```

After running sever the project will be host on the given ip in your terminal {Ex: 127.0.0.1:8XXX / local host}

```
Use requirement.txt to use all the library for this project
```


## Giving Back

- sanyamkarnawat
