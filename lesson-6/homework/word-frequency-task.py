import string
from collections import Counter

def clean_and_split(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words

def get_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"{file_name} not found.")
        content = input("Please enter a paragraph of text to create the file: ")
        with open(file_name, 'w') as file:
            file.write(content)
    return content

def count_word_frequency(words):
    word_count = Counter(words)
    return word_count

def generate_report(total_words, top_words, report_file):
    with open(report_file, 'w') as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write(f"Top 5 Words:\n")
        for word, count in top_words:
            file.write(f"{word} - {count}\n")

def word_frequency_counter(file_name, top_n=5):
    content = get_file_content(file_name)
    words = clean_and_split(content)
    word_count = count_word_frequency(words)
    total_words = len(words)
    top_words = word_count.most_common(top_n)
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_words:
        print(f"{word} - {count} {'times' if count > 1 else 'time'}")
    report_file = "word_count_report.txt"
    generate_report(total_words, top_words, report_file)
    print(f"\nThe word count report has been saved to {report_file}")


file_name = "words.txt"
top_n = int(input("Enter the number of top common words to display: "))
word_frequency_counter(file_name, top_n)
