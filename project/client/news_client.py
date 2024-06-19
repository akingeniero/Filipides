import logging

import requests
from bs4 import BeautifulSoup
from project.utils.singleton_meta import SingletonMeta

logger = logging.getLogger(__name__)


class NewsClient(metaclass=SingletonMeta):

    def __init__(self: 'NewsClient') -> None:
        """
        Initializes the TwitterClient with the necessary configurations and API client.

        Args:
            self: Instance of TwitterClient.

        Returns:
            None
        """
        logger.info("NewsClient initialized")

    async def extract_main_news(self: 'TwitterClient', url_data: str) -> str | None:
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
