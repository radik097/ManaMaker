import asyncio
import cv2
import pyautogui
import numpy as np

class TemplateMatcher:
    def __init__(self):
        self.templates = {
            'yes_button': cv2.imread('yes_template.png', 0),
            'no_button': cv2.imread('no_template.png', 0),
            'card_notification': cv2.imread('notification_template.png', 0)
        }

    async def match_template(self, template_name):
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
        template = self.templates.get(template_name)
        if template is not None:
            result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
            _, _, _, max_loc = cv2.minMaxLoc(result)
            center_loc = (max_loc[0] + template.shape[1]//2, max_loc[1] + template.shape[0]//2)
            return center_loc
        return None

# Usage
async def main():
    matcher = TemplateMatcher()
    yes_button_location = await matcher.match_template('yes_button')
    print(yes_button_location)

if __name__ == "__main__":
    asyncio.run(main())
