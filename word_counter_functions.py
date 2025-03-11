def count_words(sentence):
    words = sentence.split()
    return len(words)

def main():
    sentence = input("Enter a sentence: ")
    
    word_count = count_words(sentence)
    print(f"The sentence has {word_count} words.")

main()
