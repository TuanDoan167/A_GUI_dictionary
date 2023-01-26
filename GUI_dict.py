"""
GUI dictionary
First, the program asks for an txt input file to read from. Each line of the file should have the formart: a word in english: translation in Spanish
Then, the user can find a word, edit the dictionary by adding new word or remove word, save changes to a new txt file or overwrite the file.
The program also allow user to translate a whole sentence or print all pair of english-spanish words in the dictionary.
"""


from tkinter import *


class getinputfile_interface:
    """
    This interface will appear first when the program is run. It askes for the input file name to read from.
    """
    def __init__(self):
        self.__mydict = {}
        self.__mainwindow = Tk()
        self.__labelA = Label(self.__mainwindow, text="Enter the file name: ")
        self.__filename = Entry(self.__mainwindow)
        self.__result_text = Label(self.__mainwindow, text="")
        self.__open_button = Button(self.__mainwindow, text="Open file", command=self.open)
        self.__quit_button = Button(self.__mainwindow, text="Quit", command=self.quit)

        self.__labelA.pack()
        self.__filename.pack()
        self.__result_text.pack()
        self.__open_button.pack()
        self.__quit_button.pack()

    def open(self):
        filename = self.__filename.get()
        try:
            output_file = open(filename, mode='r')
            my_dict = {}
            for line in output_file:
                parts = line.split(":")
                if len(parts) == 2:
                    english_word = parts[0].strip()
                    spanish_word = parts[1].strip()
                    my_dict[english_word] = spanish_word
            output_file.close()
            self.__mainwindow.destroy()
            newui = User_interface(my_dict)
            newui.start()
        except OSError:
            self.__result_text.configure(text="Cannot open file")

    def start(self):
        self.__mainwindow.mainloop()

    def quit(self):
        self.__mainwindow.destroy()


class User_interface:
    """
    The main interface where all the functions can be chosen
    """
    def __init__(self, my_dictionary):
        self.__mydict = my_dictionary
        self.__mainwindow = Tk()

        self.__labelA = Label(self.__mainwindow, text="Welcome to my dictionary", background="Green", foreground="Yellow")
        self.__word_button = Button(self.__mainwindow, text="Word", command=self.word)
        self.__add_button = Button(self.__mainwindow, text="Add", command=self.add)
        self.__remove_button = Button(self.__mainwindow, text="Remove", command=self.remove)
        self.__print_button = Button(self.__mainwindow, text="Print", command=self.print)
        self.__translate_button = Button(self.__mainwindow, text="Translate", command=self.translate)
        self.__save_button = Button(self.__mainwindow, text="Save Changes", command=self.save)
        self.__quit_button = Button(self.__mainwindow, text="Quit", command=self.quit)

        self.__labelA.pack()
        self.__word_button.pack(side=LEFT)
        self.__add_button.pack(side=LEFT)
        self.__remove_button.pack(side=LEFT)
        self.__print_button.pack(side=LEFT)
        self.__translate_button.pack(side=LEFT)
        self.__save_button.pack(side=LEFT)
        self.__quit_button.pack(side=LEFT)

    def word(self):
        word_ui = word_interface(self.__mydict)
        word_ui.start()

    def add(self):
        word_ui = add_interface(self.__mydict)
        word_ui.start()

    def remove(self):
        word_ui = remove_interface(self.__mydict)
        word_ui.start()

    def print(self):
        word_ui = print_interface(self.__mydict)
        word_ui.start()

    def translate(self):
        word_ui = translate_interface(self.__mydict)
        word_ui.start()

    def save(self):
        word_ui = save_interface(self.__mydict)
        word_ui.start()

    def start(self):
        self.__mainwindow.mainloop()

    def quit(self):
        self.__mainwindow.destroy()


class word_interface:
    """
    The interface for look up word
    """

    def __init__(self, my_dictionary):
        self.__mydict = my_dictionary
        self.__mainwindow = Tk()
        self.__labelA = Label(self.__mainwindow, text="Enter word to look up: ")
        self.__search_word = Entry(self.__mainwindow)
        self.__result_text = Label(self.__mainwindow, text="")
        self.__Lookup_button = Button(self.__mainwindow, text="Look up", command=self.lookup)
        self.__quit_button = Button(self.__mainwindow, text="Quit", command=self.quit)

        self.__labelA.pack()
        self.__search_word.pack()
        self.__result_text.pack()
        self.__Lookup_button.pack()
        self.__quit_button.pack()

    def lookup(self):
        word = self.__search_word.get()
        if word in self.__mydict:
            printout = f"\'{word}\' in Spanish is \'{self.__mydict[word]}\'"
            self.__result_text.configure(text=printout)
        else:
            printout = f"The word \'{word}' could not be found from the dictionary."
            self.__result_text.configure(text=printout)

    def start(self):
        self.__mainwindow.mainloop()

    def quit(self):
        self.__mainwindow.destroy()


class add_interface:
    """
    The interface for add new word
    """
    def __init__(self, my_dictionary):
        self.__mydict = my_dictionary
        self.__mainwindow = Tk()
        self.__labelA = Label(self.__mainwindow, text="Enter the word to be added in English:")
        self.__english = Entry(self.__mainwindow)
        self.__labelB = Label(self.__mainwindow, text="Enter the translation in Spanish:")
        self.__spanish = Entry(self.__mainwindow)
        self.__result_text = Label(self.__mainwindow, text="")
        self.__ADD_button = Button(self.__mainwindow, text="ADD", command=self.add)
        self.__quit_button = Button(self.__mainwindow, text="Quit", command=self.quit)

        self.__labelA.pack()
        self.__english.pack()
        self.__labelB.pack()
        self.__spanish.pack()
        self.__result_text.pack()
        self.__ADD_button.pack()
        self.__quit_button.pack()

    def add(self):
        eng = self.__english.get()
        span = self.__spanish.get()
        newpair = {eng: span}
        self.__mydict.update(newpair)
        self.__english.delete(0,END)
        self.__spanish.delete(0,END)
        self.__result_text.configure(text=f"New word \'{eng}\' added!")


    def start(self):
        self.__mainwindow.mainloop()

    def quit(self):
        self.__mainwindow.destroy()


class remove_interface:
    """
    The interface for removing word
    """

    def __init__(self, my_dictionary):
        self.__mydict = my_dictionary
        self.__mainwindow = Tk()
        self.__labelA = Label(self.__mainwindow, text="Enter the word to be removed:")
        self.__english = Entry(self.__mainwindow)
        self.__result_text = Label(self.__mainwindow, text="")
        self.__remove_button = Button(self.__mainwindow, text="Remove", command=self.remove)
        self.__quit_button = Button(self.__mainwindow, text="Quit", command=self.quit)

        self.__labelA.pack()
        self.__english.pack()
        self.__result_text.pack()
        self.__remove_button.pack()
        self.__quit_button.pack()

    def remove(self):
        word = self.__english.get()
        if word in self.__mydict:
            del self.__mydict[word]
            printout = f"\'{word}\' was removed from the dictionary"
            self.__result_text.configure(text=printout)
        else:
            printout = f"The word \'{word}\' could not be found from the dictionary."
            self.__result_text.configure(text=printout)

    def start(self):
        self.__mainwindow.mainloop()

    def quit(self):
        self.__mainwindow.destroy()


class print_interface:
    """
    The interface for printing all words
    """
    def __init__(self, my_dictionary):
        self.__mydict = my_dictionary
        self.__mainwindow = Tk()
        self.__labelA = Label(self.__mainwindow, text="All the words in the dictionary are")
        self.__result_text = Label(self.__mainwindow, text="")
        self.__quit_button = Button(self.__mainwindow, text="Quit", command=self.quit)
        self.__print_button = Button(self.__mainwindow, text="Print", command=self.print)

        self.__labelA.pack()
        self.__result_text.pack()
        self.__print_button.pack()
        self.__quit_button.pack()

    def print(self):
        printout = ""
        for pair in sorted(self.__mydict):
            printout += f"{pair} {(self.__mydict[pair])}\n"
        self.__result_text.configure(text=printout)

    def start(self):
        self.__mainwindow.mainloop()

    def quit(self):
        self.__mainwindow.destroy()


class translate_interface:
    """
    The interface for translating a whole sentence
    """
    def __init__(self, my_dictionary):
        self.__mydict = my_dictionary
        self.__mainwindow = Tk()
        self.__labelA = Label(self.__mainwindow, text="Enter the text to be translated into Spanish:")
        self.__englishtext = Entry(self.__mainwindow)
        self.__result_text = Label(self.__mainwindow, text="")
        self.__Translate_button = Button(self.__mainwindow, text="Translate", command=self.translate)
        self.__quit_button = Button(self.__mainwindow, text="Quit", command=self.quit)

        self.__labelA.pack()
        self.__englishtext.pack()
        self.__result_text.pack()
        self.__Translate_button.pack()
        self.__quit_button.pack()

    def translate(self):
        englishtext = self.__englishtext.get()
        englishtext = englishtext.split(' ')

        for i in range(0, len(englishtext)):
            if englishtext[i] in self.__mydict:
                englishtext[i] = self.__mydict[englishtext[i]]

        printout = " ".join(englishtext)
        self.__result_text.configure(text=printout)

    def start(self):
        self.__mainwindow.mainloop()

    def quit(self):
        self.__mainwindow.destroy()


class save_interface:
    """
    The interface for writing the edited changes to file
    """
    def __init__(self, my_dictionary):
        self.__mydict = my_dictionary
        self.__mainwindow = Tk()
        self.__labelA = Label(self.__mainwindow, text="Enter the dictionary name \n  (Same filename as the input file will overwrite the old dictionary. File will be saved as .txt format)")
        self.__filename = Entry(self.__mainwindow)
        self.__quit_button = Button(self.__mainwindow, text="Quit without Save", command=self.quit)
        self.__save_button = Button(self.__mainwindow, text="Save and Quit", command=self.save_and_quit)

        self.__labelA.pack()
        self.__filename.pack()
        self.__quit_button.pack()
        self.__save_button.pack()

    def save_and_quit(self):
        output_filename = self.__filename.get()
        output_filename += ".txt"
        output_dictionary = open(output_filename, mode = "w")
        for engword in sorted(self.__mydict):
            line = engword + ":" + self.__mydict[engword]
            print(line, file=output_dictionary)
        output_dictionary.close()
        self.__mainwindow.destroy()


    def start(self):
        self.__mainwindow.mainloop()

    def quit(self):
        self.__mainwindow.destroy()


def main():
    ui = getinputfile_interface()
    ui.start()


if __name__ == "__main__":
    main()
