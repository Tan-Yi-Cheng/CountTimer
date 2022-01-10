import time

# countdown timer 
def countdown(end):
    while end: # while end > 0 for clarity 
      mins = end // 60
      secs = end % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r") # overwrite previous line 
      time.sleep(1)
      end -= 1
    print('Times out!!!')

loop = 1

while loop==1:
  t = input("Enter the time in seconds: ") 
  countdown(int(t))
  loop = input("Enter 1 if you want to countdown again: ")

print('Welcome to use again~')