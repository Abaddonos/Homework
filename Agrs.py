def single_root_words(root_word, *other_words):
    same_words = []
    while len(other_words) > 0:
        #other_words = str(other_words.lower)
        root_word = str(root_word.lower)
        for i in root_word:
            for j in other_words:
                if i in j:
                    same_words.append(j)
                    continue
                else:
                    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)