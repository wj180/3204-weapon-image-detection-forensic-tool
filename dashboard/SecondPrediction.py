from imageai.Prediction import ImagePrediction
from imageai.Prediction.Custom import CustomImagePrediction
import os.path, time
import sys
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import datetime

def weaponResult(image_list, drive_name):
    execution_path = os.getcwd()
    weapon_acc_list = []
    weapon_found = []
    weapon_found_acc = []
    dates = []
    item_am = 0
    item_gre = 0
    item_gun = 0
    item_non = 0
    item_pis = 0
    item_rev = 0
    item_rif = 0
    item_roc = 0
    item_sho = 0
    item_uzi = 0
    
    prediction = CustomImagePrediction()
    prediction.setModelPath(model_path=os.path.join(execution_path, "model_ex-031_acc-0.980000.h5"))
    prediction.setJsonPath(model_json=os.path.join(execution_path, "model_class.json"))
    # prediction.setModelTypeAsResNet()
    # prediction.setModelTypeAsInceptionV3()
    prediction.setModelTypeAsDenseNet()
    prediction.loadModel(num_objects=10)
    
    for image_path in image_list:
        predictions, probabilities = prediction.predictImage(image_path, result_count=5 )
        count = 1
        for eachPrediction, eachProbability in zip(predictions, probabilities):
            line = count , " : " , eachPrediction , " : " , eachProbability
            if count == 1:
                head, tail = os.path.split(image_path)
                if (eachProbability > 80) and (eachPrediction != "non-weapon"):                    
                    
                    # weapon_found.append(tail + ' - ' + eachPrediction)
                    # weapon_found_acc.append(eachProbability)
                    cdate = datetime.datetime.strptime(time.ctime(os.path.getctime(image_path)), "%c")
                    cdate = str(cdate).split(' ')[0]
                    dates.append(cdate)
                    dates.sort()
                    date_count = {i:dates.count(i) for i in dates}                    
                    # print("Created: " + cdate) 
                    # print(tail)
                    # print(line)
                    if eachPrediction == "ammunition":
                        item_am += 1
                        weapon_acc_list.append('{ y: ' + str(int(eachProbability)) + ', label: "' + tail + ' - ' + 'ammunition"}')
                    elif eachPrediction == "grenade":
                        item_gre += 1
                        weapon_acc_list.append('{ y: ' + str(int(eachProbability)) + ', label: "' + tail + ' - ' + 'grenade"}')
                    elif eachPrediction == "gun":
                        item_gun += 1
                        weapon_acc_list.append('{ y: ' + str(int(eachProbability)) + ', label: "' + tail + ' - ' + 'gun"}')
                    elif eachPrediction == "pistol":
                        item_pis += 1
                        weapon_acc_list.append('{ y: ' + str(int(eachProbability)) + ', label: "' + tail + ' - ' + 'pistol"}')
                    elif eachPrediction == "revolver":
                        item_rev += 1
                        weapon_acc_list.append('{ y: ' + str(int(eachProbability)) + ', label: "' + tail + ' - ' + 'revolver"}')
                    elif eachPrediction == "rifle":
                        item_rif += 1
                        weapon_acc_list.append('{ y: ' + str(int(eachProbability)) + ', label: "' + tail + ' - ' + 'rifle"}')
                    elif eachPrediction == "rocket_launcher":
                        item_roc += 1
                        weapon_acc_list.append('{ y: ' + str(int(eachProbability)) + ', label: "' + tail + ' - ' + 'rocket_launcher"}')
                    elif eachPrediction == "shotgun":
                        item_sho += 1
                        weapon_acc_list.append('{ y: ' + str(int(eachProbability)) + ', label: "' + tail + ' - ' + 'shotgun"},')
                    elif eachPrediction == "uzi":
                        item_uzi += 1
                        weapon_acc_list.append('{ y: ' + str(int(eachProbability)) + ', label: "' + tail + ' - ' + 'uzi"}')
                else:
                    print(tail)
                    print("Not a weapon" + str(int(eachProbability)))
                    item_non += 1
                count += 1
                break
    
    print(type(date_count))
    date_content = '{ x: 1, y: 0, label: "Empty"}'
    date_content_list = []
    x_counter = 1
    if date_count:
        for date_c in date_count:
            print(date_count[date_c])
            print(date_c)
            dateline = '{ x: ' + str(x_counter) + ', y: ' + str(date_count[date_c]) + ', label: "' + date_c + '"}'
            date_content_list.append(dateline)
            x_counter += 1
    
    item_list = []
    item_list.append(item_am)
    item_list.append(item_gre)
    item_list.append(item_gun)
    item_list.append(item_non)
    item_list.append(item_pis)
    item_list.append(item_rev)
    item_list.append(item_rif)
    item_list.append(item_roc)
    item_list.append(item_sho)
    item_list.append(item_uzi)
    
    # Using readlines() 
    new_contents = []
    item_lists = ["ammunition_count", "grenade_count", "gun_count", "pistol_count", "revolver_count", "rifle_count", "rocket_launcher_count", "shotg_count", "uzi_count", "non-weapon_count"]

    file1 = open('index.html', 'r') 
    lines = file1.readlines()

    for line in lines:
        new_content = line
        
        if "placeholder" in line:
            new_content = ','.join(weapon_acc_list)
        
        if "drivename" in line:
            new_content = drive_name
        
        if "dateholder" in line:
            new_content = ','.join(date_content_list)
        
        for item in item_lists:
            if item in line:
                if item == "ammunition_count":
                    if item_am > 0:
                        new_content = line.replace("ammunition_count", str(item_am))
                    else:
                        new_content = ""
                elif item == "grenade_count":
                    if item_gre > 0:
                        new_content = line.replace("grenade_count", str(item_gre))
                    else:
                        new_content = ""
                elif item == "gun_count":
                    if item_gun > 0:
                        new_content = line.replace("gun_count", str(item_gun))
                    else:
                        new_content = ""
                elif item == "pistol_count":
                    if item_pis > 0:
                        new_content = line.replace("pistol_count", str(item_pis))
                    else:
                        new_content = ""
                elif item == "revolver_count":
                    if item_rev > 0:
                        new_content = line.replace("revolver_count", str(item_rev))
                    else:
                        new_content = ""
                elif item == "rifle_count":
                    if item_rif > 0:
                        new_content = line.replace("rifle_count", str(item_rif))
                    else:
                        new_content = ""
                elif item == "rocket_launcher_count":
                    if item_roc > 0:
                        new_content = line.replace("rocket_launcher_count", str(item_roc))
                    else:
                        new_content = ""
                elif item == "shotg_count":
                    if item_sho > 0:
                        new_content = line.replace("shotg_count", str(item_sho))
                    else:
                        new_content = ""
                elif item == "uzi_count":
                    if item_uzi > 0:
                        new_content = line.replace("uzi_count", str(item_uzi))
                    else:
                        new_content = ""
                elif item == "non-weapon_count":
                    if item_non > 0:
                        new_content = line.replace("non-weapon_count", str(item_non))
                    else:
                        new_content = ""
        new_contents.append(new_content)
       
    file1.close()
    file2 = open('indexnew.html', 'w')
    file2.writelines(new_contents)
    file2.close()
    
    
def findDir(directory):
    image_list = []
    for folder, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                fullPath = os.path.join(folder, file)
                image_list.append(fullPath)
                
    return image_list
                
def main():
    drive_name = "D:/Downloads/scrape/sample"
    image_list = findDir(drive_name)
    weaponResult(image_list, drive_name)

if __name__ == "__main__":
	main()