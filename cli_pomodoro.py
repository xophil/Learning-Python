import time
#taking input from user
work_min = int(input("Enter time length in minutes: "))
short_break_min = int(input("Short break timer: "))
long_break_min = int(input("Long break timer: "))


def countdown(seconds):
        minutess = seconds // 60
        secondss = seconds % 60
        print(f"Time: {minutess:02d}:{secondss:02d}")

        for i in range(seconds, 0, -1):
             mins = i // 60 
             secs = i % 60
             print(f"{mins:02d}:{secs:02d}", end="\r")
             time.sleep(1)
        print()



def pomodoro_work_cycle():
    print("============ Work session ============")
    countdown(work_min*60)

def pomodoro_break_cycle():
    print("============ Break ============")
    countdown(short_break_min*60)


def cycle():
    i = 1
    while(i<=4):
        print(f"Work session: {i}")
        pomodoro_work_cycle()

        print(f"Break session: {i}")
        pomodoro_break_cycle()
        i=i+1
    print("============ Time for a long break ============")
    countdown(long_break_min*60)
      


print("Starting with the pomodoro timer")
cycle()
