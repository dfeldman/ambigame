import os
import re
import random
from collections import defaultdict, Counter

def read_words(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip().lower()

def filter_words(words, min_length=3, max_length=7):
    filtered = []
    for word in words:
        if min_length <= len(word) <= max_length and not re.search(r'(s|ing|ed|er|ly|es)$', word):
            filtered.append(word)
    return filtered

def get_random_words(words, length):
    same_length_words = [word for word in words if len(word) == length]
    if len(same_length_words) < 2:
        return None, None
    return random.sample(same_length_words, 2)

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u']

def update_histogram(histogram, word1, word2):
    for c1, c2 in zip(word1, word2):
        if not (is_vowel(c1) and is_vowel(c2)):
            histogram[f'{c1}/{c2}'] += 1

def process(directory, iterations=10000):
    histogram = Counter()
    all_words = []

    # Read and filter words from dictionary files
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            words = list(read_words(file_path))
            all_words.extend(filter_words(words))

    # Update histogram based on random word pairs
    for _ in range(iterations):
        length = random.randint(3, 6)
        word1, word2 = get_random_words(all_words, length)
        if word1 and word2:
#            print(word1, " ", word2)
            update_histogram(histogram, word1, word2)

    # Return the top 100 most used tiles
    return histogram.most_common(100)

def main():
    directory = '/usr/share/dict'
    top_tiles = process(directory)
    
    # Format the output as a JavaScript object
    print("const frequencies = {")
    for tile, count in top_tiles:
        print(f'    "{tile}": {count},')
    print("};")

if __name__ == "__main__":
    main()

