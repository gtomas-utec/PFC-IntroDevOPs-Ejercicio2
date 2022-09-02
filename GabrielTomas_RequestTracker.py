import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#Ingreso al servidor de mi vm
driver.get("http://192.168.70.114:8117/")
#usuario y clave
user = driver.find_element(By.NAME, "user")
user.clear()
user.send_keys("root")
password = driver.find_element(By.NAME, "pass")
password.clear()
password.send_keys("password")
#ingreso
driver.find_element(By.CLASS_NAME, "btn").click()
#sugirieron refrescar la pagina
driver.get("http://192.168.70.114:8117/")
#asunto
subject = driver.find_element(By.NAME, "Subject")
subject.clear()
subject.send_keys("Asunto del parcial")
#contenido
content = driver.find_element(By.NAME, "Content")
content.clear()
content.send_keys("Se pide para el parcial")
#Click en crear
driver.find_element(By.NAME, "SubmitTicket").click()

#esperamos
time.sleep(20)
#cerramos
driver.close()