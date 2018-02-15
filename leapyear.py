x=int(input("Enter The Year:"))

if(x%4==0):

    if(x%100==0):

        if(x%400==0):

            print("It Is Leap Year")

        else:

            print("It Is NotLeap Year")

    else:

        print("It Is Leap year")

else:

    print("It Is NotLeap Year")
