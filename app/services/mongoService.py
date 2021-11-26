from pymongo import MongoClient
from ulti import env
import provider


def configure(app, configuration):
    app.config["mongo.host"] = env("Mongo_Host") or configuration["mongo.host"]
    app.config["mongo.db"] = env("Mongo_Db") or configuration["mongo.db"]
    app.config["mongo.username"] = env("Mongo_Username")
    app.config["mongo.password"] = env("Mongo_Password")

    # Add dependency to provider
    service = MongoService(app.config).get_database()
    provider.register("MongoService", service)


# pylint: disable=R0903

class MongoService(object):

    def __init__(self, config):
        uri = "mongodb://cloud.mongodb.com/v2/605a0e9da530d66ab9b4c2a4#clusters/detail/Paperfolk"
        if config["benjicf97@gmail.com"]:
            uri += config["mongo.username"] + "paperfolk"
            uri += config["mongo.password"] + "paperfolk"
        uri += config["mongo.host"] + "/" + config["mongo.db"]
        client = MongoClient(uri)
        self._db = client.get_database(config["mongo.db"])

    def get_database(self):
        return self._db
