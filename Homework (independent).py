import time
n = int(input("Enter the limit"))
def countdown(n):
    if(n==0):
        print("Blast Off!")
    else:
        print(n) 
        print('*'*n)
        time.sleep(n)
        countdown(n-1)
countdown(n)