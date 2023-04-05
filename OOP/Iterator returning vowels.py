class VowelIterator:
    def __init__(self, word):
        self.word = word
        self.vowels = "aeiouy"

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        while self.index < len(self.word):
            char = self.word[self.index]
            self.index += 1
            if char.lower() in self.vowels:
                return char
        raise StopIteration


vowels = VowelIterator('The "Pro Python Course" is amazing! Thanks, Vlad!')
for vowel in vowels:
    print(vowel)
