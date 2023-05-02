import abc

class AbstractCollegeTeam(abc.ABC):

    name: str
    
    def __init__(self,division,conference_name):
        self.division = division
        self.conference_name = conference_name
        