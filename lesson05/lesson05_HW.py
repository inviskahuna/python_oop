part_of_speech = {
    "Noun": 0,
    "Adjective": 1,
    "Pronoun": 2,
    "Numeral": 3,
    "Verb": 4
}


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


def main():
    dog = Word("dog", "Noun")
    eat = Word("eat", "Verb")
    bone = Word("bone", "Noun")

    s = Sentence(dog, eat, bone)
    print(s)
    print(s.content)
    print(s.show_parts)


if __name__ == '__main__':
    main()
