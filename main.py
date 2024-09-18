
from tkinter import *
import math

import pygame

pygame.mixer.init()
pygame.mixer.music.load("mixkit-long-pop-2358.wav")
pygame.mixer.music.play()
frequency = 2500
duration = 400


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF407D"
RED = "#D83A56"
GREEN = "#66DE93"
YELLOW = "#FFEAC9"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None
def completion_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("mixkit-select-click-1109.wav")
    pygame.mixer.music.play()
# ---------------------------- TIMER RESET ------------------------------- #

def mouse_click():
    pygame.mixer.init()
    pygame.mixer.music.load("mixkit-mouse-click-close-1113.wav")
    pygame.mixer.music.play()

def modern_mouse_click():
    pygame.mixer.init()
    pygame.mixer.music.load("mixkit-message-pop-alert-2354.mp3")
    pygame.mixer.music.play()
def reset_timer():
    start.config(state="normal")
    global REPS
    window.after_cancel(TIMER)
    REPS = 0
    check_mark.config(text="")
    canvas.itemconfig(timer_count, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    modern_mouse_click()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start.config(state="disabled")
    modern_mouse_click()
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        countdown(long_break_sec)
        timer.config(text="Loooong break 😎", fg=PINK)

    elif REPS % 2 == 0:
        countdown(short_break_sec)
        timer.config(text="Short break 😃", fg=PINK)
        completion_sound()
    else:
        countdown(work_sec)
        timer.config(text="Focus 📖", fg=RED)


def countdown(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")

    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count -1)
        modern_mouse_click()
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✅"
        check_mark.config(text=marks)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro timer", )
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_count = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

timer = Label(text="Timer", font=(FONT_NAME, 30,"bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=2, row=1)

start = Button(text="Start", highlightthickness=0, bg=PINK,command=start_timer)
start.grid(column=0, row=4)
reset = Button(text="Reset", highlightthickness=0, bg=PINK, command=reset_timer)
reset.grid(column=3, row=4)

check_mark = Label(text="", bg=YELLOW, fg=GREEN)
check_mark.grid(column=2, row=5)


window.mainloop()
