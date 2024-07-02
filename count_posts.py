from glob import glob
from bs4 import BeautifulSoup as BS
from multiprocessing import Pool


def get_urls_from_sitemap(file):
    urls = []
    with open(file, 'r') as f:
        sitemap = f.read()
        soup = BS(sitemap, 'lxml')
        urls = [link.find('loc').text for link in soup.find_all('url')]
    return urls


def get_post_urls():
    files = glob(f'nhathuoclongchau/{date}/sitemap_baiviet*.xml')
    p = Pool(10)
    results = p.map(get_urls_from_sitemap, files)
    urls = []
    for sitemap in results:
        urls.extend([url for url in sitemap])

    urls = set(urls)
    return urls

def main():
    urls = get_post_urls()
    print(date, len(urls))

def check_post_num(date):
    files = glob(f'nhathuoclongchau/{date}/sitemap_baiviet*.xml')
    urls = []
    for file in files:
        with open(file, 'r') as f:
            sitemap = f.read()
            soup = BS(sitemap, 'lxml')
            urls.extend([link.find('loc').text for link in soup.find_all('url')])

    post_num = len(set(urls))
    print(date, post_num)


if __name__ == '__main__':
    # date = '25-4-2024'
    # # check_post_num(date)
    # main()
    previous_count = 0
    dates = [
        '1-5-2024',
        '2-5-2024',
        '3-5-2024',
        '4-5-2024',
        '5-5-2024',
        '6-5-2024',
        '7-5-2024',
        '8-5-2024',
        '9-5-2024',
        '10-5-2024',
        '11-5-2024',
        '12-5-2024',
        '13-5-2024',
        '14-5-2024',
        '15-5-2024',
        '16-5-2024',
        '17-5-2024',
        '18-5-2024',
        '19-5-2024',
        '20-5-2024',
        '21-5-2024',
        '22-5-2024',
        '23-5-2024',
        '24-5-2024',
        '25-5-2024',
        '26-5-2024',
        '27-5-2024',
        '28-5-2024',
        '29-5-2024',
        '30-5-2024',
        '31-5-2024',
        '1-6-2024',
        '2-6-2024',
        '3-6-2024',
        '4-6-2024',
        '5-6-2024',
        '6-6-2024',
        '7-6-2024',
        '8-6-2024',
        '9-6-2024',
        '10-6-2024',
        '11-6-2024',
        '12-6-2024',
        '13-6-2024',
        '14-6-2024',
        '15-6-2024',
        '16-6-2024',
        '17-6-2024',
        '18-6-2024',
        '19-6-2024',
        '20-6-2024',
        '21-6-2024',
        '22-6-2024',
        '23-6-2024',
        '24-6-2024',
        '25-6-2024',
        '26-6-2024',
    ]
    for date in dates:
        main()