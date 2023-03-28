from .audition import Audition

class Role:
    
    def __init__(self, character_name):
        self.character_name = character_name


    @property
    def auditions(self):
        return [ a for a in Audition.all if a.role == self ]
    
    @property
    def actors(self):
        return [a.actor.name for a in self.auditions ]
    
    @property
    def locations(self):
        return [a.location for a in self.auditions]

    @classmethod
    @property
    def allActorsName(cls):
        return [a.role.character_name for a in Audition.all if a.hired == True ]

    @classmethod
    def silver_screen (cls):
        unique = []
        for cn in cls.allActorsName:
            if len(unique) == 0 :
                unique.append(cn)
            if cn in unique:
                pass
            else:
                unique.append(cn)
        return unique


        
