def checkio(expression):
     const = {'()','{}','[]'}
     brakets = [i for i in expression if i in '{[()]}']
     i = 0
     while True:
          try:
               if i > 0 and brakets[i-1] + brakets[i] in const:
                    brakets.pop(i)
                    brakets.pop(i-1)
                    i -= 2
               i += 1
          except IndexError:
               return not brakets

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
