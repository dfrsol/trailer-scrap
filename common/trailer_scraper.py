from bs4 import BeautifulSoup
import abc
import requests


class TrailerScraper(metaclass=abc.ABCMeta):
    def __init__(self, url: str, output_file_name: str):
        self.number_of_seasons = 12
        self.seasons = {'seasons': []}
        self.url = url
        self.output_file_name = output_file_name

    def get_seasons(self):
        for season_number in range(1, self.number_of_seasons + 1):
            season = {'season': season_number, 'episodes': []}
            season['episodes'] = self.get_episodes(season_number)
            self.seasons['seasons'].append(season)

        return self.seasons

    def get_episodes(self, season_number: int):
        url = '{}{}'.format(self.url, season_number)
        print('Processing Season {}'.format(season_number))

        try:
            response = requests.get(url)
            raw_html = response.text
            html = BeautifulSoup(raw_html, 'html.parser')
        except requests.exceptions.RequestException as err:
            print('Error during requests to {0} : {1}'.format(url, str(err)))
            return None
        finally:
            return self.build_episodes(int(season_number), html)

    @abc.abstractmethod
    def build_episodes(self, season_number: int, html):
        raise NotImplementedError
