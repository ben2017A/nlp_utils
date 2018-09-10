
import re
import nltk.data

def sent_tokenize(text):


    """Split text into sentences."""

    # TODO: Split text by sentence delimiters (remove delimiters)
    sentences = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)

    # TODO: Remove leading and trailing spaces from each sentence
    for sent in sentences:
        sent.strip()

    return sentences

    pass  # TODO: Return a list of sentences (remove blank strings)

def sent_tokenize_2(text):
    #tokenizer = nltk.data.load()
    return nltk.sent_tokenize(text)

def word_tokenize(sent):
    """Split a sentence into words."""

    # TODO: Split sent by word delimiters (remove delimiters)
    words = re.split(' ', sent)

    # TODO: Remove leading and trailing spaces from each word
    for word in words:
        word.strip()

    return words

    pass  # TODO: Return a list of words (remove blank strings)


def word_sentence_tokenize_test():
    text = "The first time you see The Second Renaissance it may look boring. Look at it at least twice and definitely watch part 2. It will change your view of the matrix. Are the human people the ones who started the war? Is AI a bad thing?"
    print("--- Sample text ---", text, sep="\n")

    sentences = sent_tokenize_2(text)
    print("\n -- Sentences -- ")
    print(sentences)

    print("\n -- Words -- ")
    for sent in sentences:
        print(sent)
        print(word_tokenize(sent))
        print()




def counter_words(text):
    counts = dict()

    text = text.lower()
    words = text.strip().split(' ')

    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    return counts

def test_run():
    with open('./test_data/input.txt', 'r') as f:
        text = f.read()
        counts = counter_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

        print("10 most common words: \n Word \t Count")
        for word, count in sorted_counts[:10]:
            print("{} \t {}".format(word, count))

        print("10 least common words: \n Word, \t Count")
        for word, count in sorted_counts[-10:]:
            print("{} \t {}".format(word, count))

if __name__ == "__main__":
    #test_run()
    word_sentence_tokenize_test()