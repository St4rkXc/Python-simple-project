import datetime
import time
import winsound
from tkinter import *


def alarm(set_alarm_timer):
    while True:
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%y")
        print("The set date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break
        time.sleep(1)


def set_alarm():
    hour = hour_var.get()
    minute = minute_var.get()
    second = second_var.get()
    set_alarm_timer = f"{hour:02d}:{minute:02d}:{second:02d}"
    alarm(set_alarm_timer)


def start_timer():
    timer_seconds = int(timer_seconds_var.get())
    while timer_seconds > 0:
        timer_display.config(text=str(timer_seconds))
        time.sleep(1)
        timer_seconds -= 1
        clock.update()
    winsound.PlaySound(
        "sound.wav", winsound.SND_ASYNC
    )  # alarm idup
    timer_display.config(text="Time's up!")


clock = Tk()
clock.title("Stark's Clock")
clock.geometry("400x300")


time_format = Label(
    clock, text="Enter 24 Hour Format", fg="red", bg="black", font="arial"
)
time_format.place(x=60, y=120)

hour_var = IntVar()
minute_var = IntVar()
second_var = IntVar()

hour_label = Label(clock, text="Hour:", font=("Helvetica", 10))
hour_label.place(x=80, y=160)
hour_entry = Entry(clock, textvariable=hour_var, bg="lightgreen", width=3)
hour_entry.place(x=120, y=160)

minute_label = Label(clock, text="Min:", font=("Helvetica", 10))
minute_label.place(x=150, y=160)
minute_entry = Entry(clock, textvariable=minute_var, bg="lightgreen", width=3)
minute_entry.place(x=180, y=160)

second_label = Label(clock, text="Sec:", font=("Helvetica", 10))
second_label.place(x=210, y=160)
second_entry = Entry(clock, textvariable=second_var, bg="lightgreen", width=3)
second_entry.place(x=240, y=160)

set_alarm_button = Button(
    clock, text="Set Alarm", fg="red", width=10, command=set_alarm
)
set_alarm_button.place(x=150, y=200)


timer_label = Label(clock, text="Enter Timer (seconds):", font=("Helvetica", 10))
timer_label.place(x=100, y=240)

timer_seconds_var = IntVar()
timer_entry = Entry(clock, textvariable=timer_seconds_var, bg="lightgreen", width=15)
timer_entry.place(x=250, y=240)

start_timer_button = Button(
    clock, text="Start Timer", fg="green", width=10, command=start_timer
)
start_timer_button.place(x=150, y=270)

timer_display = Label(clock, text="", font=("Helvetica", 20))
timer_display.place(x=180, y=320)

clock.mainloop()
