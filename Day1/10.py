from bs4 import BeautifulSoup
import requests
from IPython import embed
import time

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64"}

time.sleep(2)

BASE_URL ="https://albertyumol.github.io/"

def extract_html_content(target_url):
    response = requests.get(target_url, headers)
    return response.text

def main():
    target_page = BASE_URL + "index.html"

    html_content = extract_html_content(target_page)
    print(html_content)

if __name__=="__main__":
    main()