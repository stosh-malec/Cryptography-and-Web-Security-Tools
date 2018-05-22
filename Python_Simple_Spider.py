import re
import urllib.request
from bs4 import BeautifulSoup


url = input('Please input a url to scrape')
recursion = input('Please enter a number of pages to recurse through')
html_queue = []
html_queue.append(url)
all_links = []
def Spider(html_queue, all_links, recursion):
    for x in range(0, int(recursion)):
        html = urllib.request.urlopen(html_queue[x])
        soup = BeautifulSoup(html)
        for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
            all_links.append(link.get('href'))
            if not link in html_queue:
                html_queue.append(link.get('href'))

Spider(html_queue, all_links, recursion)
print(all_links, " are on the page  ", url, "with a depth of ", recursion)
