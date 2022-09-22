from string import ascii_lowercase
from selenium import webdriver
from parseFile import *
import keyboard 
import os

# 200, 9/22/22
def search(companies):
    i = 200
    browser = webdriver.Chrome('chromedriver')
    while True:
        try:  
            if keyboard.is_pressed(' '):   
                for j in range(1):
                    browser.get("https://www.google.com/search?q=" + companies[i] + " software intern" + "&start=" + str(j))
                i+=1
                print(i)
            if i == len(companies):
                break
        except:
            break

def main():
    # This parses the initial files 
    # for c in ascii_lowercase:
    #     firstParse(c)

    # Loads parsed file data into a list of lists for more usability
    cwd = os.getcwd()
    companies = []
    
    print(__file__)
    for l in ascii_lowercase:
        with open( cwd + '\\parsed\\'+  l + '.txt', 'r') as in_f:
            lines = in_f.readlines()
            for j in range(len(lines)):
                lines[j] = lines[j].replace('\n','')
            companies += lines

    # Search automation
    search(companies)

if __name__ == "__main__":
    main()

