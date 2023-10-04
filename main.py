import tkinter as tk
import psutil  # You will need to install this library with pip install psutil
from animated import animate_text
import pyautogui
import cv2
import time
import keyboard

class App:
    def __init__(self, root, coords_mouse):
        self.coords_mouse = coords_mouse
        self.root = root
        self.debug_mode = tk.BooleanVar(value=False)
        self.start_button = tk.Button(root, text='Start (F5)', command=self.start, bg='grey')
        self.start_button.pack()
        self.stop_button = tk.Button(root, text='Stop (F6)', command=self.stop, bg='grey')
        self.stop_button.pack()
        self.debug_checkbutton = tk.Checkbutton(root, text="Debug Mode", variable=self.debug_mode)
        self.debug_checkbutton.pack()

        self.coords_mouse.overrideredirect(True)  # Remove window decorations
        self.coords_mouse.wm_attributes('-topmost', True)  # Keep window always on top
        self.coords_label = tk.Label(coords_mouse, text='Cursor Coords: (0, 0)', borderwidth=0)
        self.coords_label.pack()
        self.update_coords()
        self.is_running = False

        keyboard.add_hotkey('f5', self.start)
        keyboard.add_hotkey('f6', self.stop)
        keyboard.add_hotkey('f7', self.toggle_debug)

    def start(self, event=None):
        print(f'User pressed Start, state: {self.start_button["state"]}')
        self.is_running = True
        if self.start_button['state'] == 'disabled':
            self.start_button.config(bg='grey',state='normal')
            self.is_running = False
        else:
            self.disperse_cards()
            self.start_button.config(bg='green', state='disabled')
            self.stop_button.config(bg='grey', state='normal',fg='black')
        

    def stop(self, event=None):
        print(f'User pressed Stop, state: {self.stop_button["state"]}')
        if self.stop_button['state'] == 'disabled':
            self.stop_button.config(bg='grey',state='normal')
        else:
            self.stop_button.config(bg='green', state='disabled')
            self.start_button.config(bg='grey', state='normal',fg='black')
        self.is_running = False
    
    def disperse_cards(self):
        if self.is_running:
            disperse_card()
            root.after(1000, self.disperse_cards)  # repeat every 1 second

    def toggle_debug(self, event=None):
        print('User pressed F7')
        if self.debug_mode.get():
            print('Debug mode disabled')
        else:
            print('Debug mode enabled')
        self.debug_mode.set(not self.debug_mode.get())
        self.update_coords()

    def update_coords(self):
        x, y = self.root.winfo_pointerx(), self.root.winfo_pointery()
        if self.debug_mode.get():
            print(f'Cursor Coords: ({x}, {y})')
            self.coords_label.config(text=f'Cursor Coords: ({x}, {y})')
            self.coords_mouse.geometry(f'+{x + 5}+{y}')  # Position the window 5 pixels to the right of the cursor
        self.coords_mouse.after(100, self.update_coords)  # update every 100 ms
def is_game_running():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'Hearthstone.exe':
            return True
    return False

def wait_for_game():
    # Call the function with your text
    while not is_game_running():
        animate_text("Waiting for game to start")
    else:
        animate_text("Game is now running")

def click(coords):
    pyautogui.click(coords[0], coords[1])

def find_card_type(image):
    for i in range(1, 5):
        template = cv2.imread(f'Types//Type_card_{i}.png', 0)
        res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)
        if max_val > 0.8:  # threshold for a good match
            return i
    return None

def disperse_card(self, full_dispanse=False):
    click((273, 221))  # Select the card
    time.sleep(0.5)
    click((526, 609))  # Click "Disperse"
    time.sleep(0.5)
    if full_dispanse:
        click((553, 429))  # Confirm
    else:
        click((707, 434))  # Cancel
    time.sleep(0.5)
    screenshot = pyautogui.screenshot()
    card_type = find_card_type(screenshot)
    if card_type is not None:
        print(f'Card type: {card_type}')
        click((552, 405))  # Close current window

if __name__ == "__main__":
    wait_for_game()
    root = tk.Tk()
    root.overrideredirect(True)  # Remove window decorations
    root.wm_attributes('-topmost', True)  # Keep window always on top
    coords_mouse = tk.Toplevel(root)
    app = App(root, coords_mouse)
    root.mainloop()
