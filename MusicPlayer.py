from pygame import mixer #tuodaan pygame mixer
import os.path #tuodaan os kirjasto.
from tkinter import *
from tkinter import filedialog #tuodaan tiedostodialogi toiminnallisuus
from tkinter.font import Font #tuodaan fonttikirjasto.


mixer.init()

#funktio musiikkitiedoston toistamiseen.
def play():
    #track muuttujaan tallennetaan valittu kappale.
    track = filedialog.askopenfilename()
    #trackName muuttujaan tallennetaan kappaleen nimi.
    trackName = os.path.basename(track)
    #ladataan kappale
    mixer.music.load(track)
    #näytetään songName komponentissa toistettavan kappaleen nimi.
    songName.config(text = trackName)
    #aloitetaan kappaleen toistaminen.
    mixer.music.play()

#funktio jolla kappaleen toisto laitetaan tauolle.
def pause():
    mixer.music.pause()

#funktio, jolla kappaleen toistoa jatketaan.
def continuePlay():
    mixer.music.unpause()

#funktio, joka lopettaa kappaleen toiston.
def stopPlay():
    mixer.music.stop()

#funktio, jolla voi säätään toistettavan kappaleen äänenvoimakkuutta. 
def setVolume(value):
    volume = int(value) 
    mixer.music.set_volume(volume)




root = Tk()
root.config(background = 'cornsilk3')
root.title('Music')

#tallennetaan muuttujaan ohjelmassa käytettävä fontti.
titlefont = Font(family = 'MV Boli')

#luodaan frame komponentit ja annetaan niille taustaväri. frame komponenteilla voidaan asemoida
#muita komponentteja. 
frame1 = Frame()
frame1.configure(background = 'cornsilk3')

frame2 = Frame()
frame2.configure(background = 'cornsilk3')
frame3 = Frame()
frame3.configure(background = 'cornsilk3')
frame4 = Frame()
frame4.configure(background = 'cornsilk3')

#määritellään ohjelmassa käytettävät kuvakkeet.
playicon = PhotoImage(file = 'play.png')
finalplay = playicon.subsample(4,4)

pauseicon = PhotoImage(file = 'pause.png')
finalpause = pauseicon.subsample(4,4)

stopicon = PhotoImage(file = 'stop.png')
finalstop = stopicon.subsample(4,4)

continueicon = PhotoImage(file = 'continuous.png')
finalcont = continueicon.subsample(4,4)

#luodaan skaala-asteikko, jolla musiikin voimakkuutta voidaan säätää 0-100 välillä.
volumeLevel = Scale(frame4,from_ = 0, to_ = 100, orient = HORIZONTAL, resolution = 1, command = setVolume, bg = 'cornsilk3') 
#asetetaan skaalan oletusarvoksi 50.
volumeLevel.set(50)

#luodaan label komenoolla tekstikomponentit
volumeTxt = Label(frame4, text = 'Set volume ', font = titlefont, bg = 'cornsilk3')
songName = Label(frame3,bg = 'cornsilk3')
songNameLabel = Label(frame3, text = 'Now playing: ',bg = 'cornsilk3')
titlelabel = Label(root, text = 'Music player', font = titlefont, fg = 'blue',bg = 'cornsilk3')

#luodaan button komenolla painikkeet, image komennolla kerrotaan niissä käytettävät kuvakkeet ja
#command komennolla kerrotaan funktio, joka suoritetaan kun painiketta painetaan.

playMusic = Button(frame1, image = finalplay, command = play)
pauseMusic = Button(frame1, image = finalpause, command = pause)
keepPlaying = Button(frame2, image = finalcont, command = continuePlay)
stop = Button(frame2, image = finalstop, command = stopPlay)



#pakataan komponentit, pady ja padx komennoilla lisätään tyhjää tilaa komponenttien ympärille
titlelabel.pack()
frame1.pack()
frame2.pack()
playMusic.pack(side = LEFT,pady=4,padx=4)
pauseMusic.pack(side = RIGHT,pady=4,padx=4)
keepPlaying.pack(side = LEFT,pady=4,padx=4)
stop.pack(side = RIGHT,pady=4,padx=4)
frame4.pack()
volumeTxt.pack(side=LEFT)
volumeLevel.pack(side=RIGHT,padx = 4, pady = 4)
frame3.pack()
songNameLabel.pack(side=LEFT)
songName.pack()

mainloop()

    

