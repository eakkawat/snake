import curses

#Set up window
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(1)
win.nodelay(1)

# Game logic

score = 0

while True:
    event = win.getch()

curses.endwin()
print(f"Final scores = {score}")