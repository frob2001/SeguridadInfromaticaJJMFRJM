import pyrebase

config = {
  "apiKey": "AIzaSyA0WOAjtkDTPo1GWaEQaUpEMyieQL55o84",
  "authDomain": "seguridadinformatica-20c54.firebaseapp.com",
  "databaseURL": "https://seguridadinformatica-20c54-default-rtdb.firebaseio.com/",
  "projectId": "seguridadinformatica-20c54",
  "storageBucket": "seguridadinformatica-20c54.appspot.com",
  "messagingSenderId": "23895164011",
  "appId": "1:23895164011:web:43e8339655266e4cd15d2e",
  "measurementId": "G-BDW3XVM0CY"
}

firebase = pyrebase.initialize_app(config)
fdb = firebase.database()
auth = firebase.auth()