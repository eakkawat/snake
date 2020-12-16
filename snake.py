import curses

#Set up window
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

#Snake and food
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)

# Game logic
score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    for c in snake:
        win.addch(c[0], c[1], '*')

    win.addch(food[0], food[1], '#')

curses.endwin()
print(f"Final scores = {score}")