import pynput
import time
from pynput import keyboard
from pynput.keyboard import Key, Controller

keyboard = Controller()

time.sleep(4)


for i in range(4):
  time.sleep(1)
  keyboard.type("wassup")
  keyboard.press
  keyboard.press(Key.enter)
