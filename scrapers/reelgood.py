from common.trailer_scraper import TrailerScraper

reel_good_url = 'https://reelgood.com/show/trailer-park-boys-2001/season/'
output_file_name = './output/reel_good_data.json'


class ReelGoodScraper(TrailerScraper):
    def __init__(self):
        super().__init__(reel_good_url, output_file_name)

    def build_episodes(self, season_number: int, html):
        episodes = []
        episode_container_selector = '.css-nlmi7p'
        for i, episode_html in enumerate(html.select(episode_container_selector)):
            episode_number = i + 1
            air_date = episode_html.select('.css-qq8i26 i')[0].text.strip()
            title = episode_html.select('.css-qq8i26 b')[0].text.strip()
            description = episode_html.select('.css-qq8i26')[0].text.strip()
            image = episode_html.select('.css-kj3ttl picture img')[
                0].attrs.get('src', None)

            episode = {
                "season": season_number,
                "episode_number": int(episode_number),
                "title": title,
                "description": description,
                "air_date": air_date,
                "image": image
            }
            episodes.append(episode)

        return episodes
