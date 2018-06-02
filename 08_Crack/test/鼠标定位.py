#! python3 
# mouseNow.py - Displays the mouse cursor's current position. 
import pyautogui,time 
print('Press Ctrl-C to quit.') 
#TODO: Get and print the mouse coordinates.
try: 
    while True: 
          # TODO: Get and print the mouse coordinates.
        x, y = pyautogui.position() 
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) 



        print(positionStr+'\n', end='')
        time.sleep(1)
except KeyboardInterrupt: 
    print('\nDone.')
# Get and print the mouse coordinates. 
