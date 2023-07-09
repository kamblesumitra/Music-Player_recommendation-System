

#setup screen
from tkinter import *
from PIL import Image,ImageTk
from pygame import mixer
from tkinter import filedialog
import webbrowser
mixer.init()

root=Tk()
#create list box
songs_list=Listbox(root,selectmode=SINGLE,bg="#EEEEDF",fg="black",font=('arial',15),height=900,width=70,selectbackground="gray",selectforeground="black")
songs_list.place(x=900,y=0)


def Play():
    song = songs_list.get(ACTIVE)
    song = f'C:\\Users\\kambl\\OneDrive\\Desktop\\SUMITRA_112103066_RPPOOP\\songs_player\\{song}'
    mixer.music.load(song)
    mixer.music.play()

def Pause():
    mixer.music.pause()


# to stop the  song
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)


def Previous():
    # to get the selected song index
    previous_one = songs_list.curselection()
    # to get the previous song index
    previous_one = previous_one[0] - 1
    # to get the previous song
    temp2 = songs_list.get(previous_one)
    temp2 = f'C:\\Users\\kambl\\OneDrive\\Desktop\\SUMITRA_112103066_RPPOOP\\songs_player\\{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    # activate new song
    songs_list.activate(previous_one)
    # set the next song
    songs_list.selection_set(previous_one)


def Next():
    # to get the selected song index
    next_one = songs_list.curselection()
    # to get the next song index
    next_one = next_one[0] + 1
    # to get the next song
    temp = songs_list.get(next_one)
    temp = f'C:\\Users\\kambl\\OneDrive\\Desktop\\SUMITRA_112103066_RPPOOP\\songs_player\\{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    # activate newsong
    songs_list.activate(next_one)
    # set the next song
    songs_list.selection_set(next_one)



class musicplayer:
    def __init__(self,Tk):
        self.root=Tk
        self.root.title('Music Player')
        self.root.geometry('1000x1000')
        self.root.configure(background='#ffe6e6')

        # addimage
        self.L_photo = ImageTk.PhotoImage(file='t_gifpic.png')
        L_photo = Label(self.root, image=self.L_photo).place(x=50, y=80, width=460, height=460)

        #Creating Button
        #prev Button
        self.photo_B4 = ImageTk.PhotoImage(file='t_prev2.jpg')
        photo_B4 = Button(self.root, image=self.photo_B4, bd=0, height=70, width=70, bg='white',command=Previous).place(x=50, y=700)
        #play Button
        self.photo_B1=ImageTk.PhotoImage(file='t_play2.png')
        photo_B1=Button(self.root,image=self.photo_B1,bd=0,height=70,width=70,bg='white',command=Play).place(x=150,y=700)
        #play Button
        self.photo_B2=ImageTk.PhotoImage(file='t_pause2.png')
        photo_B2=Button(self.root,image=self.photo_B2,bd=0,height=70,width=70,bg='white',command=Pause).place(x=250,y=700)
        # play Button
        self.photo_B3 = ImageTk.PhotoImage(file='t_stop5.jpg')
        photo_B3 = Button(self.root, image=self.photo_B3, bd=0, height=70, width=70, bg='white',command=Stop).place(x=350, y=700)
        # play Button
        self.photo_B5 = ImageTk.PhotoImage(file='t_next2.jpg')
        photo_B1 = Button(self.root, image=self.photo_B5, bd=0, height=70, width=70, bg='white',command=Next).place(x=450, y=700)

    # add many songs to the playlist of python mp3 player




obj=musicplayer(root)


def addsongs():
    # to open a file
    temp_song = filedialog.askopenfilenames(initialdir="C:\\Users\\kambl\\OneDrive\\Desktop\\SUMITRA_112103066_RPPOOP\\songs_player\\",title="Choose a song",
                                            filetypes=(("mp3 Files", "*.mp3"),))
    ##loop through every item in the list to insert in the listbox
    for s in temp_song:
        s = s.replace("C:/Users/kambl/OneDrive/Desktop/SUMITRA_112103066_RPPOOP/songs_player/", "")
        songs_list.insert(END, s)

def deletesong():
    curr_song = songs_list.curselection()
    songs_list.delete(curr_song[0])


canvas = Canvas(root, width=20, height=root.winfo_screenheight(), bg="#CDCDAA")
canvas.place(x=1800, y=0)
def link():
    webbrowser.open_new(r"http://localhost:8501/")

rec_button = Button(root, text="Recommended for you <3", font=70, width=50, bg='#ffcccc', command=link)
rec_button.place(x=50, y=600)








my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",font=300,menu=add_song_menu)
add_song_menu.add_command(label="Add songs",font=300,command=addsongs)
add_song_menu.add_command(label="Delete song",font=300,command=deletesong)
add_song_menu.add_command(label="Exit",font=300,command=root.destroy)
root.mainloop()