import pyautogui
from PIL import Image
import time


time.sleep(5)
playing = True

# TODO create a version that screenshot and get the level of screen everytime space is pressed
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

