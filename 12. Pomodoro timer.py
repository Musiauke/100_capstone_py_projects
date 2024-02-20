import time

def start_timer(duration, message):
    for i in range(duration, 0, -1):
        print(f"{i} minutes left", end = "\r")
        time.sleep(60)
    print(message)

def pomodoro(work_duration = 25, break_duration = 5):
    try:
        while True:
            start_timer(work_duration, "It's time for a break")
            start_timer(break_duration, "It's time for work")
    except KeyboardInterrupt:
        print("\nPomodoro finished")

if __name__ == "__main__":
    pomodoro()
