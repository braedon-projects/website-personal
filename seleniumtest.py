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
    driver.get("http://127.0.0.1:4321/getbmi")


cal=0

cal+=bmi("120","72","For a weight of 120.0lbs and a height of 72.0in your BMI is: 16.27 Underweight")
#time.sleep(timer)
cal+=bmi("180","72","For a weight of 180.0lbs and a height of 72.0in your BMI is: 24.41 Normal")
#time.sleep(timer)
cal+=bmi("300","72","For a weight of 300.0lbs and a height of 72.0in your BMI is: 40.68 Obese")
#time.sleep(timer)
cal+=bmi("215","73","For a weight of 215.0lbs and a height of 73.0in your BMI is: 28.36 Overweight")

if(cal<1):
    file1.write("All BMI Tests Passed\n")
else:
    file1.write(str(cal)+" BMI Tests Failed\n")
file1.close()

file1=open("log.txt","a")
cal=0
driver.get("http://127.0.0.1:4321/retirement")

cal+=retire("25", "100000", "0.25", "200000",1," True")
cal+=retire("25", "100000", "0.9", "2000000",2," True")
cal+= retire("12", "500", "1", "5000",3, " True")

cal+= retire("32", "45000", "0.6", "1200000",4, " True")

if(cal<1):
    file1.write("All Retire Tests Passed")
else:
    file1.write(str(cal)+" Retire Tests Failed")
file1.close()



