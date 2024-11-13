import firebase_admin
from firebase_admin import credentials, firestore

class Firebase:
    
    def __init__(self):
        self.cred: credentials.Certificate = None
        self.app = None 
        self.db = None 
        
    def connect(self)-> None:
        if not firebase_admin._apps:
            self.cred = credentials.Certificate(cert='/Users/felipelima/Documents/Projects/Python/cross-line/src/models/test-upx5-firebase-adminsdk-65nw1-79a9840ca2.json')
            self.app = firebase_admin.initialize_app(self.cred)

        self.db = firestore.client()
        
        print('conectado com sucesso')
        
    def post(self, data:dict):
        self.db.collection("monitory").add(data)
        print('registrado no database')