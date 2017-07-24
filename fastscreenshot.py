import time
from PIL import Image
from mss import mss

# Fast screenshot
# mss 3.0 ver
# Usage just like pyautogui
# Parameter:
#     region: optional, four-integer tuple (left, top, width, height)
def screenshot(region=None, **kwargs):
    im = None
    monitors = None
    if region == None:
        region = kwargs.get('region')

    with mss() as sct:

        # Region to capture
        monitor = sct.monitors[1]
        if region != None:
            monitor['left'] = int(region[0])
            monitor['top'] = int(region[1])
            monitor['width'] = int(region[2])
            monitor['height'] = int(region[3])

        # Get pixels on image
        sct_img = sct.grab(monitor)
        im = Image.frombytes('RGBA', sct_img.size, bytes(sct_img.raw), 'raw', 'BGRA')
        im = im.convert('RGB')

    return im

# Evaluate screenshot time in seconds
def evaluate_screenshot_time(region=None):
    t = time.time()
    im = screenshot(region)
    return time.time() - t
