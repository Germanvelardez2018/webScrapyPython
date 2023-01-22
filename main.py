import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


PATH = r"~/driver/chormedriver"
os.environ['PATH']+=PATH


def Main():
    try:
        driver = webdriver.Chrome()
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pyenv")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source # Comprobamos que tenemos resultados validos diferentes de No "result found"
      #  driver.close()
        while True:
            pass   # Si el programa termina la ventana chrom se cierra rapidamente

        
       
    except:
        pass


if __name__ == '__main__':
    Main()