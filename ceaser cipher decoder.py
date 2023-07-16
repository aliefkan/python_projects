#to decoding messages written in ceaser cipher
import string
def reversing_sentence(sentence):
    return sentence[::-1]
def ceaser_cipher(sentence):
    alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    new_sentence = []
    punctuations = string.punctuation
    shift_amount = 0
    for j in range(26):
        shift_amount += 1
        new_sentence.append('\n')
        for i in sentence.upper():
            if i == ' ':
                new_sentence.append(' ')
            elif i in punctuations:
                new_sentence.append(i)
            else:
                index_of_char = alphabets.index(i)
                shifted_index = index_of_char + shift_amount
                shifted = alphabets[shifted_index % len(alphabets)]
                new_sentence.append(shifted)
    sentence_as_string = ''.join(new_sentence)
    return sentence_as_string
if __name__ == '__main__':
    sentence = input('Enter the sentence you want to encode or decode: ')
    reversed_sentence = reversing_sentence(sentence)
    print(ceaser_cipher(reversed_sentence))


