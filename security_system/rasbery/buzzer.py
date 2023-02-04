from gpiozero import Buzzer
from signal import pause


def buzz():
    buzzer = Buzzer(4)
    buzzer.beep(0.5, 0.5)
    pause()
