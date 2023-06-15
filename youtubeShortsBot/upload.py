from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time, os
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException

#scrapper yt studio avec Firefox (geckodriver)

# Définir les options de Firefox
options = Options()
options.binary_location = r'/opt/firefox/firefox'

# Définir le profil de Firefox
profile = webdriver.FirefoxProfile('/home/toukoum/.mozilla/firefox/0he3tt71.default-release/')
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()

# Définir les capacités désirées du pilote Firefox
desired = DesiredCapabilities.FIREFOX

# Instancier le pilote Firefox avec les options et capacités définies
driver = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired, options=options, executable_path=r'/opt/geckodriver')




#pour toutes les vidéo dans le dossier videos 
dir_path = '/home/toukoum/chatGptApi/Youtube-Shorts-Bot/videos'
count = 0
for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
print("   ", count, " Videos found in the videos folder, ready to upload...")
time.sleep(6)


#on upload tt les vidéo qui sont dans le dossier /video
for i in range(count):
     
    # =======================================
    # Set here your Youtube studio Url
    # =======================================

    driver.get('https://studio.youtube.com/channel/UCzpIAsd_bGAwxVMEFk3HK7w')

    time.sleep(3)

    # Cliquer sur le bouton de téléchargement
    upload_button = driver.find_element(By.XPATH, '//*[@id="upload-icon"]')
    upload_button.click()

    # Attendre 5 secondes
    time.sleep(5)

    
    file_input = driver.find_element(By.XPATH, '//*[@id="content"]/input')

    #représente le chemin relatif du fichier vidéo à télécharger
    simp_path = 'videos/vid{}.mp4'.format(str(i+1))

    #représente le chemin absolu du fichier vidéo à télécharger
    abs_path = os.path.abspath(simp_path)

    print(abs_path)

    file_input.send_keys(abs_path)

    time.sleep(7)

    #bouton pour uploader
    next_button = driver.find_element(By.XPATH, '//*[@id="next-button"]')

    # a faire 3 fois
    next_button = driver.find_element(By.XPATH, '//*[@id="next-button"]')

    #faut cliquer 3 fois sur le bouton next (on vérifie l'erreur qui clc à la 2ème étape)
    for l in range (3):
        while True:
            try:
                next_button.click()
                time.sleep(3)
                break
            #si erreur chelou, on attend... jsp si c le meilleur moyen
            except ElementClickInterceptedException:
                time.sleep(10)   
            except ElementNotInteractableException:
                 time.sleep(10)

    done_button = driver.find_element(By.XPATH, '//*[@id="done-button"]')
    done_button.click()
    time.sleep(5)

    os.remove(abs_path)
    

driver.quit()


