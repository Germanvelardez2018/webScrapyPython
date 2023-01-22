import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


PATH = r"~/driver/chormedriver"
os.environ['PATH']+=PATH
driver = None




def init_driver():
    global driver 
    driver = webdriver.Chrome()



def find_element():
    try:
        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pyenv")
        elem.send_keys(Keys.RETURN)
        # Comprobamos que tenemos resultados validos diferentes de No "result found"
        assert "No results found." not in driver.page_source 
    except :
        pass

def get_page(page):
    global driver
    driver.get(page)

def close_driver():
    global driver
    driver.close()

def Main():
    try:
        init_driver()
        get_page("http://www.python.org")
        while True:
            pass   # Si el programa termina la ventana chrom se cierra rapidamente
        close_driver()
        
       
    except:
        pass


if __name__ == '__main__':
    Main()