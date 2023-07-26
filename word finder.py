def word_finder(length, letters, joker1='', joker2='', joker3=''):
    words_found = []
    if length <= 0:
        return "Invalid length"
    elif type(length) != int:
        return "Invalid length"
    elif joker1.isalpha() is False and joker1 != '':
        return "Invalid input for joker letter."
    elif joker2.isalpha() is False and joker2 != '':
        return "Invalid input for joker letter."
    elif joker3.isalpha() is False and joker3 != '':
        return "Invalid input for joker letter."
    else:
        with open("word_list.txt", "r") as word_list:
            for words in word_list:
                for word in words.split():
                    if len(word) <= length:
                        if str(letters) in word:
                            if joker1 != '':
                                if joker1 in word:
                                    words_found.append(word)
                            elif joker2 != '':
                                if joker2 in word:
                                    words_found.append(word)
                            elif joker3 != '':
                                if joker3 in word:
                                    words_found.append(word)
    return print(words_found)
word_finder(int, str, str, str)