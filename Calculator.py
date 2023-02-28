while True: 
  action = input('Введите действие ("+" - сложение, "-" - вычитание, "*" - умножение, "/" - деление): ')
  if action in '+-/*':
    break
  print('Такого действия не существует')
num1 = int(input('Введи первое число: '))
num2 = int(input('Введи второе число: '))  
  
result = 0
  
if action == '+':
  result = num1 + num2

elif action == '-':
  result = num1 - num2
    
elif action == '*':
  result = num1 * num2    

elif action == '/':
  result = num1 / num2    
  
print(num1, action, num2, '=', int(result) )
		

 
