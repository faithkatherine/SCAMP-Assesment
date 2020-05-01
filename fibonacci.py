terms = int(input("enter the number of terms to output:"))
n = 0
n = int(input("enter the number to get its sequence"))
n1,n2 = 1,1
print("the sequence for the number", n , "is:")

count = 0

if terms <= 0:
       print("enter a positive number")

elif terms == 1:
     print("the sequence for the number is:")
     print(n1)

else:
   
     for count in range(terms):
          n = (n1) + (n2)
          print(n1, n2, n)
          n1 = n2
          n2 = n
          

         


     

 



