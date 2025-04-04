import pyautogui
from PIL import Image
import time
from pynput import keyboard


def take_screen():
    pyautogui.screenshot('screen.png', region=(200, 600, 300, 300))


def get_grey_value():
    pil_img = Image.open('screen.png').convert('L')  # Open in Grey scale
    width, height = pil_img.size

    pixel_nb = 0
    total_value = 0
    for x in range(width):
        for y in range(height):
            total_value += pil_img.getpixel((x, y))
            pixel_nb += 1
    mean_black = total_value / pixel_nb
    print(mean_black)
    if mean_black < 251:
        global test
        if not test:
            jump()


def jump():
    pyautogui.press('space')


def on_press(key):
    if key == keyboard.Key.space:
        print('Space')
        take_screen()
        get_grey_value()


# ---------------- Main function -----------------------
playing = True
test = True
# Create listener on Keyboard
# TODO using thread to manage the listener and the while loop
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

while playing:
    # Start taking screen
    take_screen()
    get_grey_value()
    time.sleep(0.1)
