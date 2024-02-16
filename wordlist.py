import os

def read_and_filter_words(filepath, max_length=7):
    words =set() 
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            for line in file:
                word = line.strip()
                if len(word) <= max_length:
                    words.add(word.lower())  # Add lowercase version to avoid duplicates
    return words

def generate_js_set(words, js_variable_name="wordSet"):
    js_array_content = ', '.join(f'"{word}"' for word in words)
    return f"const {js_variable_name} = new Set([{js_array_content}]);"

def main():
    directory = 'dict.txt'
    words = read_and_filter_words(directory)
    js_set = generate_js_set(words)
    print(js_set)

if __name__ == "__main__":
    main()
