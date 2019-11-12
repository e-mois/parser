import sys
import requests
import re
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
    text = ""
    for p in p_list:
        a_list = p.find_all('a')
        for a in a_list:
            if a is not None:
                a_href = a.get('href')
                replace_a = f"[{a.text}]({a_href})"
                a.replaceWith(replace_a)
        text = f'{text} {p.text}'
    return text


def parser_article(url):
    try:
        html = get_html(url)
        data = get_data(html)
        ready_text = replace_link(data)
        return ready_text
    except Exception:
        return 'Error! Input correct url please'


if __name__ == '__main__':
    parser(sys.argv[1])
