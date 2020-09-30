# Course Enrollment Application

Student-Course Enrollment Application using Python, Flask and MongoDB.  

Functionalities:
1. APIS's to add/edit/remove students using flask_restplus library.
2. Store the Student and Course Data in MongoDB.
2. Form validation for login and registering a new student.
3. Flask Session Management for user login.
4. View available course list and enroll for required courses.
5. View enrolled courses for the current semester.

### Install the required dependencies:
Create a virtual environment and load the dependencies.
```sh
$ pip install requirements.txt
```


### Configuration:

Edit the config.py file to initialize the secret key and database.

```py
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'enter-secret-key'
    MONGODB_SETTINGS = { 'db' : 'Db_Name'}
```

### To execute the script:

Navigate to the root project folder and run the script.

```sh
$ python3 main.py
```
