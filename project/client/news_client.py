import logging

import requests
from bs4 import BeautifulSoup
from project.utils.singleton_meta import SingletonMeta

logger = logging.getLogger(__name__)


class NewsClient(metaclass=SingletonMeta):
    """
    Client to interact with news websites and extract main news content.
    """

    def __init__(self) -> None:
        """
        Initializes the NewsClient with the necessary configurations.
        """
        logger.info("NewsClient initialized")

    async def extract_main_news(self, url_data: str) -> str | None:
        """
        Extracts the main news headline and content from the given URL.

        Args:
            self: Instance of NewsClient.
            url_data (str): URL of the news article to extract content from.

        Returns:
            str | None: Formatted string containing the headline and content of the news article,
                        or None if an error occurs.
        """
        try:
            response = requests.get(url_data)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            headline = soup.find('h1').text.strip()

            content = ""

            content_div = soup.find('div', class_='a_c', attrs={'data-dtm-region': 'articulo_cuerpo'})
            if content_div:
                content = content_div.text.strip()

            if not content:
                content_paragraph = soup.find('p', class_='ue-c-article__paragraph',
                                              attrs={'data-mrf-recirculation': 'Links Párrafos'})
                if content_paragraph:
                    content = content_paragraph.text.strip()

            if not content:
                content_body = soup.find('div', class_='article-body__content')
                if content_body:
                    paragraphs = content_body.find_all('p')
                    content = ' '.join([p.text.strip() for p in paragraphs])

            if not content:
                ue_l_article_body = soup.find('div', class_='ue-l-article__body')
                if ue_l_article_body:
                    paragraphs = ue_l_article_body.find_all('p')
                    content = ' '.join([p.text.strip() for p in paragraphs])

            return f"Titulo: {headline} Contenido: {content}"

        except requests.exceptions.RequestException as e:
            logger.info(f"Error al hacer la solicitud HTTP: {e}")
            return None
        except AttributeError:
            logger.info("No se pudo encontrar el elemento deseado en la página")
            return None
