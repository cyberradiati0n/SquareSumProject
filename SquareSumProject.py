def sumSquares():
  num1 = 1
  sum1 = 0
  for x in range(100):
    sum1 = num1**2 + sum1
    num1 = num1 + 1
    #print(sum1)
  num2 = 0
  addent1 = 0
  for x in range(100):
    addent1 = addent1 + 1
    num2 = num2 + addent1
    #print(num2)
  sum2 = num2**2
  #print(sum2)
  sum3 = sum2 - sum1
  
  print("The difference between the sum of the squares and the squares of the sum is "+ str(sum3))


sumSquares()
