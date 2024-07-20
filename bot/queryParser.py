import argparse

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