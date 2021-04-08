from math import ceil
# Written by Braedon Kimball (bmk228) for Software Quality Assurance

class BMI_Retirement:

	def bmi(self, w, h):
		# w is weight, h is height
		self.wflag = False
		self.hflag = False
		if w >= 50 and w <= 650:
			self.wflag = True
		if h >= 36 and h <= 96:
			self.hflag = True
		h2 = h*h
		self.cat = 'Default'
		# calculate bmi by dividing weight in pounds (lb) by height in inches (in) squared and multiplying by a conversion
		# factor of 703 https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html
		self.b = round(float((w/h2) * 703), 2)
		print("For a weight of " + str(w) + "lbs and a height of " + str(h) + "in your BMI is: " + str(self.b))
		if self.b <= 18.5:
			print("Category: Underweight. \n")
			self.cat = 'Underweight'
		elif self.b >= 25 and self.b <= 29.9:
			print("Category: Overweight. \n")
			self.cat = 'Overweight'
		elif self.b >=18.51 and self.b <= 24.9:
			print("Category: Normal Weight. \n")
			self.cat = 'Normal'
		elif self.b >= 30.0:
			print("Category: Obese. \n")
			self.cat = 'Obese'


	def retirement(self, age, salary, percentsaved, savgoal):
		# savings per year = (salary * %saved) * 1.35
		self.spy = (salary * percentsaved) * 1.35
		# year til goal = ceiling of savings goal / spy
		self.ytg = ceil(savgoal/self.spy)
		# age when goal is met
		self.goalage = age + self.ytg
		#flags to ensure that testing assertions work
		self.flag = False #goal age flag
		self.pflag = False #percentage flag
		self.sflag = False #salary flag
		self.aflag = False #Starting age flag
		if self.goalage <= 100:
			self.flag = True
		if percentsaved <= 1.0 and percentsaved >= 0.0:
			self.pflag = True    
		if salary <= 500000 and salary > 0:
			self.sflag = True
		if age < 100 and age > 0:
			self.aflag = True

		print("Age until savings goal is met: " + str(self.goalage))


def main():

	print("Welcome to the application! Options below: \n")
	x = 0
	br = BMI_Retirement()
	while x == 0:
		
		print("1: Calculate BMI \n2: Calculate Retirement\n3: Exit the program")
		var = input()
		
		if var == '1':
			w = float(input("Enter weight in pounds: "))
			h = float(input("Enter height in inches: "))

			br.bmi(w, h)

		elif var == '2':
			a = float(input("Enter age (between 0 and 100): "))
			s = float(input("Enter yearly salary between 0 and 500,000 in $usd: "))
			ps = float(input("Enter percentage saved (between 0.0 and 1.0): "))
			gs = float(input("Enter savings goal <2,000,000: "))
			br.retirement(a, s, ps, gs)
		
		elif var == '3':
			break
		
		else:
			print("Please input a valid option, either 1 or 2.\n")

	return


#main()
