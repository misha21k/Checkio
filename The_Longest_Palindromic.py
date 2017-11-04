import math

def form_line(index, text, flag):
     j = 1
     line = text[index]
     try:
          while text[index-j+1*flag] == text[index+j] and index-j+1*flag >= 0:
               line = (('' if j == 1 and flag else text[index-j+1*flag]) +
                          line + text[index+j])
               j += 1
     except IndexError:
          pass
     return line

def longest_palindromic(text):
     i = 0
     rezul = ''
     while i < len(text) - math.ceil(len(rezul)/2):
          line = max(form_line(i, text, True), form_line(i, text, False), key=len)
          if len(rezul) < len(line):
               rezul = line
          i += 1
     return rezul

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
