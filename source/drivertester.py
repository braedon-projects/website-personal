#Written by Braedon Kimball,bmk228
import unittest
from driver import bmi, retirement

class TestBMICalculations(unittest.TestCase):

    def test_underweight(self):
        cat, out, wflag, hflag = bmi(120, 72)
        self.assertEqual(cat, 'Underweight')
    def test_normal(self):
        cat, out, wflag, hflag = bmi(180, 72)
        self.assertEqual(cat, 'Normal')
    def test_obese(self):
        cat, out, wflag, hflag = bmi(300, 72)
        self.assertEqual(cat, 'Obese')
    def test_overweight(self):
        cat, out, wflag, hflag = bmi(215, 73)
        self.assertEqual(cat, 'Overweight')
    def test_inputweight(self):
        cat, out, wflag, hflag = bmi(300, 68)
        self.assertIs(wflag, True)
    def test_inputheight(self):
        cat, out, wflag, hflag = bmi(300, 80)
        self.assertIs(hflag, True)
    

class TestRetirement(unittest.TestCase):

    def test_alive(self): #Ensure that the age cap of 100 is met
        m, flag, pflag, sflag, aflag = retirement(25, 100000, 0.25, 2000000)
        self.assertIs(flag, True)
         
    def test_real_percentage(self):
        m, flag, pflag, sflag, aflag = retirement(25, 100000, 0.9, 2000000)
        self.assertIs(pflag, True) #if pflag is true, then the percentage is between [0.0, 1.0]

    def test_reasonable_income(self):
        m, flag, pflag, sflag, aflag = retirement(25, 10, 0.25, 2000000)
        self.assertIs(sflag, True) #if sflag is true, then the salary is in the range (0, 500,000]

    def test_reasonable_startage(self):
        m, flag, pflag, sflag, aflag = retirement(12, 500, 1, 5000)
        self.assertIs(aflag, True)

    def test_reasonable_inputs(self):
        m, flag, pflag, sflag, aflag = retirement(32, 45000, 0.6, 1200000) #Ensure that all inputs are reasonable based on the defined acceptable ranges. 
        self.assertIs(flag, True)
        self.assertIs(pflag, True)
        self.assertIs(sflag, True)

if __name__ == "__main__":
    unittest.main()