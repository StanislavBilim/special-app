while True:
  operation = input('Введите операцию: ')
  if operation in ('+-*/'):
    break
  print('Такой операции не существует')
  
if operation == '-':

  N = int(input('Сколько операндов? '))
  string = ""
  for x in range(1, N + 1):
    n = int(input('Введите операнд ' + str(x) + ': '))
    if x == 1:
      res = n
    elif x != 1:
      res -= n
    if x == N:
      string += str(n)
      break
    string += str(n) + ' - '
elif operation == '+':
  N = int(input('Сколько операндов? '))
  string = ""
  for x in range(1, N + 1):
    n = int(input('Введите операнд ' + str(x) + ': '))
    if x == 1:
      res = n
    elif x != 1:
      res += n
    if x == N:
      string += str(n)
      break
    string += str(n) + ' + '
elif operation == '*':
  N = int(input('Сколько операндов? '))
  string = ""
  for x in range(1, N + 1):
    n = int(input('Введите операнд ' + str(x) + ': '))
    if x == 1:
      res = n
    elif x != 1:
      res *= n
    if x == N:
      string += str(n)
      break
    string += str(n) + ' * '
elif operation == '/':
  N = int(input('Сколько операндов? '))
  string = ""
  for x in range(1, N + 1):
    n = int(input('Введите операнд ' + str(x) + ': '))
    if x == 1:
      res = n
    elif x != 1:
      res /= n
    if x == N:
      string += str(n)
      break
    string += str(n) + ' / '

print('\n', string, '=', int(res))
		

 
