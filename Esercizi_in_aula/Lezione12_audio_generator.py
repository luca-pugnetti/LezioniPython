from gtts import gTTS

# pip install gTTS

# Testo del riassunto
testo = """

Il nostro tempo è limitato, per cui non lo dobbiamo sprecare vivendo la vita di qualcun altro. Non facciamoci intrappolare dai dogmi, che vuol dire vivere seguendo i risultati del pensiero di altre persone. Non lasciamo che il rumore delle opinioni altrui offuschi la nostra voce interiore. E, cosa più importante di tutte, dobbiamo avere il coraggio di seguire il nostro cuore e la nostra intuizione. In qualche modo, essi sanno che cosa vogliamo realmente diventare. Tutto il resto è secondario.

"""

audio = gTTS(text=testo, lang='it')
audio_file_path = (f"testoAudio.mp3")
audio.save(audio_file_path)

print(f"File audio salvato come {audio_file_path}")