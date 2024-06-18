import requests
from bs4 import BeautifulSoup


def extract_main_news(url):
    """
    Extracts the main news headline and content from a given URL.

    Args:
        url (str): The URL of the webpage containing the news.

    Returns:
        dict: A dictionary containing the main news headline and content.
              Keys: 'headline', 'content'
    """
    try:
        response = requests.get(url)
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

        return {'headline': headline, 'content': content}

    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud HTTP: {e}")
        return None
    except AttributeError:
        print("No se pudo encontrar el elemento deseado en la página")
        return None
