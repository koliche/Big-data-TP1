import sys
# Skip the Header of csv :
file = sys.stdin
next(file)
def venteMapper(key_index):
    for line in file:
        # Split words by
        words = line.split(",")
        # Get region and profit
        mapperKey = words[key_index]
        profit = words[-1].replace('\n','')
        # Return the Result tupls
        print((mapperKey,profit))

#Q1
venteMapper(0)
#Q2
#venteMapper(1)
#Q3
#venteMapper(2)







