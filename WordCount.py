class WordCount:
    def word_count(self, words):
        words = words.lower()
        word_dict = {}
        w = words.split()

        for word in w:
            if word not in word_dict:
                word_dict[word] = 1

            else:
                word_dict[word] += 1

        print(word_dict)



