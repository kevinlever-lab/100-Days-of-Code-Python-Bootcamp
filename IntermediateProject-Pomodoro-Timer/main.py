from tkinter import *
import math
"""
Pomodoro Timer

A graphical Pomodoro productivity timer built with Python's Tkinter module
that alternates between work sessions and breaks, tracking completed work
sessions with checkmarks and following the standard Pomodoro technique
cycle of four work sessions followed by a long break.

Process:
    1. When the Start button is clicked:
          a. Increments the repetition counter.
          b. Starts a 25-minute work session for odd repetitions,
             displaying 'Work' in green.
          c. Starts a 5-minute short break for even repetitions,
             displaying 'Break' in pink.
          d. Starts a 20-minute long break after every 8th repetition
             (4 work sessions), displaying 'Break' in red, then
             resets the repetition counter to 0.
    3. The countdown timer updates every second, displaying the remaining
       time in MM:SS format on the tomato canvas.
    4. At the end of each work session a checkmark (✔) is added to the
       check label to track completed Pomodoro sessions.
    5. When the Reset button is clicked:
          - Cancels the current timer.
          - Resets the repetition counter to 0.
          - Resets the timer display to '00:00'.
          - Clears the session label and checkmarks.

Pomodoro Cycle:
    Work Session:   25 minutes (odd repetitions 1, 3, 5, 7).
    Short Break:     5 minutes (even repetitions 2, 4, 6).
    Long Break:     20 minutes (after 8th repetition / 4 work sessions).
    Checkmarks:     One checkmark added after each completed work session.

Functions:
    reset_clicked():      Cancels the active timer, resets all displays
                          and the repetition counter to their initial state.
    start_timer():        Determines the current session type based on
                          the repetition count and starts the appropriate
                          countdown timer.
    count_down(count):    Recursively counts down from the given number
                          of seconds, updating the timer display each
                          second and triggering the next session when
                          the countdown reaches zero.

Dependencies:
    tkinter: Used to build the graphical user interface, including the
             window, canvas, labels, and buttons.
    math:    Used to calculate the minutes component of the countdown
             timer via math.floor().
"""
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 # Seconds for testing purposes. Multiply by 60 for minutes for normal operation.
SHORT_BREAK_MIN = 5 # Seconds for testing purposes. Multiply by 60 for minutes for normal operation.
LONG_BREAK_MIN = 20 # Seconds for testing purposes. Multiply by 60 for minutes for normal operation.
repetitions = 0
timer = None
insert_check =""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_clicked():
    """
    Resets the Pomodoro timer and all UI displays to their initial state.

    Cancels the currently active countdown timer, resets the repetition
    counter to zero, and restores all UI components to their default
    values as they appeared when the application first launched.
    """

    global repetitions
    #stop the timer
    window.after_cancel(timer)
    #Reset the display
    repetitions = 0
    #Reset top label
    timer_label.config(text="Timer")
    #Reset timer text to 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #Reset check label
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """
    Starts the appropriate Pomodoro session timer based on the current
    repetition count and updates the session label accordingly.

    Increments the global repetition counter and determines whether to
    start a work session, a short break, or a long break based on the
    current repetition number. Updates the timer label text and colour
    to reflect the current session type.

    Pomodoro Cycle Logic:
        Odd repetitions  (1, 3, 5, 7): Starts a 25-minute work session.
                                        Timer label displays 'Work' in green.
        Even repetitions (2, 4, 6):    Starts a 5-minute short break.
                                        Timer label displays 'Break' in pink.
        8th repetition:                Starts a 20-minute long break.
                                        Timer label displays 'Break' in red.
                                        Repetition counter is reset to 0
                                        to restart the Pomodoro cycle.

    Note:
        The multiplier for WORK_MIN, SHORT_BREAK_MIN, and LONG_BREAK_MIN
        is currently set to 1 (seconds) for testing purposes. Change the
        multiplier to 60 to count in minutes for normal use.

    Global Variables:
        repetitions (int): The global repetition counter tracking the
                           current position in the Pomodoro cycle,
                           incremented at the start of each session and
                           reset to 0 after the 8th repetition.

    Calls:
        count_down(count): Starts the countdown timer for the calculated
                           session duration in seconds.
    """
    global repetitions
    work_sec = WORK_MIN * 1                 # Seconds for testing purposes. Set to 60 for minutes for normal operation.
    short_break_sec = SHORT_BREAK_MIN * 1   # Seconds for testing purposes. Set to 60 for minutes for normal operation.
    long_break_sec = LONG_BREAK_MIN * 1     # Seconds for testing purposes. Set to 60 for minutes for normal operation.
    repetitions += 1
    #Long break every 8th repetition, work session every odd repetition, short break every even repetition
    if repetitions % 8 == 0:
        count_down(long_break_sec)  # long break timer
        timer_label.config(text="Break", font=(FONT_NAME, 30, "normal"), bg=YELLOW, fg=RED, width=10)
        # reset repetitions to 0
        repetitions = 0
    elif repetitions % 2 == 1:
        count_down(work_sec)  #work timer
        timer_label.config(text="Work", fg=GREEN)
        #timer_label.grid(column=1, row=0)
    else: 
        count_down(short_break_sec)  # short break timer
        timer_label.config(text="Break", font=(FONT_NAME, 30, "normal"), bg=YELLOW, fg=PINK, width=10)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """
    Recursively counts down from the given number of seconds, updating
    the timer display each second and triggering the next Pomodoro
    session when the countdown reaches zero.

    Calculates and displays the remaining time in MM:SS format on the
    canvas timer text. Seconds less than 10 are zero-padded to maintain
    consistent display formatting (e.g. '4:05' instead of '4:5').
    Schedules itself to run again after 1000 milliseconds (1 second)
    until the countdown reaches zero.

    Countdown Behaviour:
        count > 0:  Schedules the next countdown call after 1 second
                    using window.after(), decrementing count by 1 each
                    call and updating the timer display.
        count == 0: Countdown has finished. If the completed session was
                    a work session (odd repetition), appends a checkmark
                    (✔) to the check label to track completed Pomodoro
                    sessions. Calls start_timer() to automatically begin
                    the next session in the Pomodoro cycle.

    Display Format:
        MM:SS - Minutes and zero-padded seconds.
                e.g. 25 minutes displays as '25:00',
                     4 minutes 5 seconds displays as '4:05'.

    Global Variables:
        timer (str):        Stores the reference ID returned by
                            window.after(), used by reset_clicked() to
                            cancel the active countdown if needed.
        insert_check (str): Stores the cumulative string of checkmark
                            characters (✔) displayed in the check label
                            after each completed work session.

    Calls:
        start_timer(): Automatically triggered when the countdown
                       reaches zero to begin the next Pomodoro session.
    """
    global timer
    global insert_check
    #Calculate minutes - Round down
    count_min = math.floor(count / 60)
    #Calculate seconds
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        #Global timer variable
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        # Add a check mark every two repetitions after a work session
        if repetitions % 2 == 1:
            insert_check += "✔"
            check_label.config(text=insert_check)
        # Reset check marks after a long break
        if repetitions % 8 == 0:
            insert_check = ""
            check_label.config(text=insert_check)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

timer_label = Label(text="Timer", font=(FONT_NAME, 30, "normal"), bg=YELLOW, fg=GREEN, width=10)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_clicked)
reset_button.grid(column=2, row=2)

check_label = Label(font=(FONT_NAME, 20, "normal"), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

canvas.grid(column=1, row=1)

#Keep window displayed
window.mainloop()

