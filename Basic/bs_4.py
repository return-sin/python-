from bs4 import BeautifulSoup
import requests

# page = requests.get('https://www.baidu.com')
# # print(page.content)
# soup = BeautifulSoup(page.content, 'html.parser')
# # print(soup.prettify())
# title = soup.find("a")
# print(title)
# print(title.get_text()) # type:ignore

# poem_text = soup.find_all("a")
# for text in poem_text:
#       print( text.get_text( ) )


# page = requests.get('https://github.com/Connor-SM')
# soup = BeautifulSoup(page.content, 'html.parser')
# # print(soup.prettify())
# # username = soup.find("span", class_="p-nickname vcard-username d-block")
# # print(username.get_text())
# username = soup.find("span", attrs={"class":"p-nickname vcard-username d-block"})
# print(username)
# print(username.get_text())


page = requests.get('http://www.arthurleej.com/e-love.html')
soup = BeautifulSoup(page.content, 'html.parser')
html = list(soup.children)[2]
for section in html: # type:ignore
    print('\n\n Start of new section')
    print(section)
