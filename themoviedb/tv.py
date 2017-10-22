class TV(object):
    def __init__(self, id):
         self.id = id  #store the id as instance variable

    def info(self):
        return {'id': self.id}