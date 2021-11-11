def checkio(data):
     bool = [False,False,False]
     for char in data:
          if '0' <= char <= '9':
               bool[0] = True
          elif 'a' <= char <= 'z':
               bool[1] = True
          elif 'A' <= char <= 'Z':
               bool[2] = True
          else:
               bool[0] = False
               break
     if len(data) >= 10 and bool == [True,True,True]:
          return True
     else:
          return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
