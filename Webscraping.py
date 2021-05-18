# importing the required modules

from bs4 import BeautifulSoup                       # for web scrapping
from urllib.request import urlopen                  # for fetching url's
import wikipedia                                    # For accessing content from Wikipedia
import os
import json                                         # For handling json returns
import random

def get_content(text):


    # get content from Wikipedia

    text_to_fetch = text
    Wiki_content = wikipedia.page(text_to_fetch).summary
    file = open(f'{text_to_fetch}_Wiki.txt', 'w+')
    file.write('Content from Wikipedia\n\n')
    file.writelines(Wiki_content)
    file.close()
    # os.startfile(text_to_fetch+"_Wiki.txt")


    # get content from Javatpoint

    URL = 'https://www.javatpoint.com/binary-tree'
    page = urlopen(URL)
    soup = BeautifulSoup(page.read().decode('UTF-8'), 'html.parser')
    text = soup(['p', 'h3'])
    file = open(text_to_fetch+"_Javat.txt", 'w+', encoding="utf-8")
    file.write('Content from Javatpoint\n\n')
    for data in text[:44]:
        file.write(data.text)
        file.write('\n\n')
    file.close()
    # os.startfile(text_to_fetch+"_Javat.txt")


    # get content from TutorialsPoint

    URL = 'https://www.tutorialspoint.com/data_structures_algorithms/tree_data_structure.htm'
    page = urlopen(URL)
    soup = BeautifulSoup(page.read().decode('UTF-8'), 'html.parser')
    text = soup(['p', 'pre', 'h2', 'h3'])
    file = open(text_to_fetch+"_TutorialsPoint.txt", 'w+', encoding="utf-8")
    file.write('Content from TutorialsPoint\n\n')
    for data in text[:-2]:
        file.write(data.text)
        file.write('\n\n')
    file.close()
    # os.startfile(text_to_fetch+"_TutorialsPoint.txt")

    return


# get content from Wikipedia

def get_content_from_Wikipedia(Content_to_be_fetched):
    Wiki_content = wikipedia.page(Content_to_be_fetched).content
    results = wikipedia.summary(Content_to_be_fetched, sentences = 3)
    results_url = wikipedia.page(Content_to_be_fetched).url
    file = open(f'{Content_to_be_fetched}_Wiki.txt', 'w+', encoding="utf-8")
    file.write(f'Content regarding {Content_to_be_fetched} from Wikipedia\n\n')
    file.writelines(Wiki_content)
    file.write(f'\n\n\nFor more clearer information, you can visit - {results_url}')
    file.close()
    # os.startfile(Content_to_be_fetched+"_Wiki.txt")
    return results


# get jokes from the site icnb.com

def get_randomjoke():
    URL = 'https://api.icndb.com/jokes/random?exclude=[explicit]'
    joke = urlopen(URL)
    joke = json.load(joke)
    return joke['value']['joke']


# get jokes not related to ChuckNorris from the site icnb.com

def get_randomjoke_withoutChuckNorris():
    names = ["John Doe", "bruce schneier"]
    name = names[random.randint(0, 1)]
    URL = f'http://api.icndb.com/jokes/random?firstName={name[0]}&lastName={name[1]}'
    joke = urlopen(URL)
    joke = json.load(joke)
    return joke['value']['joke']
