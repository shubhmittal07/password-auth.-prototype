#android screen unlock pin authenticastion
import time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    unlock('Enter the password')
t = 20

def unlock (prompt,retries=1,reminder='try again after 20 seconds',pasword=1425):
 while True:
    key=int(pasword)
    a=input("Enter the password:")
    b=int(a)
    if (b == key):
        print("You are welcome!!!!")
        break
    elif (b != key):
        retries = retries -1
    if (retries < 0):
        print(reminder)
        countdown(int(t))
        break
unlock('Enter the password:')

        





