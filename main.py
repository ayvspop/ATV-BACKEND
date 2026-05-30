import firebase_admin
from firebase_admin import credentials, db
import json
import os

# GitHub Secrets থেকে ডাটা নেওয়া
firebase_json = os.environ.get('FIREBASE_CONFIG')
database_url = os.environ.get('DATABASE_URL')

# Firebase কানেক্ট করা
if not firebase_admin._apps:
    cred_dict = json.loads(firebase_json)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred, {
        'databaseURL': database_url
    })

def fetch_and_save():
    # ডাটাবেসের রুট (/) থেকে সব ডাটা নেওয়া
    ref = db.reference('/')
    data = ref.get()

    # ডাটা JSON ফাইল হিসেবে সেভ করা
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print("Data fetched and saved to data.json")

if __name__ == "__main__":
    fetch_and_save()
