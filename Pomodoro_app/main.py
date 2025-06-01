# Pomodoro Application
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = '#9bdeac'
YELLOW = "#f7f5dd"
FONT_NAME = "JetBrains Mono"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    heading.config(text="Timer")
    reps = 0
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)  # Calling function to start timer
        heading.config(text="Long Break Time", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        heading.config(text="Break Time", fg=PINK, )
    else:
        countdown(work_sec)
        heading.config(text="Work Time", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_second = count % 60

    if count_second < 10:
        count_second = f"0{count_second}"

    # To change element of canvas we use canvas.item config()
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔️"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=40, bg=YELLOW)
window.minsize(400, 400)

canvas = Canvas(width=200, height=234, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 18, "normal"))
canvas.grid(column=1, row=1)

# Labels
heading = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 28, "normal"), bg=YELLOW)
heading.grid(column=1, row=0)
check_mark = Label(fg=GREEN, font=(FONT_NAME, 12, "normal"), bg=YELLOW)
check_mark.grid(column=1, row=2)

# Buttons
start_button = Button(text="Start", fg=PINK, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", fg=RED, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
