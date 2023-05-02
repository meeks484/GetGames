import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class GameInfoDataBase():

    service_account_file = "sportsdata-f797a-firebase-adminsdk-qe2po-9677b11fd3.json"
    service_account_path = "C:/Users/meeks/Programming Projects/Web Projects/SportsCurves/GetGames/GetGames/" + service_account_file 

    firebaseConfig = {
        "apiKey": "AIzaSyA89xmcslAJIq4kyLbHfpBff_6mC92eGRA",
        "authDomain": "sportsdata-f797a.firebaseapp.com",
        "databaseURL": "https://sportsdata-f797a-default-rtdb.firebaseio.com",
        "projectId": "sportsdata-f797a",
        "databaseURL": "https://sportsdata-f797a-default-rtdb.firebaseio.com/",
        "storageBucket": "sportsdata-f797a.appspot.com",
        "messagingSenderId": "464579296164",
        "appId": "1:464579296164:web:f128381f227145d07f5f31",
        "measurementId": "G-R3JY8F8V8R"
    }

    __instance = None

    @staticmethod
    def get_instance():
        if GameInfoDataBase.__instance == None:
            GameInfoDataBase()
        return GameInfoDataBase.__instance

    def __init__(self):
        if GameInfoDataBase.__instance != None:
            raise Exception("You cannot create more than one instance of SportradarNCAAMB")
        else:
            GameInfoDataBase.__instance = self
            # firebase = pyrebase.initialize_app(self.firebaseConfig)
            cred = credentials.Certificate(self.service_account_path)
            firebase_admin.initialize_app(cred, {
                "databaseURL": "https://sportsdata-f797a-default-rtdb.firebaseio.com",
                "databaseAuthVariableOverride": {
                    'uid': 'gh6OAlNrFMcAYMnnwEYzLIE0Yiv2'
                }
            })
            self.database = db.reference('/')



    def push_game_info(self,game_id, season, game_info):
        self.database.child(season).child("Game_IDs").child(game_id).set(game_info)

    def get_all_game_id(self,season):
        game_db = self.database.child(season).child("Game_IDs").get()
        return list(game_db)

    def get_single_game(self,season,game_id):
        return self.database.child(season).child("Game_IDs").child(game_id).get()
    
    def add_game_to_team(self,season,game):
        set_game={
            "home_team": game["home_team"],
            "winner": game["winner"],
            "delta": game["delta"],
            "opp_id": game["opp_id"],
            "opp_alias": game["opp_alias"],
            "opp_name": game["opp_name"]
        }
        self.database.child(season).child("Teams").child(game["alias"]).child('id').set(game["id"])
        self.database.child(season).child("Teams").child(game["alias"]).child("Games").child(game["date"]).set(set_game)

    def delete_single_game(self,season,game_id):
        self.database.child(season).child(game_id).remove()

    def team_reorganize(self):
        team_list = self.database.child("2021").child("Teams").get()
        for team in team_list:
            key_list = list(team_list[team])
            team_list[team]["id"] = ""
            team_list[team]["Name"] = ""
            team_list[team]["School"] = ""
            team_list[team]["Conference"] = ""
            team_list[team]["RPI"] = 0
            team_list[team]["SOS"] = 0
            team_list[team]["Games"] = {}
            
            for key in key_list:
                team_list[team]["Games"][key] = team_list[team][key]
                team_list[team].pop(key)
        
        self.database.child("2021").child("Teams").delete()
        self.database.child("2021").child("Teams").set(team_list)


    def update_Rpi(self,rpi):
        dict1 = {d['id']: d for d in rpi}

        team_list = self.database.child("2021").child("Teams").get()

        for team in team_list:
            id_value = team_list[team]["id"]
            if id_value in dict1:
                self.database.child("2021").child("Teams").child(team).child("RPI").set(dict1[id_value]["rpi"])
                self.database.child("2021").child("Teams").child(team).child("SOS").set(dict1[id_value]["sos"])

        

            # missing_games = [item for item in game_id if item not in game_data]

