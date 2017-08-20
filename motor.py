from gpiozero import Motor
from time import sleep
import sys, select, tty, termios

motorA = Motor(17,18)
motorB = Motor(22,23)

def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

old_settings = termios.tcgetattr(sys.stdin)
try:
    tty.setcbreak(sys.stdin.fileno())

    i = 0
    while 1:
        if isData():
            c = sys.stdin.read(1)
            print(c)
            if c == '\x1b':
                break
            elif c == 'w':
                motorA.forward()
                motorB.forward()
            elif c == 's':
                motorA.backward()
                motorB.backward()
            elif c == 'a':
                motorA.forward()
                motorB.backward()
            elif c == 'd':
                motorA.backward()
                motorB.forward()
            elif c == 'q':
                motorA.stop()
                motorB.stop()
finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
