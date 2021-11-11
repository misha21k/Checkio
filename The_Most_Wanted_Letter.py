def checkio(text):
     schet = []
     maximum = 0
     for i in range(0,26):
          schet.append(0)
     for char in text.lower():
          if 'a' <= char <= 'z':
               schet[ord(char)-ord('a')] += 1
               if schet[ord(char)-ord('a')] > maximum:
                    maximum = schet[ord(char)-ord('a')]
     for i in range(0,26):
          if schet[i] == maximum:
               return chr(i+ord('a'))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
