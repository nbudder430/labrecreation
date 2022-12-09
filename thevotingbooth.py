from tkinter import *
import csv

other_candidates = {"john": 0, "jane": 0}

class GUI:
    def __init__(self, window) -> None:
        """
        In charge of creating the GUI
        :param window: Window of the GUI Application
        """
        self.window = window
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text="It's Voting Day!", bg= "BLUE", fg="WHITE")
        self.label_name.pack(padx=0, side='left')
        self.frame_name.pack(pady=25)
        self.label_name.config(font=('Helvetica bold', 25, "bold"))

        self.frame_info = Frame(self.window)
        self.label_info = Label(self.frame_info, text="Who will your candidate be?")
        self.label_info.pack(padx=0, side='left')
        self.frame_info.pack(pady=10)
        self.label_info.config(font=('Helvetica bold', 12, "italic"))

        self.frame_lines1 = Frame(self.window)
        self.label_lines1 = Label(self.frame_lines1,
                                  text='|----------------------------------------------------------------------|',
                                  fg="RED")
        self.label_lines1.pack(padx=0, side='left')
        self.frame_lines1.pack(pady=5)

        self.frame_vote = Frame(self.window)
        self.label_vote = Label(self.frame_vote, text='')
        self.vote_1 = IntVar()
        self.vote_1.set(0)
        self.vote_John = Radiobutton(self.frame_vote, text='John', font=('Times', 15), variable=self.vote_1, value=0)
        self.vote_Jane = Radiobutton(self.frame_vote, text='Jane', font=('Times', 15), variable=self.vote_1, value=1)
        self.vote_other = Radiobutton(self.frame_vote, text='Other', font=('Times', 15), variable=self.vote_1, value=2)
        self.entry_other = Entry(self.frame_vote)
        self.label_vote.pack(padx=0, side='left')
        self.vote_John.pack(padx=12, side='left')
        self.vote_Jane.pack(padx=12, side='left')
        self.vote_other.pack(padx=12, side='left')
        self.entry_other.pack(side = "right")
        self.frame_vote.pack(pady=5)

        self.frame_lines2 = Frame(self.window)
        self.label_lines2 = Label(self.frame_lines2,
                                  text='|----------------------------------------------------------------------|',
                                  fg= "RED")
        self.label_lines2.pack(padx=0, side='left')
        self.frame_lines2.pack(pady=5)

        self.frame_vote = Frame(self.window)
        self.button_save = Button(self.frame_vote, text='FINALIZE VOTE', command=self.clicked,height= 2, width=20)
        self.button_save.pack()
        self.frame_vote.pack(pady=15)

        self.frame_finish = Frame(self.window)
        self.button_finish = Button(self.frame_finish, text='Finish Voting', command=self.clicked_finish,height= 2, width=20)
        self.button_finish.pack()
        self.frame_finish.pack(pady=15)

    def clicked(self) -> None:
        """
        Function to get votes after submitting votes
        :return: None
        """
        global other_candidates
        submission = self.entry_other.get()
        if self.vote_1.get() == 0:
            other_candidates["john"] += 1
        elif self.vote_1.get() == 1:
            other_candidates["jane"] += 1
        elif self.vote_1.get() == 2:
            other = self.entry_other.get()
            try:
                if other is not str:
                    pass
            except TypeError:
                self.window.quit()
                raise TypeError("Only strings are allowed")
            if other is None:
                pass
            elif other not in other_candidates:
                other_candidates[other] = 1
            else:
                other_candidates[other] += 1
        self.entry_other.delete(0, END)
        self.vote_1.set(0)

    def clicked_finish(self) -> None:
        """
        Function that finishes voting, closes the GUI, and write the csv file
        :return: None
        """
        header = ["name", "tally"]
        with open('votes.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)
            for key, value in other_candidates.items():
                writer.writerow([key, value])
        self.window.quit()
