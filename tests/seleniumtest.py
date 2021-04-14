from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #must pip install webdriver_manager
from selenium.webdriver.common.keys import Keys
import time


file1=open("log.txt","w")

def bmi(sweight,sheight,output):
    weight= driver.find_element_by_xpath(".//*[@name='weight']")
    weight.send_keys(sweight)

    heigh= driver.find_element_by_xpath(".//*[@name='height']")
    heigh.send_keys(sheight)

    sub = driver.find_element_by_xpath(".//*[@name='submit']")
    sub.click()

    message=driver.find_element_by_xpath(".//*[@class='text']").text
    
    if(message == output):
        
        return 0
    
    return 1

def retire(age_input, salary_input, percentsaved_input, savgoal_input,flag,value):
    age= driver.find_element_by_xpath(".//*[@name='age']")
    age.send_keys(age_input)

    sal= driver.find_element_by_xpath(".//*[@name='salary']")
    sal.send_keys(salary_input)
    
    persaved=driver.find_element_by_xpath(".//*[@name='percentsaved']")
    persaved.send_keys(percentsaved_input)

    sg= driver.find_element_by_xpath(".//*[@name='savingsgoal']")
    sg.send_keys(savgoal_input)

    sub = driver.find_element_by_xpath(".//*[@name='submit']")
    sub.click()

    message=driver.find_element_by_xpath(".//*[@class='text']").text

    message=message.split(",")

    if(flag==1):
        if(message[1]==value):
            return 0
        else:
            return 1

    elif(flag==2):
        if(message[2]==value):
            return 0
        else:
            return 1
    elif(flag==3):
        if(message[3]==value):
            return 0
        else:
            return 1
    else:
        if(message[3]==value):
            if(message[2]==value):
                if(message[1]==value):
                    return 0
        return 1
    

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("http://127.0.0.1:4321")

sub = driver.find_element_by_xpath(".//*[@name='getbmi']")
sub.click()
cal=0

test=bmi("120","72","For a weight of 120.0lbs and a height of 72.0in your BMI is: 16.27 Underweight")
cal+=test
if(test==1):
    file1.write("Failed BMI Underweight test\n") 

test=bmi("180","72","For a weight of 180.0lbs and a height of 72.0in your BMI is: 24.41 Normal")
cal+=test
if(test==1):
    file1.write("Failed BMI Normal test\n") 

test=bmi("300","72","For a weight of 300.0lbs and a height of 72.0in your BMI is: 40.68 Obese")
cal+=test
if(test==1):
    file1.write("Failed BMI Obese test\n")

test=bmi("215","73","For a weight of 215.0lbs and a height of 73.0in your BMI is: 28.36 Overweight")
cal+=test
if(test==1):
    file1.write("Failed BMI Overweight test\n") 

if(cal<1):
    file1.write("All BMI Tests Passed\n")
file1.close()



file1=open("log.txt","a")
cal=0
driver.get("http://127.0.0.1:4321/")
sub = driver.find_element_by_xpath(".//*[@name='retirement']")
sub.click()

test=retire("25", "100000", "0.25", "200000",1," True")
cal+=test
if(test==1):
    file1.write("Failed Retirement test to ensure that the age cap of 100 is met\n")

test=retire("25", "100000", "0.9", "2000000",2," True")
cal+=test
if(test==1):
    file1.write("Failed Retirement test to ensure that the percentage is between [0.0, 1.0]\n")
    
test= retire("12", "500", "1", "5000",3, " True")
cal+=test
if(test==1):
    file1.write("Failed Retirement test to ensure that the salary is in the range (0, 500,000]\n")


test= retire("32", "45000", "0.6", "1200000",4, " True")
cal+=test
if(test==1):
    file1.write("Failed Retirement test to ensure that all inputs are reasonable based on the defined acceptable ranges\n")

if(cal<1):
    file1.write("All Retirement Tests Passed")

file1.close()
