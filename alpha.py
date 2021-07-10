#inport modules
from selenium import webdriver
import os.path
import time
import json
from colorama import Fore
import pyfiglet

#make a list for links
files=[]

#print welcome message
print(Fore.BLUE+pyfiglet.figlet_format("WELCOME\nALPHA v1.0"))


#get link videos channel youtube
input_driver=str(input("Videos Channel URL:\n"))
#get a file for save
file_name=str(input("Enter Your File Will Be Saved:\n"))

#make a loop for your file name
p=0
while p<1:
    #conds for exist files
    if os.path.exists(f"{file_name}.json"):
        print("Your File Is Exists Make Another Name :)")
        file_name=str(input("Enter Your File Will Be Saved:\n"))
    else:
        #drivers
        #if you use linux make this
        #./chromedriver
        driver=webdriver.Chrome("./chromedriver")
        driver.get(input_driver)
        p+=1

#time for scroll on the bottom of youtube
print("You Have 15 Second Time To Scroll Videos To End :)")

time.sleep(15)

#fine <a></a> elements
links=driver.find_elements_by_css_selector('a')

#a loop for links in links variable
for link in links:
    #add (href) attribute to the files list
    files.append(link.get_attribute("href"))

#open the file json and import links to the json
with open(f"{file_name.lower()}.json","w") as file:
    file.write(json.dumps(files,indent=4))

#end message :)
print(Fore.CYAN+"End :), Thanks For Using Alpha")
print(Fore.GREEN+"Writed By Meti.py")
