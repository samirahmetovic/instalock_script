from pyautogui import click, locateCenterOnScreen

def instalock(agent):
    scaling = 1
    image = agent + ".png"
    while True:
        position = locateCenterOnScreen(image, confidence=0.9)

        if position:
            break

    x, y = position

    x = x * scaling
    y = y * scaling
    click(x,y)