
class Audition:

    all = []
    
    def __init__(self,location, role, actor):
        self.location = location
        self._role = role 
        self._actor = actor 
        self.hired = False
        Audition.all.append(self)


    @property
    def role(self):
        return self._role

    @property
    def actor(self):
        return self._actor  
    
    def call_back(self):
        self.hired = True
        return self.hired