import requests
from bs4 import BeautifulSoup as BS
import datetime
import time
import os

def download_file(url, folder_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        os.makedirs(os.path.dirname(folder_path), exist_ok=True)
        file_path = os.path.join(folder_path, os.path.basename(url))
        with open(file_path, 'wb') as f:
            f.write(response.content)

    except requests.exceptions.RequestException as e:
        print(f'Download failed: {e}')

def download_from_sitemap_index(sitemap_index_url: str):
    r = requests.get(sitemap_index_url)
    soup = BS(r.content, 'html5lib')
    sitemaps = [sitemap.find('loc').text for sitemap in soup.find_all('sitemap')]
    domain = sitemap_index_url.replace('https://', '').replace('http://', '').replace('www.', '')
    domain = domain.split('.')[0]
    now = datetime.datetime.today()
    folder = f'{domain}/{now.day}-{now.month}-{now.year}/'
    for url in sitemaps:
        download_file(url, folder)


def main():
    url = "https://nhathuoclongchau.com.vn/sitemap.xml"

    download_from_sitemap_index(url)


if __name__ == '__main__':
    main()