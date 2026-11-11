def count_word(text, word):
    count = 0
    for w in text.split():
        if w == word:
            count += 1
    return count


print(count_word("apple Apple APPLE", "apple"))
