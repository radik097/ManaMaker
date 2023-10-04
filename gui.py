import tkinter as tk
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

        keyboard.add_hotkey('f5', self.start)
        keyboard.add_hotkey('f6', self.stop)
        keyboard.add_hotkey('f7', self.toggle_debug)

    def start(self, event=None):
        print(f'User pressed Start, state: {self.start_button["state"]}')
        if self.start_button['state'] == 'disabled':
            self.start_button.config(bg='grey',state='normal')
        else:
            self.start_button.config(bg='green', state='disabled')
            self.stop_button.config(bg='grey', state='normal',fg='black')

    def stop(self, event=None):
        print(f'User pressed Stop, state: {self.stop_button["state"]}')
        if self.stop_button['state'] == 'disabled':
            self.stop_button.config(bg='grey',state='normal')
        else:
            self.stop_button.config(bg='green', state='disabled')
            self.start_button.config(bg='grey', state='normal',fg='black')

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

if __name__ == "__main__":
    root = tk.Tk()
    root.overrideredirect(True)  # Remove window decorations
    root.wm_attributes('-topmost', True)  # Keep window always on top
    coords_mouse = tk.Toplevel(root)
    app = App(root, coords_mouse)
    root.mainloop()
