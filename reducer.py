
import sys
# Input Key: mapper output key
# Input Value: mapper output value
test = dict()
for line in sys.stdin:
    if line.count("(")==1:
        # Output Key: Key_name = "region name" or "country name" or "type"
        # Output Value: the total profit
        # Get the region or country or type total profit
        key_name = line.replace("('", "").replace("'", '').split(",")[0]
        profie_val = line.replace("('", "").replace("'", '').replace(")\n", '').split(",")[1]
        if key_name in test.keys():
            test[key_name] = float(test[key_name]) + float(profie_val)
        else:
            test[key_name] = float(profie_val)
    else:
        # Output Key: type and the sales channel
        # Output Value: the total units sold
        # Get the type_item name and the unit sold by sales channel
        type_item_name = line.replace("('", "").replace("'", '').split(",")[0]
        salesChannel = line.replace("('", "").replace("'", '').replace(")\n", '').split(",")[1]
        unitsSold = line.replace("'", "").replace("))\n", '').split(",")[2]
        if (type_item_name,salesChannel) in test.keys():
            test[(type_item_name,salesChannel)] = float(test[(type_item_name,salesChannel)]) + float(unitsSold)
        else:
            test[(type_item_name,salesChannel)] = float(unitsSold)
print(test)









