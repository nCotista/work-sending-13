n = float(input('Weight(kg) :'))
b= float(input('Height(M) :'))
y = b*b
x = n/y
print('BMIis','%.1f'%(x))
if(x<18.5):
   print('Underweight ')
elif(x<25):
   print('Normal Weight')
elif(x<30):
   print('Overweight')
else:
   print('Obesity')