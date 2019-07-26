import urllib.request
from bs4 import BeautifulSoup
import re

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, features="lxml")
    table = soup.find('tbody')

    projects = []

    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')

        projects.append({
            'profile': cols[0].a['href'],
            'firstname': cols[0].a.text,
            'secondname': cols[1].a.text,
            'nickname': cols[2].a.text,
            'height': re.sub(r'\s+', '', cols[3].text),
            'weight': re.sub(r'\s+', '', cols[4].text),
            'reach': re.sub(r'\s+', '', cols[5].text),
            'stance': re.sub(r'\s+', '', cols[6].text),
            'wins': re.sub(r'\s+', '', cols[7].text),
            'lost': re.sub(r'\s+', '', cols[8].text),
            'draw': re.sub(r'\s+', '', cols[9].text)
        })

    for project in projects:
        print(project)

def main():
    parse(get_html('http://ufcstats.com/statistics/fighters?char=a&page=all'))

if __name__ == "__main__":
    main()
