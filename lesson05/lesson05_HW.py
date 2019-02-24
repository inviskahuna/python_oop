class Word(object):

    def __init__(self, value, pos, text=False):
        self.value = value
        self.text = text
        self.part_of_speech = pos

    def __str__(self):
        return self.value


class Sentence(object):
    sentence = []
    words = []

    def __init__(self, *words):
        for word in words:
            self.words.append(word)
            self.sentence.append(word.value)

    def __str__(self):
        return " ".join(self.sentence)

    def show(self):
        self.__str__()

    @property
    def content(self):
        return [x for x in range(len(self.words))]

    @property
    def show_parts(self):
        return set([x.part_of_speech for x in self.words])


class AnotherSen(object):
    dog = Word("dog", "Noun")  # This is 0
    eat = Word("eat", "Verb")  # This is 1
    bone = Word("bone", "Noun")  # This is 2
    words = [dog, eat, bone]
    sen = []
    pos = []

    def __init__(self, word_list):
        self.word_list = word_list
        for i in self.word_list:
            self.sen.append(self.words[i])

    def __str__(self):
        str_out = []
        for i in self.sen:
            str_out.append(i.value)
        return " ".join(str_out)

    def show(self):
        self.__str__()

    @property
    def content(self):
        return self.word_list

    @property
    def show_parts(self):
        return set([x.part_of_speech for x in self.sen])


def main():
    dog = Word("dog", "Noun")
    eat = Word("eat", "Verb")
    bone = Word("bone", "Noun")

    s = Sentence(dog, eat, bone)
    print(s)
    print(s.content)
    print(s.show_parts)

    a = AnotherSen([0, 2])
    print(a)
    print(a.content)
    print(a.show_parts)


if __name__ == '__main__':
    main()
