from bs4 import BeautifulSoup
import requests

season_url = 'https://www.imdb.com/title/tt0290988/episodes?season='


def get_episodes(season_number):
    url = '{}{}'.format(season_url, season_number)
    episodes = []

    print('Processing Season {}'.format(season_number))

    try:
        response = requests.get(url)
        raw_html = response.text
        html = BeautifulSoup(raw_html, 'html.parser')
    except requests.exceptions.RequestException as err:
        print('Error during requests to {0} : {1}'.format(url, str(err)))
        return None
    finally:
        for _, episode_html in enumerate(html.select('.list_item .info')):
            episode_number = episode_html.select(
                'meta')[0].attrs.get('content', None)
            air_date = episode_html.select('.airdate')[0].text.strip()
            title = episode_html.select('strong a')[0].attrs.get('title', None)
            description = episode_html.select(
                '.item_description')[0].text.strip()
            rating = episode_html.select(
                '.ipl-rating-star__rating')[0].text.strip()

            episode = {
                "season": int(season_number),
                "episode_number": int(episode_number),
                "title": title,
                "description": description,
                "air_date": air_date,
                "rating": rating
            }

            episodes.append(episode)

        return episodes


def get_seasons():
    seasons = {'seasons': []}
    number_of_seasons = 12

    for season_number in range(1, number_of_seasons + 1):
        season = {'season': season_number, 'episodes': []}
        season['episodes'] = get_episodes(season_number)
        seasons['seasons'].append(season)

    return seasons
