## Tutorial Project

### Getting started with Django.

Step 1: Activate Virtual Env
```commandline
python -m venv venv
source venv/bin/activate
```

Step 2: Clone this.

Step 3: Install Project Dependencies
```commandline
python -m pip install -r requirements.txt
```

Step 4: Run Migrations
```commandline
python manage.py makemigrations
python manage.py migrate
```

Step 5: Run Server
```commandline
python manage.py runserver
```

Step 6: Play

- Get all Users API
```commandline
GET localhost:8000/api/users
```
- Get Single User API
```commandline
GET localhost:8000/api/user/{id}
```

- Create User
```commandline
POST localhost:8000/api/users
Body: 
email: email@gmail.com
password: password
username: testuser
```
 
- Edit User
```commandline
PUT localhost:8000/api/user/{id}
Body: 
email: email@gmail.com
password: password
username: testuser
```

- Delete User
```commandline
DELETE localhost:8000/api/users/{id}
```
### Unit Test
```commandline
python manage.py test
```


### Create Super User
```commandline
python manage.py createsuperuser 
```

- Login to Admin
```commandline
localhost:8000/admin
```