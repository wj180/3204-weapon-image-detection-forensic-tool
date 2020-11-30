from imageai.Prediction import ImagePrediction
from imageai.Prediction.Custom import CustomImagePrediction
import os.path, time
import sys
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def weaponResult(image_list):
    execution_path = os.getcwd()

    weapon_found = []
    weapon_found_acc = []
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
                    # print("Created: %s" % time.ctime(os.path.getctime(image_path)))
                    print(tail)
                    print(line)
                    if eachPrediction == "ammunition":
                        item_am += 1
                    elif eachPrediction == "grenade":
                        item_gre += 1
                    elif eachPrediction == "gun":
                        item_gun += 1
                    elif eachPrediction == "pistol":
                        item_pis += 1
                    elif eachPrediction == "revolver":
                        item_rev += 1
                    elif eachPrediction == "rifle":
                        item_rif += 1
                    elif eachPrediction == "rocket_launcher":
                        item_roc += 1
                    elif eachPrediction == "shotgun":
                        item_sho += 1
                    elif eachPrediction == "uzi":
                        item_uzi += 1
                else:
                    print(tail)
                    print("Not a weapon")
                    item_non += 1
                count += 1
                break
    
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
        for item in item_lists:
            if item in line:
                if "ammunition_count" in item:
                    new_content = line.replace("ammunition_count", str(item_am))
                elif "grenade_count" in item:
                    new_content = line.replace("grenade_count", str(item_gre))
                elif "gun_count" in item:
                    new_content = line.replace("gun_count", str(item_gun))
                elif "pistol_count" in item:
                    new_content = line.replace("pistol_count", str(item_pis))
                elif "revolver_count" in item:
                    new_content = line.replace("revolver_count", str(item_rev))
                elif "rifle_count" in item:
                    new_content = line.replace("rifle_count", str(item_rif))
                elif "rocket_launcher_count" in item:
                    new_content = line.replace("rocket_launcher_count", str(item_roc))
                elif "shotg_count" in item:
                    new_content = line.replace("shotg_count", str(item_sho))
                elif "uzi_count" in item:
                    new_content = line.replace("uzi_count", str(item_uzi))
                elif "non-weapon_count" in item:
                    new_content = line.replace("non-weapon_count", str(item_non))
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
    image_list = findDir("D:/VM Shared/3204/dashboard/comparison")
    weaponResult(image_list)

if __name__ == "__main__":
	main()