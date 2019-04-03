# nanohr_backend
The backend to NanoHr

## Contributing

Follow these steps to start contributing  
1.Clone the project, `https://github.com/mugagambi/nanohr_backend.git`   
2.cd to the project root and create a python virtualenv .    
3.Activate the virtualenv. run `pip install -r requirements.txt ` to install dependencies  
4.Then copy .env.example to .env and make the necessarily changes. On unix systems `cp .env.example .env`  
5.Migrate to update the database schema `python manage.py migrate`. Make sure to use postgresql because the system depends on postgres specific features.    
6.Create super user to access the admin `python manage.py createsuperuser`    
7.Finally run server. `python manage.py runserver`  

In case of questions . open a github issue.
thanks
