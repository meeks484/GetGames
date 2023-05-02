import time
from Ncaamb import Ncaamb
from GameInfoDataBase import GameInfoDataBase
from BasketballGame import BasketballGame

api_key: str = 'gqf5crzbu46n8e99mduypnja'



ncaamb_ = Ncaamb.get_instance(api_key)
rpi = ncaamb_.getRpi("2021")




# game_id = ncaamb_.gameIdBySeason("2021")

# game_stats = ncaamb_.statsByGameId(game_id[1])

my_database = GameInfoDataBase.get_instance()

my_database.update_Rpi(rpi)
# game_data = my_database.get_all_game_id("2021")





# missing_games = [item for item in game_id if item not in game_data]

# for game in missing_games:
#     time.sleep(10)
#     game_stats = ncaamb_.statsByGameId(game)
#     my_database.push_game_info(game,"2021",game_stats)





# games = BasketballGame.get_instance()

# for game in game_data:
#     game_info = my_database.get_single_game(season="2021",game_id=game)
#     if game_info != "postponed":
#         home_team = games.getHomeTeam(game_data=game_info)
#         my_database.add_game_to_team("2021",home_team)
#         away_team = games.getAwayTeam(game_data=game_info)
#         my_database.add_game_to_team("2021",away_team)
    

