import re
import codecs
from collections import Counter


class ProcessText(object):

    def __init__(self, text):
        self.text = text

    @property
    def split_by_sentences(self):
        pattern = re.compile(r'(?<=[.!?…]) ')
        s = pattern.split(self.text)
        ret = []
        for i in s:
            ret.append(re.sub("|\n|\r", '', i))
        return ret

    def find_freq_word(self, length):
        pattern = re.compile(r'([а-яА-Я]+)')
        c = Counter([word for word in pattern.findall(self.text) if len(word) >= length])
        ret = max(dict(c), key=c.get)
        return "Самое частое слово длинной не менее [{}] [{}], [{}] случая".format(length, ret, c[ret])

    @property
    def find_links(self):
        pattern = re.compile(r'(\w+.\w+\.[ru]+/?\w+\.?)')
        return pattern.findall(self.text)

    @property
    def find_freq_links_domain(self):
        pattern = re.compile(r'[\w]+.ru')
        c = Counter(pattern.findall(self.text))
        ret = max(dict(c), key=c.get)
        return "чаще всего используется домен [{}], [{}] случая".format(ret, c[ret])

    def decorate_links(self, decor):
        text = self.text
        for x in self.find_links:
            text = re.sub(x, decor, text)
        return text


def main():
    with codecs.open('text.txt', 'r', encoding='utf-8') as text:
        raw_text = text.read()

    p = ProcessText(raw_text)

    print(p.split_by_sentences)
    print(p.find_freq_word(4))
    print(p.find_links)
    print(p.find_freq_links_domain)
    print(p.decorate_links("[Ссылка отобразится после регистрации]"))


if __name__ == '__main__':
    main()
