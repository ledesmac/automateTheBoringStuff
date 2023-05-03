#! python3
# 2048.py - Script to play 2048 game by looping through the same moves
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def main():
    browser = webdriver.Firefox()
    browser.get('https://gabrielecirulli.github.io/2048/')


    #Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT
    try:
        elem = browser.find_element(By.TAG_NAME, "html")
        container = browser.find_element(By.CLASS_NAME, "game-container")
        all_children_by_css = container.find_element(By.CLASS_NAME,"game-message")
        running = True
        while running:
            elem.send_keys(Keys.UP)
            time.sleep(0.1)
            elem.send_keys(Keys.RIGHT)
            time.sleep(0.1)
            elem.send_keys(Keys.DOWN)
            time.sleep(0.1)
            elem.send_keys(Keys.LEFT)
            time.sleep(0.1)
            classes = all_children_by_css.get_attribute("class")
            print(classes)
            if 'game-over' in classes:
                running = False
            
        print("GAME OVER")
    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    main()