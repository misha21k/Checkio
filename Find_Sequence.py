def proverka(line):
     if line.count(None) <= len(line)-4:
          schet = 1
          for i in range(1, len(line)):
               if line[i] == line[i-1] and line[i] is not None:
                    schet += 1
               else:
                    schet = 1
               if schet == 4:
                    return True
     return False

def diagonal(matrix, flag):
     len_1 = len(matrix) - 1
     return [[None]*(i*flag+(len_1-i)*(not flag)) + list(line) +
             [None]*(i*(not flag)+(len_1-i)*flag) for i, line in enumerate(matrix)]
                         
def checkio(matrix):
     for line in matrix:
          if proverka(line):
               return True
     for line in zip(*matrix):
          if proverka(line):
               return True
     for line in zip(*diagonal(matrix, True)):
          if proverka(line):
               return True
     for line in zip(*diagonal(matrix, False)):
          if proverka(line):
               return True 
     return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
