from moviepy.editor import *

#pour comprendre comment fonctionne moviepy

# Charger la vidéo
video = VideoFileClip("videos/vid1.mp4")

# Créer le clip de texte avec une police blanche sur fond transparent
txt_clip = (TextClip("VERITE ABSOLUE", color='white', font='Helvetica-bold', fontsize=50)
            .set_position('center')
            .set_duration(video.duration))

# Créer le clip de couleur semi-transparent pour le fond du texte
txt_width, txt_height = txt_clip.size
color_clip = (ColorClip(size=(txt_width+75, txt_height+50), color=(0,0,0))
              .set_opacity(.5)
              .set_duration(video.duration)
              .set_position('center'))





# Créer le clip de texte qui apparaît à partir de 5 secondes
txt_clip2 = (TextClip("LE PREMIER QUI S'EXCUSE EST TOUJOURS LE PLUS COURAGEUX", color='white', font='Helvetica-bold', fontsize=50,
                      stroke_color='black', stroke_width=2, kerning=10, align='center', method='caption', interline=-20)
             .set_position('center')
             .set_duration(video.duration))



# Combiner le clip de texte et le clip de couleur
result = CompositeVideoClip([color_clip, txt_clip])

# Centrer la composition
result = result.set_position(lambda t: ('center', 120))

# Combiner la vidéo originale avec le clip de texte
final_result = CompositeVideoClip([video, result, txt_clip2])

# Enregistrer la vidéo finale
final_result.write_videofile("vid1_texte.mp4", fps=video.fps)
