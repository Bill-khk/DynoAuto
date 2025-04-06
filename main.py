import multiprocessing
import pyautogui
import time
from PIL import Image
from pynput import keyboard


def take_screen(option):
    global game_time
    distance = int(240 + (round(game_time/8, 0)*30))
    if option:
        pyautogui.screenshot('jump.png', region=(distance, 600, distance, 300))
    else:
        pyautogui.screenshot('screen.png', region=(distance, 600, distance, 300))
        print(f'Distance:{distance}')


def get_grey_value(option):
    if option:
        pil_img = Image.open('jump.png').convert('L')  # Open in Grey scale
    else:
        pil_img = Image.open('screen.png').convert('L')  # Open in Grey scale
    width, height = pil_img.size

    pixel_nb = 0
    total_value = 0
    for x in range(width):
        for y in range(height):
            total_value += pil_img.getpixel((x, y))
            pixel_nb += 1
    mean_black = int(total_value / pixel_nb)
    print(mean_black)
    if mean_black < 251:
        global test
        if not test:
            jump()


def jump():
    pyautogui.press('space')


# The on_press listener is used to set up the program.
def on_press(key):
    global playing
    if key == keyboard.Key.space:
        print('Space')
        take_screen(True)
        get_grey_value(True)
    elif key == keyboard.Key.esc:
        playing = False


def keyboard_listener():
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()


def play():
    time.sleep(3)
    while playing:
        # Start taking screen
        take_screen(False)
        get_grey_value(False)
        time.sleep(0.05)


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
# TODO Make ESC stop the other thread
if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=play)
    p2 = multiprocessing.Process(target=keyboard_listener)
    p3 = multiprocessing.Process(target=count_time)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
