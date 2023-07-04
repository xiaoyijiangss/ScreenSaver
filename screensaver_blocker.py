
'''screensaver blocker
pressing shift key every `max_interval` seconds if no movement or keystrokes
also displaying current calendar week number

dependencies
    - pynput
'''

from pynput import keyboard, mouse
import time
import datetime as dt


m = mouse.Controller()
k = keyboard.Controller()

#-- maximum interval in seconds to press shift key if there's no movement
max_interval = 60           

#-- interval for software to check whether there's movement of mouse / keyboard
pull_interval = 5           

has_keystroke = False


def on_press(key):
    """event listener for listening keyboard inputs
    """
    global has_keystroke
    has_keystroke = True


def move_a_little():
    """move a little bit to prevent screen lock
    """
    global listener
    listener.stop()
    print("++ pressing shift", flush=True)
    k.press(keyboard.Key.shift)
    k.release(keyboard.Key.shift)
    listener = keyboard.Listener(
        on_press = on_press
    )
    listener.start()


if __name__ == "__main__":

    listener = keyboard.Listener(
        on_press = on_press
    )
    listener.start()

    while True:
        last_pos = m.position
        has_keystroke = False
        start_time = time.time()
        year = dt.date.today().year
        kw = dt.date.today()
        print(kw)
        kw_str = str(year) + 'kw' + str(kw)

        print(">> reset, current time = {:.0f}".format(start_time), flush=True)

        while True:

            time.sleep(pull_interval)

            print("lapsing, time = {:.0f}, {}".format(time.time(), kw_str, flush=True))

            if has_keystroke:
                print("++ keystroke, reset", flush=True)
                break
            elif time.time() - start_time > max_interval:
                move_a_little()
                break
            elif m.position != last_pos:
                print("++ mouse movement, reset", flush=True)
                break
            else:
                continue
