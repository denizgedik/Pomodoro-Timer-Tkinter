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
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 1
    label.config(text="Timer", fg=GREEN)
    check_label["text"] = ""
    canvas.itemconfig(timer_text, text="LET'S GO")
    button_start["state"] = "normal"
    button_reset["state"] = "disabled"


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer_work():
    button_start["state"] = "disabled"
    button_reset["state"] = "normal"
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        label["fg"] = GREEN
        label["text"] = "Work"
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        label["fg"] = PINK
        label["text"] = "Break"
    elif reps == 8:
        count_down(long_break_sec)
        label["fg"] = RED
        label["text"] = "Long Break"
    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    global timer
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # elif count_sec == 9 or count_sec == 8 or count_sec == 7 or count_sec == 6 or count_sec == 5 or count_sec == 4 or count_sec == 3 or count_sec == 2 or count_sec == 1:
    #     count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer_work()
        checkmark = ""
        times = (reps // 2) - 1
        for _ in range(times):
            checkmark += "✔"
        check_label["text"] = checkmark


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


# Label
label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
label.grid(column=1, row=0)
check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="LET'S GO", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Button
button_start = Button(text="Start", highlightbackground=YELLOW, highlightthickness=0, command=start_timer_work)
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", highlightbackground=YELLOW, highlightthickness=0, command=reset_timer, state="disabled")
button_reset.grid(column=2, row=2)

















window.mainloop()