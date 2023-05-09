from bs4 import BeautifulSoup as Bs
from fake_useragent import UserAgent
import requests

url = "https://fobook.ru"

ua = UserAgent()
headers = {'accept': '*/*', 'user-agent': ua.firefox}
page = 1
authors = []
story_names = []


while True:
    response = requests.get(url, headers)
    html = Bs(response.content, "html.parser")
    items = html.select("#content")
    page_title = html.select(".page-title")

    if page <= 22:
        for el in html.select("#content"):
            author = el.select(".author")
            story_name = el.select("#content>article > h2 > a")
            for i in author:
                authors.append(i.text)
            for i in story_name:
                story_names.append(*i.contents)


    else:
        break

    page += 1
    url = f"https://fobook.ru/page{page}"


with open("search_res.txt", "w") as file:
    for i in range(len(authors)):
        file.write(str(authors[i]) + " - " + str(story_names[i]) + "\n")
        file.write("")
