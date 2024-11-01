def single_root_words(root_word, *other_words):
    same_words = []
    count = 0
    rw = root_word.lower()
    list_ = list(other_words)
    while len(list_) > count:
        words = list_[count]
        nword = str(words).lower() #Пока я додумался до этого, я настолько преисполнился, что мне уже все ясно
        if rw in nword or nword in rw:
            same_words.append(words)
            count += 1
        else:
            count += 1
    else:
        return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)