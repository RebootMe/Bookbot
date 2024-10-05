
def main():
    with open("Books/frankenstein.txt") as f:
        file_contents = f.read()

    k=total_words(file_contents)
    print(k)


def total_words(text):
    words=text.split()
    return len(words)

main()