import threading
import pyautogui
import time
from PIL import Image
from pynput import keyboard

#Game URL=https://elgoog.im/dinosaur-game/
def take_screen(option):
    global game_time
    distance = int(240 + (round(game_time / 8, 0) * 30)) # TODO Try to change the distance based on the number of jump instead ?
    if option:
        pyautogui.screenshot('jump.png', region=(distance, 600, distance, 300))
    else:
        pyautogui.screenshot('screen.png', region=(distance, 600, distance, 300))
        # print(f'Distance:{distance}') # Used to see the translation of the screenshot


def get_grey_value(option):
    if option:
        pil_img = Image.open('jump.png').convert('L')  # Open in Grey scale
    else:
        pil_img = Image.open('screen.png').convert('L')  # Open in Grey scale
    width, height = pil_img.size

    pixel_nb = 0
    total_value = 0
    top_value = 0
    bot_value = 0
    for x in range(width):
        for y in range(height):
            total_value += pil_img.getpixel((x, y))
            if y >= height / 2:
                top_value += pil_img.getpixel((x, y))
            else:
                bot_value += pil_img.getpixel((x, y))
            pixel_nb += 1
    mean_black = int(total_value / pixel_nb)
    print(mean_black)
    if mean_black < 251:
        global test
        if not test:
            print(f'Jump, mb={mean_black}, top_value={top_value}, bo_value={bot_value}') # Check behavior based on top_value and bot_value
            jump()


def jump():
    pyautogui.press('space')


def keyboard_listener():
    def on_press(key):
        global playing
        if key == keyboard.Key.space:
            print('Space')
            take_screen(True)
            get_grey_value(True)
        elif key == keyboard.Key.esc:
            playing = False
            return False

    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()


def play():
    time.sleep(3)
    while playing:
        # Start taking screen
        take_screen(False)
        get_grey_value(False)


def count_time():
    global game_time
    while playing:
        game_time += 1
        time.sleep(1)


# ---------------- Main function -----------------------
test = False
playing = True
game_time = 0

# ---------------- Test ----------------------- Code use to display where the screenshot is going to be taken
# import tkinter as tk
# x, y = 200, 600
# width, height = 200, 300
# root = tk.Tk()
# root.attributes("-topmost", True)       # Always on top
# root.overrideredirect(True)            # No window borders
# root.geometry(f"{width}x{height}+{x}+{y}")       # Size and position
# root.wm_attributes("-transparentcolor", "white")
# root.configure(bg='white')  # Set background to match transparency
# canvas = tk.Canvas(root, width=width, height=height, highlightthickness=0)
# canvas.pack()
# root.mainloop()
# ---------------- Main function -----------------------

# TODO manage flying bird and ducking
if __name__ == "__main__":
    # creating processes
    t1 = threading.Thread(target=play)
    t2 = threading.Thread(target=keyboard_listener)
    t3 = threading.Thread(target=count_time)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
