# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')



# test = dict()
#
# def ventReducer():
#     for line in sys.stdin:
#         # Get the region name and the profit
#         region_name = line.replace("('", "").replace("'", '').split(",")[0]
#         profie_val = line.replace("('", "").replace("'", '').replace(")\n", '').split(",")[1]
#         if region_name in test.keys():
#             test[region_name] = float(test[region_name]) + float(profie_val)
#         else:
#             test[region_name] = float(profie_val)
#     print(test)
#
# ventReducer()



# # Skip the Header of csv :
# file = sys.stdin
# next(file)
# def venteMapper(key_index):
#     for line in file:
#         # Split words by
#         words = line.split(",")
#         # Get region and profit
#         mapperKey = words[key_index]
#         profit = words[-1].replace('\n','')
#         # Return the Result tupls
#         print((mapperKey,profit))
#
# #Q1
# venteMapper(0)
# #Q2
# #venteMapper(1)
# #Q3
# #venteMapper(2)
