AI = open("AI.txt", "r")
word_count = 0
word_dict = {}
special_characters = '"', '"', ",", ".", "-", "'", "@", "!"
for word in AI:
    for w in word.split():
        w = w.lower()
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1

word_dict[w] = float(word_count)

# print(word.split())
print(word_dict)
