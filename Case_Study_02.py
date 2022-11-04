import json
filename = 'pos_0_t_png.json'
filename2 = 'pos_10010.png.json'
f = open(filename, 'r')
f2 = open(filename2, 'r')
data_1 = json.load(f)
data_2 = json.load(f2)
data_1['objects'].insert(0, data_2['objects'][0])
for i in range(len(data_1['objects'])):
        data_1['objects'][i]['classTitle'] = "car"
data_1['objects'][len(data_1['objects'])-1]['classTitle'] = "number"
with open("Combined_test_pos_10010.png.json", "a") as outfile:
    json.dump(data_1, outfile, indent = 4)