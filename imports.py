import random as random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import hashlib

cred = credentials.Certificate(r"C:\Users\boras\OneDrive\Masaüstü\Python\projects\kelimeoyunu\config\firebase.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://tdka-81983-default-rtdb.firebaseio.com/"
})