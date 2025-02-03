import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from bs4.element import Comment
from IPython.display import clear_output

while input('Would you like to analyze a website? (y/n): ') == 'y':
    try:
        clear_output()
        site = input('Enter the website you would like to analyze: ')
        print(site)
    except:
        print('Something went wrong. Please try again.')
print('Thank you for analyzing the website! Come back again!')

def scrape(site):
    page = requests.get(site)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.find_all(text=True)
    print(text)

def filterTags(element):
    if element.parent.name in ["style", "script", "head", "title", "meta", "[document]" ]:
        return False
    if isinstance(element, Comment):
        return False
    return True
    text = soup.find_all(text=True)
    visible_text = filter(filterTags, text)
    for text in visible_text:
        for word in words:
            if word !='':
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    print(word_count[:7])

def filterWaste(word):
    bad_words = ("the", "a", "in", "of", "to", "you", "\xa0", "and", "at", "on", "for", "from", "is", "that", "his","are", "be", "-", "as", "&", "they", "with", "how", "was", "her", "him", "i", "has", "|")
    if word.lower() in bad_words:
        return False
    else:
        return True
    
    for text in visible_text:
        words = text.replace('\n', '').replace('\t', '').split(' ')
        words = list(filter(filterWaste, words))
        for word in words:
            print(word, end=' ')

