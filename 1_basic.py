import nltk
from nltk.tokenize import sent_tokenize, word_tokenize


# the sent tokenize simply splits up the line at fullstop (.) , then later onward you can bring up the regular expression to split by periods

def tokenize_sentence(sentences):
    sentences = str(sentences).strip()
    tokenized_sentences = sent_tokenize(sentences)
    return tokenized_sentences




if __name__ == '__main__':
    sentence = input() # taking the input from the user
    # nltk.download()  # this is used to download the natural language processing library
    td = tokenize_sentence(sentence)  # Tokenizing the sentence
    print(td)

    ''' Keep in mind below is the word tokenization, since the Punctuation is treated even seperate , we can also use to handle stop words.
     As:
    '''
    tw = word_tokenize(sentence)  # Tokenizing the sentence with respect  to all the words.
    print(tw)
    # Notice that the pucjtuation is treated as a seperate token as :
