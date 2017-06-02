class Credentials(object):
    def __init__(self, provider):
        self.provider = provider

    def add_credentials(self):
        #This method must be redefined.
        pass
 
    def __str__(self):
        return "provider: %s" % self.provider

class Task(object):
    def __init__(self, id_celery, name):
        self.id_celery = id_celery
        self.name=name

class DataOfTask(object):
    def __init__(self, name):
        self.name=name
