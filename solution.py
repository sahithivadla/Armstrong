# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false

def checkArmstrong(num):
        # Your code goes here
        temp = num
        sum =0
        while(temp>0):
                d= temp%10
                sum =sum+(d**3)
                temp = temp//10
        if(num!=sum):
                return False

        return True
