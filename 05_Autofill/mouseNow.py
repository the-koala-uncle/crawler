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
        pixelColor = pyautogui.screenshot().getpixel((x, y)) 
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3) 
        positionStr += ', ' + str(pixelColor[1]).rjust(3) 
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')' 
        print(positionStr+'\n', end='')
        time.sleep(1)
except KeyboardInterrupt: 
    print('\nDone.')
# Get and print the mouse coordinates. 
