

if __name__ == "__main__":
    root = tk.Tk()
    root.overrideredirect(True)  # Remove window decorations
    root.wm_attributes('-topmost', True)  # Keep window always on top
    coords_mouse = tk.Toplevel(root)
    app = App(root, coords_mouse)
    root.mainloop()
