from typing import Final

class BasketballGame():

    TWO_POINT: Final[int] = 2
    THREE_POINT: Final[int] = 3

    __instance = None

    team = {
        "alias": str,
        "name": str,
        "home_team": bool,
        "date": str,
        "winner": bool,
        "delta": int,
        "opp_alias": str,
        "opp_name": str,
    }

    @staticmethod
    def get_instance():
        if BasketballGame.__instance == None:
            BasketballGame()
        return BasketballGame.__instance
    
    def __init__(self):
        if BasketballGame.__instance != None:
            raise Exception("You cannot create more than one instance of Basketball Game")
        else:
            BasketballGame.__instance = self




    def getHomeTeam(self,game_data) -> team:
        return self.__extractInfo("home_team",game_data)
    


    
    def getAwayTeam(self,game_data) -> team:
        return self.__extractInfo("away_team",game_data)




    def __extractInfo(self,site,game_data) -> team:
        team = {}
        if site == "home_team":
            team["home_team"] = True
            opponent: str = "away_team"
        else:
            team["home_team"] = False
            opponent: str = "home_team"
        
        team["id"] = game_data[site]["id"]
        team["alias"] = game_data[site]["alias"]
        team["name"] = game_data[site]["name"]
        team["school"] = game_data[site]["market"]
        team["opp_id"] = game_data[opponent]["id"]
        team["opp_alias"] = game_data[opponent]["alias"]
        team["opp_name"] = game_data[opponent]["name"]

        team["date"] = game_data["date"]

        points = game_data[site]["points"]
        opponent_points = game_data[opponent]["points"]
        if points > opponent_points: 
            team["winner"] = True
        else:
            team["winner"] = False
        
        two_points = game_data[site]["two_points"] * self.TWO_POINT
        three_points = game_data[site]["three_points"] * self.THREE_POINT
        field_goals = two_points + three_points

        opponent_two_points = game_data[opponent]["two_points"] * self.TWO_POINT
        opponent_three_points = game_data[opponent]["three_points"] * self.THREE_POINT
        opponent_field_goals = opponent_two_points + opponent_three_points

        team["delta"] = field_goals - opponent_field_goals
        return team
        




        


        

    