from bot.scraper import scrape_site
from bot.scraper import makeFile
from bot.config import SITE_URL
import argparse

def main():


  # create parser
  parser = argparse.ArgumentParser(description= "insert a searcgh qeury for job")

  #add argumet
  #parser.add_argument("name", type= str, help="Your name")
  parser.add_argument("job", type= str, help="Your job search query")

  #parse the argument
  args = parser.parse_args()

  #use the argumet
  jobSearchQuery = args.job
  #print(f"Hello , {args.job}")
  scrape_site(SITE_URL, jobSearchQuery)
  makeFile()

if __name__ == "__main__":
  main()