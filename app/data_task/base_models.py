class Credentials(object):
    def __init__(self, provider):
        self.provider = provider
        self.user_id= "none"

    def add_credentials(self):
        #This method must be redefined.
        pass

    def set_user_id(self,user_id):
        self.user_id=user_id

    def get_user_id(self):
        return self.user_id

    def __str__(self):
        return "provider: %s" % self.provider

class Task(object):
    def __init__(self, id_celery, name):
        self.id_celery = id_celery
        self.name=name

class DataOfTask(object):
    def __init__(self, name):
        self.name=name
