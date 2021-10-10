from abc import ABC, abstractclassmethod


class MatchManager(ABC):

    def __init__(self):
        self.match =None

    def set_match(self,match):
        self.match = match
        self.post_init()

        def end_match(self):
            self.match.active= False

        @abstractclassmethod
        def post_int(self):
            pass



class MatchVisitTemplate(ABC):
    def process_visit(self,player_index, visit):
        status, message = self.validate_visit(player_index, visit)
        if status is False:
            return -1, message

        result = self.check_winning_condition(player_index, visit)

        self.record_statistics(player_index,visit,result)

        return result,self.format_summary(player_index, visit)

    @abstractclassmethod
    def validate_visit(self,player_index,visit):
        pass

    @abstractclassmethod
    def check_winning_condition(self, player_index, visit):
        pass

    @abstractclassmethod
    def record_statistics(self, player_index, visit, result):
        pass

    @abstractclassmethod
    def format_summary(self, player_index, visit):
        pass