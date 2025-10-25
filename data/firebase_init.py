import json
import firebase_admin
from firebase_admin import credentials, firestore
import os

def init_firebase():
    if not firebase_admin._apps:
        key_data = json.loads(os.environ.get("FIREBASE_KEY"))
        cred = credentials.Certificate(key_data)
        firebase_admin.initialize_app(cred)
    return firestore.client()
