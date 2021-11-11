def transformation(line, n):
     if not n:
          return line
     like_one = ['I', 'X', 'C', 'M']
     like_five = ['V', 'L', 'D']
     trans_line = ''
     for c in line:
          if c in like_one:
               trans_line += like_one[like_one.index(c) + n]
          else:
               trans_line += like_five[like_five.index(c) + n]
     return trans_line

def checkio(data):
     rome_numbers = {'1':'I', '2':'II', '3':'III', '4':'IV', '5':'V',
                     '6':'VI', '7':'VII', '8':'VIII', '9':'IX'}
     data_rome = ''
     len_data = len(str(data))
     for i, c in enumerate(str(data)):
          try:
               data_rome += transformation(rome_numbers[c], len_data - i - 1)
          except KeyError:
               continue
     return data_rome

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
