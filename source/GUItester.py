#Written by Braedon Kimball,bmk228
import unittest
from cmdapp import BMI_Retirement

class TestBMICalculations(unittest.TestCase):

    def test_underweight(self):
        br = BMI_Retirement()
        br.bmi(120, 72)
        self.assertEqual(br.cat, 'Underweight')
    def test_normal(self):
        br = BMI_Retirement()
        br.bmi(180, 72)
        self.assertEqual(br.cat, 'Normal')
    def test_obese(self):
        br = BMI_Retirement()
        br.bmi(300, 72)
        self.assertEqual(br.cat, 'Obese')
    def test_overweight(self):
        br = BMI_Retirement()
        br.bmi(215, 73)
        self.assertEqual(br.cat, 'Overweight')
    def test_inputweight(self):
        br = BMI_Retirement()
        br.bmi(300, 68)
        self.assertIs(br.wflag, True)
    def test_inputheight(self):
        br = BMI_Retirement()
        br.bmi(300, 80)
        self.assertIs(br.hflag, True)
    

class TestRetirement(unittest.TestCase):

    def test_alive(self): #Ensure that the age cap of 100 is met
        br = BMI_Retirement()
        br.retirement(25, 100000, 0.25, 2000000)
        self.assertIs(br.flag, True)
         
    def test_real_percentage(self):
        br = BMI_Retirement()
        br.retirement(25, 100000, 0.9, 2000000)
        self.assertIs(br.pflag, True) #if pflag is true, then the percentage is between [0.0, 1.0]

    def test_reasonable_income(self):
        br = BMI_Retirement()
        br.retirement(25, 10, 0.25, 2000000)
        self.assertIs(br.sflag, True) #if sflag is true, then the salary is in the range (0, 500,000]

    def test_reasonable_startage(self):
        br = BMI_Retirement()
        br.retirement(12, 500, 1, 5000)
        self.assertIs(br.aflag, True)

    def test_reasonable_inputs(self):
        br = BMI_Retirement()
        br.retirement(32, 45000, 0.6, 1200000) #Ensure that all inputs are reasonable based on the defined acceptable ranges. 
        self.assertIs(br.flag, True)
        self.assertIs(br.pflag, True)
        self.assertIs(br.sflag, True)

if __name__ == "__main__":
    unittest.main()