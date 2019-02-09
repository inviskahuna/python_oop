import re
import codecs

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

    def find_freq_word(self, length, lang, text):
        pass

    def find_links(self, text):
        pass

    def find_freq_links_domain(self, text):
        pass

    def decorate_links(self, text, replace):
        pass


def main():
    with codecs.open('text.txt', 'r', encoding='utf-8') as text:
        raw_text = text.read()

    p = ProcessText(raw_text)

    print(p.split_by_sentences)

if __name__ == '__main__':
    main()
