import unittest
from tkinter import messagebox, Tk

from TestTheGreatMorningScramble import TestGreatMorningScramble

suite = unittest.TestLoader().loadTestsFromTestCase(TestGreatMorningScramble)
result = unittest.TextTestRunner().run(suite)

if result.wasSuccessful():
    root = Tk()
    root.withdraw()
    messagebox.showinfo("Tests passed", "All tests have ran succesfully with no errors.")
else:
    root =Tk()
    root.withdraw()
    messagebox.showerror("Tests failed", "There has been a few errors please check the terminal.")