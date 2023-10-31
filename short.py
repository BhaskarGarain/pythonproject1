import tkinter
import pyshorteners

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get()) #tinturl api
    print(shorturl_entry.insert(0, short_url)) #inserted at index 0
    

root = tkinter.Tk() #creat a root windo
root.title("URL Shortener") #title of window
root.geometry("300x150")


longurl_label = tkinter.Label(root, text="Enter Long URL") #class for lebel and root is parent text is which will show
longurl_entry = tkinter.Entry(root) #entry is text box
shorturl_label=tkinter.Label(root, text="Output shortened URL") 
shorturl_entry = tkinter.Entry(root)
shorten_button = tkinter.Button(root, text="Shorten URL", command=shorten) #class for button

longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shorten_button.pack()

root.mainloop() #run a infi loop to show the app as long as i dont close it