import json
filename = 'pos_10010.png.json'
f = open(filename, 'r')
data = json.load(f)
list = []
for i in range(len(data['objects'])) :
    for j in range(len(data['objects'][i]['tags'])):
        list.append((data['objects'][i]['tags'][j]['name'],data['objects'][i]['tags'][j]['value']))
formatted_json = [{
    "dataset_name": filename,
        "image_link": "",
        "annotation_type": "image",
        "annotation_objects": {
            "vehicle": {
                "presence": 0,
                "bbox": []
            },
            "license_plate": {
                "presence": 0,
                "bbox": []
            }
        },
        "annotation_attributes": {
            "vehicle": {
                "Type": None,
                "Pose": None,
                "Model": None,
                "Make": None,
                "Color": None
            },
            "license_plate": {
                "Difficulty Score": None,
                "Value": None,
                "Occlusion": None
            }
        }
}]
dict = {}
for i in list :
    if i[0] == "Difficulty Score" :
        dict[i[0]] = 0
    else:
        dict[i[0]] = i[1]
V_bbox = []
L_bbox = []
for i in range(len(data['objects'])):
    for j in range(len(data['objects'][i]['points']['exterior'])):
        for k in range(len(data['objects'][i]['points']['exterior'][j])):
            if data['objects'][i]['classTitle'] == "Vehicle" :
                V_bbox.append(data['objects'][i]['points']['exterior'][j][k])
            else:
                L_bbox.append(data['objects'][i]['points']['exterior'][j][k])
for i in range(len(V_bbox)):
    formatted_json[0]['annotation_objects']['vehicle']['bbox'].append(V_bbox[i])
    formatted_json[0]['annotation_objects']['vehicle']['presence'] = 1
for i in range(len(L_bbox)):
    formatted_json[0]['annotation_objects']['license_plate']['bbox'].append(L_bbox[i])
    formatted_json[0]['annotation_objects']['license_plate']['presence'] = 1

for i in formatted_json[0]['annotation_attributes']['vehicle']:
    if i in dict:
        formatted_json[0]['annotation_attributes']['vehicle'][i] = dict[str(i)]
for i in formatted_json[0]['annotation_attributes']['license_plate']:
    if i in dict:
        formatted_json[0]['annotation_attributes']['license_plate'][i] = dict[i]
    if i == 'Occlusion' and data['objects'] == 2 :
        formatted_json[0]['annotation_attributes']['license_plate'][i] = 0
with open("formatted_test_pos_10010.png.json", "a") as outfile:
    json.dump(formatted_json, outfile, indent = 4)