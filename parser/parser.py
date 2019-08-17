import sys
import re
import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url).text
    return r


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    article_list = soup.find('body').find_all('p')
    new_article_list = []
    pattern = re.compile(r'\w')
    for p in article_list:
        if re.findall(pattern, p.text):
            new_article_list.append(p)

    return new_article_list


def replace_link(p_list):
    for p in p_list:
        a_text = p.find('a')
        if a_text is None:
            print(p.text)
        else:
            a_text_href = a_text.get('href')
            replace_a = '[' + a_text.text + '] (' + a_text_href + ')'
            a_text.replaceWith(replace_a)
            print(p.text)


def parser(url):
    #replace_link(get_data(get_html(url)))
    try:
        return replace_link(get_data(get_html(url)))
    except Exception:
        print('Error! Input correct url please')


if __name__ == '__parser__':
    parser(sys.argv[1])
