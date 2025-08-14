from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time



PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.set_window_size(1580, 1220)


testJob = {
    "arbetsgivare":"Svenska Storesupport Bemanning AB",
    "jobb": "Lagerarbetare",
    "ort": "Örebro",
    "datum": "2022-10-07"
}


driver.get("https://arbetsformedlingen.se/loggain")

link = driver.find_element("link text", "Bank-id")
# time.sleep(3)
link.click()


time.sleep(20)
driver.get("https://arbetsformedlingen.se/for-arbetssokande/mina-sidor/aktivitetsrapportera")


button = WebDriverWait(driver, 10).until( # Lägg till akiviteter
EC.element_to_be_clickable((By.XPATH, '//*[@id="arw-container"]/ng-component/arw-full-page-block[2]/div/section/div/div/div[1]/div/div/div[2]/digi-ng-button-icon-text/digi-ng-button-base/button/div/digi-ng-typography-icon-text/div/span[text()="Lägg till aktiviteter"]')))
button.click()



# TODO
# Fix dates so its always for the last months.
# if date != last months, then random day 1-28

def findJob(arb, job, stalle, datum): # Arbetsgivare, tjänst, ort, datum
    time.sleep(5)
    radioButton = driver.find_element(By.XPATH, "//*[@id='soktjobb-typ']/div/digi-ng-form-radiobutton[1]") # The Radio Button
    time.sleep(2)
    radioButton.click()


    arbetsgivare = driver.find_element(By.XPATH, "//*[@id='soktjobb-arbetsgivare']")
    arbetsgivare.send_keys(arb)
    time.sleep(2)

    tjanst = driver.find_element(By.XPATH, "//*[@id='soktjobb-soktTjanst']")
    tjanst.send_keys(job)
    time.sleep(2)

    ort = driver.find_element(By.XPATH, "//*[@id='soktjobb-ort']")
    ort.send_keys(stalle)
    time.sleep(2)

    aktivitetsdatum = driver.find_element(By.XPATH, "//*[@id='soktjobb-aktivitetsdatum']")
    aktivitetsdatum.send_keys(datum)

    spara = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='soktjobb']/arw-uppdatera-aktivitet-knappar/div/digi-ng-button[1]/digi-ng-button-base/button")))  
    spara.click()


""" findJob("Svenska Storesupport Bemanning AB", "Lagerarbetare", "Örebro", "2022-10-07")
findJob("Randstad AB", "IT-strateg", "Örebro", "2022-10-27")
findJob("Försvarsmakten", "IT-strateg", "Örebro", "2022-10-06")
findJob("AFRY AB", "Systemutvecklare/Programmerare", "Örebro", "2022-10-06")
findJob("Insitepart AB", "Lagerarbetare", "Örebro", "2022-10-28")
 """

time.sleep(20) # temp

button = WebDriverWait(driver, 10).until( # Till Min Aktivitetsrapport
EC.element_to_be_clickable((By.XPATH, '//*[@id="arw-container"]/ng-component/arw-full-page-block[2]/div/section/div/div[2]/digi-ng-button/digi-ng-button-base/button')))
button.click()

time.sleep(20) # temp
button = WebDriverWait(driver, 10).until( # Granska och skicka in
EC.element_to_be_clickable((By.XPATH, '//*[@id="arw-container"]/ng-component/arw-full-page-block[2]/div/section/div/div/div[1]/div/div/div[2]/digi-ng-button/digi-ng-button-base/button')))
button.click()

time.sleep(20) # temp
button = WebDriverWait(driver, 10).until( # Skicka in rapport
EC.element_to_be_clickable((By.XPATH, '//*[@id="arw-container"]/ng-component/arw-full-page-block[2]/div/section/div/div[3]/digi-ng-layout-segment/div/div/div[2]/digi-ng-button[1]/digi-ng-button-base/button')))
button.click()

driver.quit()