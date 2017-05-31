class Credentials(object):
    def __init__(self, provider,username):
        self.provider = provider
        self.username_provider = username_provider

class Task(object):
    def __init__(self,id_celery,name):
        self.id_celery = id_celery
        self.name=name

class DataOfTask(object):
    def __init__(self, name):
        self.name=name
