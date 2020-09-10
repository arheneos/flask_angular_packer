from uuid import uuid4
import pymongo
import datetime


class MongoSession:

    def __init__(self, mongo_client: pymongo.MongoClient):
        self.mongo = mongo_client
        self.db = mongo_client.AngularSession
        self.session = self.db.session

    def get_session(self, sid: str):
        return self.session.find_one({'sid': sid})

    def all_user_session(self, username: str):
        return self.session.find({'username': username})

    def create_session(self, username: str) -> str:
        uid = str(uuid4())
        session_data = dict(
            username=username,
            expires=datetime.datetime.utcnow() + datetime.timedelta(days=60),
            sid=uid
        )
        self.session.insert(session_data)
        return uid

    def remove_session(self, sid: str):
        pass
