def add(a,b):

	pass

def subtract(a,b):

	pass

def multiply(a,b):
	return a*b

def divide(a,b):
	return a/b

def menu():
 while True:
  print("Select opration:")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")

  choice=input("Enter choice(1/2/3/4):")

  if choice not in("1","2","3","4"):
   print("Error,please enter again")
   continue
  
  try:
   a=float(input("Enter first number:"))
   b=float(input("Enter second number:"))
  except ValueError:
   print("Invalid input.Enter numbers.")
   continue

  if choice=='1':
   result=add(a,b)
   print(f"{a}+{b}={result}")
  elif choice=="2":
   result=subtract(a,b)
   print(f"{a}-{b}={result}")
  elif choice=="3":
   result=multiply(a,b)
   print(f"{a}*{b}={result}")
  elif choice=="4":
   result=divide(a,b)
   print(f"{a}/{b}={result}")

  again=input("Let's do next calculation?(yes/no):")
  if again!="yes":
   break

if __name__=="__main__":
 menu()
