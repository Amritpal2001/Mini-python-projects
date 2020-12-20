import string
import random

if __name__=="__main__":
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation

while True:
    try:
        pass_len = int(input("Enter length of password: "))
        if pass_len<1 or pass_len>94:
            print("The minimum length of password is 1 and maximum length is 94")
            # as the total of all the above ascii characters is 94
            continue

    except ValueError:
        print("Please enter correct input")
        continue
    else:
        break
pas=[]
pas.extend(list(s1))
pas.extend(list(s2))
pas.extend(list(s3))
pas.extend(list(s4))

print("Password is : ",end="")
print("".join(random.sample(pas,pass_len)));
