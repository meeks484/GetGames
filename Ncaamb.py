import requests
from AbstractSportRadar import AbstractSportRadar
from typing import Final

class Ncaamb(AbstractSportRadar):
    SPORT_URL: Final = "/ncaamb/trial/v7/en/"
    EXTENDED_URL: Final = AbstractSportRadar.BASE_URL + SPORT_URL

    __instance = None

    @staticmethod
    def get_instance(api_key):
        if Ncaamb.__instance == None:
            Ncaamb(api_key)
        return Ncaamb.__instance
    

    def __init__(self, api_key):
        if Ncaamb.__instance != None:
            raise Exception("You cannot create more than one instance of SportradarNCAAMB")
        else:
            self.api_key = api_key
            Ncaamb.__instance = self


    def gameIdBySeason(self,season):
        final_url = self.EXTENDED_URL + "games/" + season + "/REG/schedule.json?api_key=" + self.api_key
        response = requests.get(final_url)
        data = response.json()
        game_ids = game_ids = [game['id'] for game in data['games']]
        return game_ids

    def statsByGameId(self,game_id):
        final_url = self.EXTENDED_URL + "games/" + game_id + "/summary.json?api_key=" + self.api_key
        response = requests.get(final_url)
        data = response.json()
        if data["status"] == "postponed":
            return "postponed"
        date = data["scheduled"][0:10]
        home_team = self.__teamGameSummary(site="home",data=data)
        away_team = self.__teamGameSummary(site="away",data=data)
        return{
            "date": date,
            "home_team": home_team,
            "away_team": away_team
        }

    def teamSummary(self, team_id):
        final_url = self.EXTENDED_URL + "teams/" + team_id + "/profile.json?api_key=" + self.api_key
        response = requests.get(final_url)
        data = response.json()
        conference_id = data["conference"]["id"]
        conference_name = data["conference"]["name"]
        division_id = data["division"]["id"]
        division_name = data["division"]["alias"]
        return {
            "conference_id": conference_id,
            "conference_name": conference_name,
            "division_id": division_id,
            "division_name": division_name 
        }


    def __teamGameSummary(self, site, data):
        team_id = data[site]["id"]
        name = data[site]["name"]
        alias = data[site]["alias"]
        market = data[site]["market"]
        points = data[site]["points"]
        free_points = data[site]["statistics"]["free_throws_made"]
        two_points = data[site]["statistics"]["two_points_made"]
        three_points = data[site]["statistics"]["three_points_made"]
        offensive_rebounds = data[site]["statistics"]["offensive_rebounds"]
        defensive_rebounds = data[site]["statistics"]["defensive_rebounds"]
        steals = data[site]["statistics"]["steals"]
        blocks = data[site]["statistics"]["blocks"]
        return {
            "id": team_id,
            "name": name,
            "alias": alias,
            "market": market,
            "points": points,
            "free_points": free_points,
            "two_points": two_points,
            "three_points": three_points,
            "offensive_rebounds": offensive_rebounds,
            "defensive_rebounds": defensive_rebounds,
            "steals": steals,
            "blocks": blocks
        }
    
    def getRpi(self,season):
        final_url = self.EXTENDED_URL + "rpi/" + season + "/rankings.json?api_key=" + self.api_key
        response = requests.get(final_url)
        data = response.json()


        rpi = list(map(lambda x: {k: x[k] for k in ('id', 'sos', 'rpi')},data['rankings']))
       
        # def keep_selected_keys(dictionary):
        # selected_keys = ["name", "age", "gender"]
        # new_dict = {}
        # for key in selected_keys:
        #     if key in dictionary:
        #         new_dict[key] = dictionary[key]
        # return new_dict

        # new_list = [keep_selected_keys(old_dict) for old_dict in old_list]

        return rpi
    

   





