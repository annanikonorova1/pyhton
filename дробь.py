import math
from fractions import Fraction
num_1,num_2=map(int,input('Введите первую дробь:num_1/num_2:').split('/'))
num_3,num_4=map (int,input('Введите вторую дробь:num_3/num_4:').split('/'))
num_5=num_1/num_2
num_6=num_3/num_4
res_1=(num_5)+(num_6)
print(round(res_1,2))
res_2=(num_5)*(num_6)
print(round(res_2,2))
firstfraction = Fraction(num_1, num_2)
secondfraction = Fraction(num_3, num_4)
res_3 = firstfraction + secondfraction
res_4 = firstfraction * secondfraction
print(round(res_3,2))
print(round(res_4,2))