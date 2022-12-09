from thevotingbooth import *


def main() -> None:
    """
    Function creates the window
    :return: None
    """
    window = Tk()
    window.title('The Voting Booth')
    window.geometry('400x420')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
