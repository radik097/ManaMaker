from rich.console import Console
import time

console = Console()

def animate_text(target_text):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if all(c.isascii() or c.isspace() for c in target_text) else 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    current_text = [' '] * len(target_text)  # Initialize an empty string of the same length as target_text

    for idx, target_char in enumerate(target_text):
        if target_char.isspace():  # Skip spaces
            current_text[idx] = target_char
            continue
        
        # Determine whether the target character is uppercase or lowercase
        is_upper = target_char.isupper()
        char_alphabet = alphabet if is_upper else alphabet.lower()

        for char in char_alphabet:
            current_text[idx] = char

            # Determine the color based on whether the character is correct
            color = "green" if char == target_char else "red"
            
            # Print the current_text with the current character colored
            console.print(''.join([
                char if i != idx else f"[{color}]{char}[/{color}]"
                for i, char in enumerate(current_text)
            ]), end='\r')

            time.sleep(0.05)  # Adjust the speed of the animation

            if char == target_char:
                color = "green" if char == target_char else "red"
                break  # Break early if the correct character is found
