
def main():
    with open("Books/frankenstein.txt") as f:
        file_contents = f.read()

    words=total_words(file_contents)

    alphabets=total_alphabets(file_contents.lower())
    #print(alphabets)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print("")
    for alpha in alphabets:
        print(f"The {alpha} character was found {alphabets[alpha]} times")
    print("--- End report ---")

def total_words(text):
    words=text.split()
    return len(words)

def total_alphabets(text):
    count={
        'a':0,'b':0,'c':0,
        'd':0,'e':0,'f':0,
        'g':0,'h':0,'i':0,
        'j':0,'k':0,'l':0,
        'm':0,'n':0,'o':0,
        'p':0,'q':0,'r':0,
        's':0,'t':0,'u':0,
        'v':0,'w':0,'x':0,
        'y':0,'z':0
    }

    for a in text:
        for x in count:
            if a==x:
                #print(f"{a} is {x}")
                count[x]=count[x]+1

    return count


main()