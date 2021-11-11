def checkio(n, m):
     rezul = 0
     n, m = '{0:0>{1}}'.format(bin(n)[2:],max(len(bin(n)[2:]),len(bin(m)[2:]))),  \
     '{0:0>{1}}'.format(bin(m)[2:],max(len(bin(n)[2:]),len(bin(m)[2:])))
     for i in range(len(n)):
          if n[i] != m[i]:
               rezul += 1
     return rezul

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
