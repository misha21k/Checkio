import math

def read_x_y(data):
     x_i = []
     y_i = []
     num = ''
     for char in data:
          if char in set('0123456789.-'):
               num += char
          elif num:
               if len(x_i) == len(y_i):
                    x_i.append(float(num))
               else:
                    y_i.append(float(num))
               num = ''
     return x_i, y_i

def round_math(num):
     if 0.5/100 - num % 0.01 < 0.00005:
          return math.ceil(num*100)/100
     else:
          return math.floor(num*100)/100

def print_equation(r_0, x_0, y_0):
     list_rezul = [str(round_math(num)).rstrip('0').rstrip('.').lstrip('-')
                   for num in (x_0, y_0, r_0)]
     sing = ['+' if num < 0 else '-' for num in (x_0, y_0)]
     return '(x{3}{0})^2+(y{4}{1})^2={2}^2'.format(*list_rezul, *sing)

def checkio(data):
     x_i, y_i = read_x_y(data)
     x_0 = sum(x_i)/3
     y_0 = sum(y_i)/3
     r_0 = 0
     i = -1
     while True:
          rezul = [r_0, x_0, y_0]
          r_i = [math.hypot(x_0-x_i[i], y_0-y_i[i]) for i in range(3)]
          r_0 = sum(r_i)/3
          i = (i + 1) if i < 2 else 0
          x_0 = x_i[i] + (x_0 - x_i[i])*r_0/r_i[i]
          y_0 = y_i[i] + (y_0 - y_i[i])*r_0/r_i[i]
          if abs(max(rezul[0]-r_0, rezul[1]-x_0,
                 rezul[2]-y_0, key=abs)) < 0.00001:
               break
     return print_equation(r_0, x_0, y_0)

print(checkio("(2,2),(6,2),(2,6)"))
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
