from evdev import uinput, ecodes as e
from time import sleep


ui = uinput.UInput()


n_up = 1
n_down = 1

# n_up = 8
# n_down = 1

# n_up = 8
# n_down = 8


def kp(key):
    ui.write(e.EV_KEY, key, 1)
    ui.write(e.EV_KEY, key, 0)
    ui.syn()
    sleep(0.01)


with uinput.UInput() as ui:
    while True:
        for x in range(n_up):
            kp(e.KEY_UP)
            kp(e.KEY_LEFT)
        for x in range(n_down):
            kp(e.KEY_DOWN)
            kp(e.KEY_LEFT)
