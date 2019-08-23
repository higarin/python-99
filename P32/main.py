def gcd(num1,num2):
    while num2 != 0:
      num1,num2 = num2,num1%num2
     ###上記分からなかったので、使い方覚えるようにする###
    return num1

#gcd(36,63)
#63 36
#36 27
#27 9
#9 0
