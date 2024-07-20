from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from bot.config import SITE_URL
import re
import time
import pandas as pd

myJobs = []

def scrape_site(url, jobSearchQuery):
  #set up driver
  driver = webdriver.Chrome()
  #open site
  driver.get(url)

  #let page load
  driver.implicitly_wait(10)

  #get the page and make it nice for the others
  html = driver.page_source
  soup = BeautifulSoup(html, "html.parser")

  #iniitialise myJobs which is list with all the jobs

  
  #get and send text to job serach bar
  job_searchbar = driver.find_element(By.CSS_SELECTOR, "input#text-input-what")
  job_searchbar.send_keys(jobSearchQuery +Keys.RETURN)

  #get and send text to location serach bar
  """ location_searchbar = driver.find_element(By.CSS_SELECTOR, "input#text-input-where")
  location_searchbar.send_keys("Oslo" ) """
   #press SEARCH btn
  """   search_button = driver.find_element(By.CSS_SELECTOR, "button.yosegi-InlineWhatWhere-primaryButton")
    search_button.click() """

  #get all jobs container
  while True:
    try: 
      jobList= driver.find_elements(By.CSS_SELECTOR, "div.slider_container")
      for job in jobList:
        #title
          job_title = job.find_element(By.CSS_SELECTOR, "h2.jobTitle>a>span").text

        #date published
          date_published = job.find_element(By.CSS_SELECTOR,  "span[data-testid='myJobsStateDate']").text

        #link
          link = job.find_element(By.CSS_SELECTOR, "h2.jobTitle>a").get_attribute("href")

        #company
          company =  job.find_element(By.CSS_SELECTOR, "span[data-testid='company-name']").text
      

        #location
          location = job.find_element(By.CSS_SELECTOR,'div[data-testid="text-location"]').text

          myJobs.append({
          "Job Title" : job_title,
          "Company" : company,
          "Location" : location,
          "Date Published" : date_published.replace("Publisert for", ""),
           "Link" : link,
        })


        #get newt button
      next_button = driver.find_element(By.CSS_SELECTOR,   "a[data-testid='pagination-page-next']").get_attribute("href")
      print(next_button)
      driver.get( next_button)
      time.sleep(2)
    except:
      break
#close driver after everything
  driver.quit()
  save_to_excel(myJobs, "myJobs.xlsx")


def makeFile():
  with open("jobs.txt", "w" ) as file:
      for index, job in enumerate(myJobs):
        file.write(
f'''
{index+1}. Job Name : {job["Job Title"]}
  Job Link : {job["Link"]}
  Location :  {job["Location"]}
  Company : {job["Company"]}
  Date Published : {job["Date Published"]} 

''')
        
def save_to_excel(data, filename):
   #create data frame
   df = pd.DataFrame(data, )

   #write data frame to excel file
   df.to_excel(filename, index = False,  engine='openpyxl')



   





  
