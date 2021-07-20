import tkinter as tk
from tkinter.constants import CENTER
from anagram import *

def PrintAnagrams(SortedAnagrams, Frame):
    
    for child in Frame.winfo_children():
        child.destroy()

    max = 2
    NewSortedAnagrams = str("2-Letter Words\n")
    
    for line in SortedAnagrams:
        if (len(line) == max):
            NewSortedAnagrams = NewSortedAnagrams + line + " "
        elif (len(line) > max):
            max = len(line)
            NewSortedAnagrams = NewSortedAnagrams + '\n\n%d-Letter Words\n' % (len(line))
            NewSortedAnagrams = NewSortedAnagrams + line + " "

    var = tk.StringVar()
    var.set(NewSortedAnagrams)

    textlabel1 = tk.Label(Frame, anchor="center", font="Times 14", text="=======================================================================================")
    textlabel2 = tk.Label(Frame, anchor="center", font="Times 14", text="Possible Words")
    textbox = tk.Text(Frame, state="normal", height=560, width=920, spacing1=1,spacing3=1, wrap="word")

    textbox.tag_configure("center", justify='center')
    textbox.insert("1.0",NewSortedAnagrams)
    textbox.tag_add("center", "1.0", "end")
    textbox.configure(state="disabled")

    textlabel1.pack(pady=15)
    textlabel2.pack(padx=5, pady=5)
    textbox.pack(padx=5, pady=5)
    
    
def GenerateAnagrams(Entry,Text):
    AnagramInput = Entry.get()
    UnSortAnagramList = CheckDict(AnagramInput)
    SortedAnagramList = SortAnagrams(UnSortAnagramList)
    PrintAnagrams(SortedAnagramList, Text)

def WindowGen():
    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.geometry("960x720")
    window.title("Anagram Solver")

    EntryFrame = tk.Frame(window)
    EntryFrame.pack(side="top")

    TextFrame = tk.Frame(window)
    TextFrame.pack(side="top")

    EntryLabel = tk.Label(EntryFrame, text = "Enter your Letters Here and Press Generate", justify="center", font=("Times","20"))
    EntryLabel.pack()

    UserEntry = tk.Entry(EntryFrame, justify="center", width=20, font=("Times","20"))
    UserEntry.insert(0,"")
    UserEntry.pack(padx=5,pady=5)

    SubmitButton = tk.Button(EntryFrame, justify="center", font=("Times","20"), text="Generate", command = lambda: GenerateAnagrams(UserEntry,TextFrame))
    SubmitButton.pack(padx=5,pady=5)

    window.mainloop()

if __name__ == '__main__':
    window = tk.Tk()
    EntryFrame = tk.Frame(window)
    Anagrams = ['aa', 'ae', 'ai', 'as', 'at', 'es', 'et', 'is', 'it', 'si', 'ta', 'ti', 'aas', 'ais', 'ait', 'ate', 'eat', 'eta', 'its', 'sae', 'sat', 'sea', 'sei', 'set', 'sit', 'tae', 'tas', 'tea', 'tie', 'tis', 'aits', 'asea', 'ates', 'east', 'eats', 'etas', 'sate', 'sati', 'seat', 'seta', 'site', 'teas', 'ties']
    PrintAnagrams(Anagrams,EntryFrame)