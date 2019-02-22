from boxsdk import JWTAuth
from boxsdk import Client
import os

class Provider(object):

    def __init__(self, config_path):
        self._sdk = JWTAuth.from_settings_file(config_path)
        self._client = Client(self._sdk)
        print("init {name}".format(name=self.__class__.__name__))

    def put(self, filename):
        items = self._client.search().query(filename)
        if len(items) > 0 & items[0].name == filename:
            file_id = items[0].id
            file = self._client.file(file_id).update_contents(filename)
            print("updated ", filename)
        else:
            file = self._client.folder('0').upload_file(filename)
            print("put ", filename)
        return file


    def get(self, filename):
        items = self._client.search().query(filename)
        if len(items) > 0 & items[0].name == filename:
            file_id = items[0].id
            with open(filename, 'wb') as f:
                self._client.file(file_id).download_to(f)
        print("Downloaded ", filename)

    def delete(self, filename):
        items = self._client.search().query(filename)
        if len(items) > 0 & items[0].name == filename:
            file_id = items[0].id
            self._client.file(file_id).delete()
            print("Deleted ", filename)
        else:
            print("No file found with name ", filename)

    def size(self, filename):
        items = self._client.search().query(filename)
        if len(items) > 0:
            size = items[0].size
            name = items[0].name
            print(name, " is ", size, " bytes.")
        else:
            print("No file found with name ", filename)

    def info(self, filename):
        items = self._client.search().query(filename)
        if len(items) > 0:
            file_id = items[0].id
            file = self._client.file(file_id).get()
            for key in file:
                print(key, " : ", file[key])
        else:
            print("No file found with name ", filename)

    def create(self, filename):


    def sync(self, source, dest):
        files = []
        for file in os.listdir(source):
            self.put(self, file)
            files.append(file)


