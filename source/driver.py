from math import ceil
# Written by Braedon Kimball (bmk228) for Software Quality Assurance

def bmi(w, h):
	# w is weight, h is height
	wflag = False
	hflag = False
	if w >= 50 and w <= 650:
		wflag = True
	if h >= 36 and h <= 96:
		hflag = True
	h2 = h*h
	cat = 'Default'
	# calculate bmi by dividing weight in pounds (lb) by height in inches (in) squared and multiplying by a conversion
	# factor of 703 https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html
	b = round(float((w/h2) * 703), 2)
	out = ("For a weight of " + str(w) + "lbs and a height of " + str(h) + "in your BMI is: " + str(b))
	if b <= 18.5:
		#print("Category: Underweight. \n")
		cat = 'Underweight'
	elif b >= 25 and b <= 29.9:
		#print("Category: Overweight. \n")
		cat = 'Overweight'
	elif b >= 18.51 and b <= 24.9:
		#print("Category: Normal Weight. \n")
		cat = 'Normal'
	elif b >= 30.0:
		#print("Category: Obese. \n")
		cat = 'Obese'
	return cat, out, wflag, hflag

def retirement(age, salary, percentsaved, savgoal):
	# savings per year = (salary * %saved) * 1.35
	spy = (salary * percentsaved) * 1.35
	# year til goal = ceiling of savings goal / spy
	ytg = ceil(savgoal/spy)
	# age when goal is met
	goalage = age + ytg
	# flags to ensure that testing assertions work
	flag = False  # goal age flag
	pflag = False  # percentage flag
	sflag = False  # salary flag
	aflag = False  # Starting age flag
	if goalage <= 100:
		flag = True
	if percentsaved <= 1.0 and percentsaved >= 0.0:
		pflag = True
	if salary <= 500000 and salary > 0:
		sflag = True
	if age < 100 and age > 0:
		aflag = True

	message = ("Age until savings goal is met: " + str(goalage))
	return message, flag, pflag, sflag, aflag

