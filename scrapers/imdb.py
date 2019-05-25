from common.trailer_scraper import TrailerScraper

imdb_url = 'https://www.imdb.com/title/tt0290988/episodes?season='
output_file_name = './output/imdb_data.json'


class IMDBScraper(TrailerScraper):
    def __init__(self):
        super().__init__(imdb_url, output_file_name)

    def build_episodes(self, season_number: int, html):
        episodes = []
        episode_container_selector = '.list_item .info'
        for _, episode_html in enumerate(html.select(episode_container_selector)):
            episode_number = episode_html.select(
                'meta')[0].attrs.get('content', None)
            air_date = episode_html.select('.airdate')[0].text.strip()
            title = episode_html.select('strong a')[0].attrs.get('title', None)
            description = episode_html.select(
                '.item_description')[0].text.strip()
            rating = episode_html.select(
                '.ipl-rating-star__rating')[0].text.strip()

            episode = {
                "season": season_number,
                "episode_number": int(episode_number),
                "title": title,
                "description": description,
                "air_date": air_date,
                "rating": rating
            }
            episodes.append(episode)

        return episodes
