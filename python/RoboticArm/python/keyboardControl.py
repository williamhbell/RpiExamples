#!/usr/bin/env python
# Robotic arm manipulation with the keyboard and the ncurses module.
# W. H. Bell
import curses
#import usb.core, usb.util

# The main function
def main():

  # Try to connect to the robotic arm
  #roboArm = usb.core.find(idVendor=0x1267, idProduct=0x0000)

  # If the connection fails, then raise an exception
  #if roboArm is None:
  #  raise ValueError("Arm not found")

  # Create a ncurses screen
  stdscr = curses.initscr()

  # Turn off the character echo
  curses.noecho()

  # Turn off the requirement for the enter key to be pressed after the 
  # key.
  curses.cbreak()

  # Add the menu strings
  stdscr.addstr(0,0,"=================================================")
  stdscr.addstr(1,16,"Maplin robotic arm",curses.A_BOLD)
  stdscr.addstr(2,0,"=================================================")
  stdscr.addstr(3,0," LED on: 1")
  stdscr.addstr(4,0," Grip open: q              Grip closed: a")
  stdscr.addstr(5,0," Wrist up: w               Wrist down: s")
  stdscr.addstr(6,0," Elbow up: e               Elbow down: d")
  stdscr.addstr(7,0," Shoulder up: r            Shoulder down: f")
  stdscr.addstr(8,0," Base left: z              Base right: x")
  stdscr.addstr(12,0," To quit: Esc")
  stdscr.addstr(14,0,"=================================================")  

  # Update the terminal with the menu strings
  stdscr.refresh()

  # Use a dict to store the bits for each motor direction and the LED,
  # where th integer value corresponding to the ASCII character is used 
  # as the key
  movement = {}
  movement[ord('z')] = [0,1,0]
  movement[ord('x')] = [0,2,0]
  movement[ord('r')] = [64,0,0]
  movement[ord('f')] = [128,0,0]
  movement[ord('e')] = [16,0,0]
  movement[ord('s')] = [32,0,0]
  movement[ord('w')] = [4,0,0]
  movement[ord('s')] = [8,0,0]
  movement[ord('q')] = [2,0,0]
  movement[ord('a')] = [1,0,0]
  movement[ord('1')] = [0,0,1]

  # Store the keys for the dict, to prevent many function calls.
  cmds = movement.keys()

  # A variable to contain the character typed
  key = 0

  # Loop until someone types Esc (escape)
  while key != 27:
    key = stdscr.getch()
    if key in cmds:
      stdscr.addstr(20,0,str(movement[key]))
      stdscr.refresh()
      #roboArm.ctrl_transfer(0x40,6,0x100,0,movement[key],1000)  
    else:
      print [0,0,0]
      #roboArm.ctrl_transfer(0x40,6,0x100,0,[0,0,0],1000)

  # End the curses window and return the terminal to the user
  curses.endwin()

# Call the main function if this file is executed
if __name__ == '__main__':
  main()
