import pyautogui
from pyautogui import click, locateCenterOnScreen, moveTo
import os
import time


def instalock(agent, language, window):
    # select agent
    scaling = 1
    image_agent = os.getcwd() + "\\assets\\" + agent + ".png"
    image_lock = os.getcwd() + "\\lock\\" + "lock_" + language + ".png"
    while True:
        position_lock = locateCenterOnScreen(image_lock, confidence=0.9)
        position_agent = locateCenterOnScreen(image_agent, confidence=0.9)

        if position_agent and position_lock:
            break

    x_agent, y_agent = position_agent
    x_lock, y_lock = position_lock

    x_agent = x_agent * scaling
    y_agent = y_agent * scaling

    x_lock = x_lock * scaling
    y_lock = y_lock * scaling

    click(x_agent, y_agent)
    # pyautogui.MINIMUM_DURATION = 0.3
    moveTo(x_lock, y_lock, 0.3, pyautogui.easeInBack)

    click(x_lock, y_lock)
    window.update("agent locked")



