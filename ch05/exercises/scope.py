def multiply(num,num2):
  result = 0
  for i in range(num):
    result= result + num2
  return result 
def exponent(num,exponent):
  result = 1
  for i in range(exponent):
    result= result*num
  return result
def square(num):
  return exponent(num,2)
def main():
  print(multiply(10,2))
  print(exponent(6,2))
  print(exponent(2,3))
  print(square(4))
  print(square(8))
  return main
main()