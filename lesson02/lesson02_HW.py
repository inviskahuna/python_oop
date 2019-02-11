from requests import get
from bs4 import BeautifulSoup as Bs
import re


class PupilsCounter(object):
    def __init__(self, link):
        self.page = get(link)

    @property
    def get_pupils_with_re(self):
        pattern = re.compile('<span class="total-users">Нас уже\s+(\d+\s+\d+\s+\d+)\s+человек<\/span>')
        string = pattern.findall(self.page.text)
        ret = re.sub("\s+", "", *string)
        return int(ret)

    @property
    def get_pupils_with_soup(self):
        soup = Bs(self.page.text, 'html.parser')
        s = soup.find(class_="total-users").text
        int_list = [str(s) for s in s if s.isdigit()]
        return int("".join(int_list))


def main():
    p = PupilsCounter("https://geekbrains.ru")
    print("Определили с RE что учеников {}".format(p.get_pupils_with_re))
    print("Определили с BS что учеников {}".format(p.get_pupils_with_soup))


if __name__ == '__main__':
    main()
