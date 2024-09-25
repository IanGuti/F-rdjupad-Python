import logging
import pandas as pd
from test_api import API
from test_save_data import DataSaver

log = logging.getLogger(__name__)

# Configurate loggmessages
logging.basicConfig(
    filename = "test_api_fetcher.log",
    format = "[%(asctime)s][%(name)s][%(levelname)s] %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    level = logging.INFO
    )

# URL, ID and key for APIn
api_key = '0C4939C37DDAD8979D4152E4948DC3ED'
steam_id = '76561198014480911'

# Check that the API key is the correct length and check that the Steam-ID is correct length and only digits
if len(api_key) == 32:
    if len(steam_id) == 17:
        if steam_id.isdigit():
            
            url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={api_key}&steamid={steam_id}&include_appinfo=true&include_played_free_games=true"
            
            # Call the API-script and fetch data
            api_instance = API(url)
            api_data = api_instance.fetch_data()
            api_del = api_data["response"]["games"]

            # Remove the columns that are not needed
            for dictionary in api_del:
                remove_keys = list(dictionary.keys())[3:14]
                for key in remove_keys:
                    del dictionary[key]

            # Save the data in a database
            df = pd.DataFrame(api_del)
            save_sql = DataSaver(df)
            save_sql.save()
        else:
            log.warning("Steam-ID is not only numbers.")
            raise Exception("The Steam-ID you have enterd need to be only digits.")
            
    else:
        log.warning("Wrong length on steam-id")
        raise Exception("The Steam-ID you have entered needs to be 17 digits long.")
        
else:
    log.warning("Wrong length on API-key.")
    raise Exception("Your API-key has to have 32 characters.")
