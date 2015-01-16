import curses

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit ")
stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()

curses.endwin()
