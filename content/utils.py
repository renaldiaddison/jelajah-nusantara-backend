from news.utils import extractFindAllData
from .place_links import category_data
from bs4 import BeautifulSoup
from requests import get
import random

def generateImageByCategory(content):
    url = ""

    for key, value in category_data.items():
        if key.lower() in content.lower():
            url = value
            break
    
    if url == "":
        random_item = random.choice(list(category_data.items()))
        url = random_item[1]

    return url

def getScrappingDataPlace(link):
    res = {}
    try:
        url = get(link)
        soup = BeautifulSoup(url.text, 'html.parser')
        content_container = soup.find('main', class_="mw-body")
        title = soup.find('span', class_="mw-page-title-main")
        content = content_container.findAll(lambda tag: tag.name == 'p' and not tag.attrs)
        image_url = content_container.find('img', class_="mw-file-element")
        content = "\n".join(extractFindAllData(content))

        # Handle title
        if(title):
            title = title.text
        else:
            title = soup.find('h1', class_="firstHeading mw-first-heading").text

        # Handle image
        # if(image_url):
        #     image_url = image_url.get('src')
        # else:
        #     image_url = ""
            
        image_url = generateImageByCategory(content)
        
        res = {
            "title": title,
            "content": content,
            "image_url" : image_url,
        }
    except Exception as error:
        print(error)
        res = {
            "message": "error!",
        }
    return res

def getScrappingDataFood(link):
    res = {}
    try:
        url = get(link)
        soup = BeautifulSoup(url.text, 'html.parser')
        content_container = soup.find('main', class_="mw-body")
        title = soup.find('span', class_="mw-page-title-main")
        content = content_container.findAll(lambda tag: tag.name == 'p' and not tag.attrs)
        image_url = content_container.find('img', class_="mw-file-element")
        content = "\n".join(extractFindAllData(content))

        # Handle title
        if(title):
            title = title.text
        else:
            title = soup.find('h1', class_="firstHeading mw-first-heading").text

        if(image_url):
            image_url = image_url.get('src')
            res = {
                "title": title,
                "content": content,
                "image_url" : image_url,
            }

    except Exception as error:
        print(error)
        res = {
            "message": "error!",
        }
    return res

def getScrappingDataCulture(link):
    res = {}
    try:
        url = get(link)
        soup = BeautifulSoup(url.text, 'html.parser')
        content_container = soup.find('main', class_="mw-body")
        title = soup.find('span', class_="mw-page-title-main")
        content = content_container.findAll(lambda tag: tag.name == 'p' and not tag.attrs)
        image_url = content_container.find('img', class_="mw-file-element")
        content = "\n".join(extractFindAllData(content))

        # Handle title
        if(title):
            title = title.text
        else:
            title = soup.find('h1', class_="firstHeading mw-first-heading").text

        if image_url and image_url.get('src'):
            res = {
                "title": title,
                "content": content,
                "image_url" : image_url.get('src'),
            }

    except Exception as error:
        print(error)
        res = {
            "message": "error!",
        }
    return res

def scrappingData(links, content_type):
    res = []
    for link in links:
        print(link)
        scrappingRes = {}
        if content_type == "Place":
            scrappingRes = getScrappingDataPlace(link)
        elif content_type == "Food":
            scrappingRes = getScrappingDataFood(link)
        elif content_type == "Culture":
            scrappingRes = getScrappingDataCulture(link)
        
        if scrappingRes != {}:
            res.append(scrappingRes)

    return res
