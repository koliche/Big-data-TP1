import sys
import argparse
# Create the Question number parameter :
parser = argparse.ArgumentParser()
parser.add_argument('--question_number', help='the number of the question to be displayed')
args = parser.parse_args()

question_number = args.question_number
# Skip the Header of csv :
file = sys.stdin
next(file)
def venteMapper(question_number):
    for line in file:
        # Split words by
        words = line.split(",")
        # Get region and profit
        mapperKey = words[question_number]
        profit = words[-1].replace('\n','')
        # Return the Result tupls
        print((mapperKey,profit))

def venteSoldMapper(question_number):
    for line in file:
        # Split words by ,
        words = line.split(",")
        # Get Type,Sales Channel and Units Sold
        mapperKey = words[2]
        salesChannwl = words[3].replace('\n','')
        unitsSold = words[8].replace('\n','')
        print ((mapperKey,(salesChannwl,unitsSold)))

if int(question_number) == 4 :
    # Question 4
    venteSoldMapper(int(question_number))
else:
    #Question 1,2,3
    venteMapper(int(question_number)-1)








