from .audition import Audition

class Actor:
    
    def __init__(self, name):
        self.name = name 


    @property
    def auditions(self):
        return [ a for a in Audition.all if a._actor == self ]
    
    @property
    def roles(self):
        return [a._role for a in self.auditions ]

    @property
    def characters(self):
        return [r.character_name for r in self.roles]
    
    @property
    def paychecks(self):
        return [a._role.character_name for a in self.auditions if a.hired == True]
