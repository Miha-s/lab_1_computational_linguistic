import nltk
import re

from nltk.corpus import wordnet as wn

# Розв'язання полісемії, або вибір правильного значення слова на основі його контексту

def check_nltk_data(resource):
    try:
        nltk.data.find(resource)
        return True
    except LookupError:
        return False

if not check_nltk_data('corpora/wordnet'):
    nltk.download('wordnet')

if not check_nltk_data('corpora/omw-1.4'):
    nltk.download('omw-1.4')


def find_best_synset(word, context): 
    synsets = wn.synsets(word)
    
    best_synset = None
    max_matches = synsets[0]

    for synset in synsets:
        definition = synset.definition()
        examples = ' '.join(synset.examples())
        
        matches = sum(1 for context_word in context if context_word in definition or context_word in examples)

        if matches > max_matches:
            max_matches = matches
            best_synset = synset

    return best_synset


def main():
    sentence = input("Enter a sentence: ")

    cleaned_sentence = re.sub(r'[^\w\s]', '', sentence)  
    words = cleaned_sentence.split() 
    print(f"Words in the sentence: {words}")

    while True:
        word = input("Enter a word from the sentence: ")        

        if word in words:
          best_synset = find_best_synset(word, words)
          if not best_synset:
              print(f"Failed to find synset for word", word)
          else:
            print(f"Definition: {best_synset.definition()}")
            print(f"Examples: {best_synset.examples()}")

        else:
            print(f"'{word}' is not in the sentence. Please try again.")

if __name__ == "__main__":
    main()

# Path similarity
# context_word = "water"
# context_synsets = wn.synsets(context_word)

# best_synset = None
# best_similarity = 0

# for synset in synsets:
#     for context_synset in context_synsets:
#         similarity = synset.path_similarity(context_synset)
#         if similarity and similarity > best_similarity:
#             best_similarity = similarity
#             best_synset = synset

# if best_synset:
#     print(f"Best match: {best_synset.name()} - {best_synset.definition()} with similarity {best_similarity}")
# else:
#     print("No good match found.")