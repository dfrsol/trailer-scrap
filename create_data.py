import json
import os
from common.trailer_scraper import TrailerScraper
from scrapers.reelgood import ReelGoodScraper
from scrapers.imdb import IMDBScraper

imdb = IMDBScraper()
reel_good = ReelGoodScraper()
scrapers = [imdb, reel_good]


def get_seasons_from_all_sources():
    for s in scrapers:
        get_seasons_from_single_source(s)


def get_seasons_from_single_source(scraper: TrailerScraper):
    os.makedirs(os.path.dirname(scraper.output_file_name), exist_ok=True)

    with open(scraper.output_file_name, 'w') as open_file:
        json.dump(scraper.get_seasons(), open_file)
        print('Processing complete, data was written to {}'.format(
            scraper.output_file_name))


get_seasons_from_all_sources()
