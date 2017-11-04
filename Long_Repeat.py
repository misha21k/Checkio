def long_repeat(line):
     string = ''
     length = set()
     for char in line:
          if char in string or not string:
               string += char
          else:
               length.add(len(string))
               string = char
     length.add(len(string))
     return max(length)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
