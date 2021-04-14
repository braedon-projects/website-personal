from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #must pip install webdriver_manager
from selenium.webdriver.common.keys import Keys
import time

path="http://127.0.0.1:4321/"

file1=open("log.txt","w")

def bmi(sweight,sheight,value,cat):
    weight= driver.find_element_by_xpath(".//*[@name='weight']")
    weight.send_keys(sweight)

    heigh= driver.find_element_by_xpath(".//*[@name='height']")
    heigh.send_keys(sheight)

    sub = driver.find_element_by_xpath(".//*[@name='submit']")
    sub.click()

    message=driver.find_element_by_xpath(".//*[@class='container text-center result']").text
    
    if value and cat in message:
        return 0, message
    
    return 1 , message

def retire(age_input, salary_input, percentsaved_input, savgoal_input,expected):
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

    message=driver.find_element_by_xpath(".//*[@class='container text-center result']").text
    
    if(expected!=message):
        return 1, message
    return 0, message
    

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(path)

sub = driver.find_element_by_xpath(".//*[@name='bmi']")
sub.click()
cal=0

# Underweight
expected="16.27 Underweight"
value, cat=expected.split(" ")
test=bmi("120","72",value,cat)
cal+=test[0]
if(test[0]==1):
    file1.write("Failed BMI Underweight test Expected: "+str(expected)+" Received: "+str(test[1])+"\n") 
#underWeight
expected="24.41 Normal"
value, cat=expected.split(" ")
test=bmi("180","72",value,cat)
cal+=test[0]
if(test[0]==1):
    file1.write("Failed BMI Normal test Expected: "+str(expected)+" Received: "+str(test[1])+"\n") 

expected="40.68 Obese"
value, cat=expected.split(" ")
test=bmi("300","72",value,cat)
cal+=test[0]
if(test[0]==1):
    file1.write("Failed BMI Obese test Expected: "+str(expected)+" Received: "+str(test[1])+"\n")

expected="28.36 Overweight"
value, cat=expected.split(" ")
test=bmi("215","73",value,cat)
cal+=test[0]
if(test[0]==1):
    file1.write("Failed BMI Overweight test Expected: "+str(expected)+" Received: "+str(test[1])+"\n") 

if(cal<1):
    file1.write("All BMI Tests Passed\n")
file1.close()



file1=open("log.txt","a")
cal=0
driver.get(path)
sub = driver.find_element_by_xpath(".//*[@class='container']")
sub.click()
sub = driver.find_element_by_xpath(".//*[@name='retirement']")
sub.click()

expected="Age until savings goal is met: 31.0"
test=retire("25", "100000", "0.25", "200000",expected)
cal+=test[0]
if(test[0]==1):
    file1.write("Failed Retirement test expected: "+expected+" Recieved: "+test[1]+"\n")


expected="Age until savings goal is met: 42.0"

test=retire("25", "100000", "0.9", "2000000",expected)
cal+=test[0]
if(test[0]==1):
    file1.write("Failed Retirement test expected: "+expected+" Recieved: "+test[1]+"\n")

expected="Age until savings goal is met: 20.0"
test= retire("12", "500", "1", "5000",expected)
cal+=test[0]
if(test[0]==1):
    file1.write("Failed Retirement test expected: "+expected+" Recieved: "+test[1]+"\n")


expected="Age until savings goal is met: 65.0"
test= retire("32", "45000", "0.6", "1200000",expected)
cal+=test[0]
if(test[0]==1):
    file1.write("Failed Retirement test expected: "+expected+" Recieved: "+test[1]+"\n")

if(cal<1):
    file1.write("All Retirement Tests Passed")

file1.close()



