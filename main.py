from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)

    canvas.itemconfig(img_timer,text="00:00")
    timer_label.config(text="Timer",fg=GREEN)
    global reps
    reps=0
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    # if its 8th rep big break
    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=PINK)
        countdown_mechanism(LONG_BREAK_MIN * 60)
    # if its 2nd/4th/6th rep small break
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown_mechanism(SHORT_BREAK_MIN * 60)
    # if its 1st/3rd/5th rep work
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown_mechanism(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown_mechanism(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(img_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown_mechanism, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(0, reps // 2):
            marks += "✔️"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
img_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

# timer_label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)
# start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

# reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

# checkmark
check_mark = Label(fg=RED, bg=YELLOW)
check_mark.grid(row=3, column=1)

window.mainloop()
