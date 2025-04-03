import pyautogui
from PIL import Image
import time

from pynput import keyboard

#time.sleep(5)
playing = False

# TODO Put screenshot and color analysis into functions
while playing:
    img = pyautogui.screenshot('screen.png', region=(200, 600, 300, 300))
    pil_img = Image.open('screen.png').convert('L')  # Open in Grey scale
    width, height = pil_img.size

    pixel_nb = 0
    total_value = 0
    for x in range(width):
        for y in range(height):
            value = pil_img.getpixel((x, y))
            total_value += pil_img.getpixel((x, y))
            pixel_nb += 1
    mean_black = total_value / pixel_nb
    print(mean_black)
    if mean_black < 251:
        pyautogui.press('space')
        time.sleep(0.5)


def on_press(key):
    if key == keyboard.Key.space:
        pyautogui.screenshot('test.png', region=(200, 600, 300, 300))
        pil_img = Image.open('test.png').convert('L')  # Open in Grey scale
        width, height = pil_img.size

        pixel_nb = 0
        total_value = 0
        for x in range(width):
            for y in range(height):
                value = pil_img.getpixel((x, y))
                total_value += pil_img.getpixel((x, y))
                pixel_nb += 1
        mean_black = total_value / pixel_nb
        print(mean_black)


test = True
while test:
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()
