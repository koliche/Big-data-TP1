
import sys

test = dict()


for line in sys.stdin:
    if line.count("(")==1:
        # Get the region name and the profit
        region_name = line.replace("('", "").replace("'", '').split(",")[0]
        profie_val = line.replace("('", "").replace("'", '').replace(")\n", '').split(",")[1]
        if region_name in test.keys():
            test[region_name] = float(test[region_name]) + float(profie_val)
        else:
            test[region_name] = float(profie_val)
    else:
        # Get the type_item name and the profit
        type_item_name = line.replace("('", "").replace("'", '').split(",")[0]
        salesChannel = line.replace("('", "").replace("'", '').replace(")\n", '').split(",")[1]
        unitsSold = line.replace("'", "").replace("))\n", '').split(",")[2]
        if (type_item_name,salesChannel) in test.keys():
            test[(type_item_name,salesChannel)] = float(test[(type_item_name,salesChannel)]) + float(unitsSold)
        else:
            test[(type_item_name,salesChannel)] = float(unitsSold)

print(test)









