
import sys

test = dict()


for line in sys.stdin:
    # Get the region name and the profit
    region_name = line.replace("('", "").replace("'", '').split(",")[0]
    profie_val = line.replace("('", "").replace("'", '').replace(")\n", '').split(",")[1]
    if region_name in test.keys():
        test[region_name] = float(test[region_name]) + float(profie_val)
    else:
        test[region_name] = float(profie_val)
print(test)









