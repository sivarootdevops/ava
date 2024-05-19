import pymongo


class DatabaseClient:
    db: pymongo.MongoClient
    def __init__(self, host: str, port: int, username: str, password: str) -> None:
        self.host = host
        self.port = port
        self.username = username
        self.password = password
    
    def connect(self):
        DatabaseClient.db = pymongo.MongoClient(f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/?authSource=admin")
        print(DatabaseClient.db.server_info())
        
    @staticmethod
    def get():
        return DatabaseClient.db
        