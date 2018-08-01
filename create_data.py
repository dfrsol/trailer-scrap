import json
import os
from imdb import seasons


file_name = './output/imdb_data.json'
os.makedirs(os.path.dirname(file_name), exist_ok=True)

with open(file_name, 'w') as open_file:
    json.dump(seasons.get_seasons(), open_file)
