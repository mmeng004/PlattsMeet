from django.shortcuts import render
from pyrebase import pyrebase
# Create your views here.


config={
  "apiKey": "AIzaSyACgDB0GPZvCwe86mppBtWJWiW_lsiekLs",
  "authDomain": "plattsmeet-8c552.firebaseapp.com",
  "databaseURL": "https://plattsmeet-8c552-default-rtdb.firebaseio.com",
  "projectId": "plattsmeet-8c552",
  "storageBucket": "plattsmeet-8c552.appspot.com",
  "messagingSenderId": "905839026225",
  "appId": "1:905839026225:web:b974341bebd7d86b823510",
  "measurementId": "G-S6VMXBM11D"
}

#here we are doing firebase authentication
firebase=pyrebase.initialize_app(config)
auth = firebase.auth()
database=firebase.database()


def index(request):
        #accessing our firebase data and storing it in a variable
        name = database.child('Data').child('Name').get().val()
        stack = database.child('Data').child('Stack').get().val()
        framework = database.child('Data').child('Framework').get().val()
    
        context = {
            'name':name,
            'stack':stack,
            'framework':framework
        }
        return render(request, 'index.html', context)
