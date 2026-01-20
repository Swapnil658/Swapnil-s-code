a= input("Enter the student's Name:")
b= int(input("Enter the student's Roll number:"))
c= int(input("Enter the student's Class:"))
d= input("Enter the student's Section:")

if b<50 and c<12:
    
 e= int(input("Enter your marks in English:"))
 f= int(input("Enter your marks in Physics:"))
 g= int(input("Enter your marks in Chemistry:"))
 h= int(input("Enter your marks in Mathematics:"))
 i= int(input("Enter your marks in Computer Science:"))
 j= int(input("Enter your marks in Physical Education:"))

else:
    print("Enter Right Class Data")
    print("Enter Right Roll Number")

if e>100 or f>100 or g>100 or h>100 or i>100 or j>100:
    print("Please enter valid marks")

if e+f+g+h+i > e+f+g+h+j:
    print("Total Marks:",e+f+g+h+i+j)
    print("Percentage:",(e+f+g+h+i)/5)

elif f+g+h+i+j > e+g+h+i+j:
    print("Total Marks:",e+f+g+h+i+j)
    print("Percentage:",(f+g+h+i+j)/5)

elif e+f+g+i+j > e+f+h+i+j:
    print("Total Marks:",e+f+g+h+i+j)
    print("Percentage:",(e+f+g+i+j)/5)

elif e+f+g+h+j > e+f+g+h+i:
    print("Total Marks:",e+f+g+h+i+j)
    print("Percentage:",(e+f+g+h+j)/5)

elif e+g+h+i+j > f+g+h+i+j:
    print("Total Marks:",e+f+g+h+i+j)
    print("Percentage:",(e+g+h+i+j)/5)

elif e+f+h+i+j > e+f+g+i+j:
    print("Total Marks:",e+f+g+h+i+j)
    print("Percentage:",(e+f+h+i+j)/5)

else:
    print("You have entered wrong marks")

if e+f+g+h+i/5>=90 or f+g+h+i+j/5>=90 or e+f+g+i+j/5>=90 or e+f+g+h+j/5>=90 or e+g+h+i+j/5>=90 or e+f+h+i+j/5>=90:
    print("GRADE A")

elif e+f+g+h+i/5>=75 or f+g+h+i+j/5>=75 or e+f+g+i+j/5>=75 or e+f+g+h+j/5>=75 or e+g+h+i+j/5>=75 or e+f+h+i+j/5>=75:
    print("GRADE B")

elif e+f+g+h+i/5>=60 or f+g+h+i+j/5>=60 or e+f+g+i+j/5>=60 or e+f+g+h+j/5>=60 or e+g+h+i+j/5>=60 or e+f+h+i+j/5>=60:
    print("GRADE C")

elif e+f+g+h+i/5>=40 or f+g+h+i+j/5>=40 or e+f+g+i+j/5>=40 or e+f+g+h+j/5>=40 or e+g+h+i+j/5>=40 or e+f+h+i+j/5>=40:
    print("GRADE D")

elif e+f+g+h+i/5>=40 or f+g+h+i+j/5<40 or e+f+g+i+j/5<40 or e+f+g+h+j/5<40 or e+g+h+i+j/5<40 or e+f+h+i+j/5<40:
    print("FAIL")

if e>=75 or f>=75 or g>=75 or h>=75 or i>=75 or j>=75:
    print("Distinction")
elif e>=33 or f<=33 or g<=33 or h<=33 or i<=33 or j<=33:
    print("Passed")
elif e<33 or f<33 or g<33 or h<33 or i<33 or j<33:
    print("Failed")