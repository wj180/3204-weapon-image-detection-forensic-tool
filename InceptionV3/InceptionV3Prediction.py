from imageai.Prediction import ImagePrediction
from imageai.Prediction.Custom import CustomImagePrediction
import os.path, time
import sys
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def weaponResult(image_list):
    execution_path = os.getcwd()

    now = datetime.now()
    start_time = now.strftime("%H:%M:%S")
    print("Start Time =", start_time)

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
    prediction.setModelPath(model_path=os.path.join(execution_path, "model_ex-035_acc-0.987719.h5"))
    prediction.setJsonPath(model_json=os.path.join(execution_path, "model_class.json"))
    # prediction.setModelTypeAsResNet()
    prediction.setModelTypeAsInceptionV3()
    # prediction.setModelTypeAsDenseNet()
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
                    print(tail + " : " + "Not a weapon")
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

def genPieChart(item_list):
    # Creating dataset 
    items = ["ammunition", "grenade", "gun", "non-weapon", "pistol", "revolver", "rifle", "rocket_launcher", "shotgun", "uzi"] 
      
    data = item_list 
      
    colors = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey']
    # percent = 100.*data/data.sum()

    patches, texts = plt.pie(data, colors=colors, startangle=90, radius=1.2)
    labels = ['{0} - {1:1}'.format(i,j) for i,j in zip(items, data)]

    # sort_legend = True
    # if sort_legend:
        # patches, labels, dummy =  zip(*sorted(zip(patches, labels, data), key=lambda items: items[2], reverse=True))

    plt.legend(patches, labels, loc='best', bbox_to_anchor=(-0.1, 1.), fontsize=8)
    plt.savefig('piechart.png', bbox_inches='tight')

def genBarChart(weapon_type_list, weapon_acc_list):
    # Plot the bar graph
    plot = plt.bar(weapon_type_list, weapon_acc_list)
     
    # Add the data value on head of the bar
    for value in plot:
        height = value.get_height()
        plt.text(value.get_x() + value.get_width()/2.,
                 1.002*height,'%d' % int(height), ha='center', va='bottom')
     
    # Add labels and title
    plt.title("Bar Chart")
    plt.xlabel("Year")
    plt.ylabel("Unit")
 
    # Display the graph on the screen
    plt.show()
    
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
    endtime = datetime.now()
    end_time = endtime.strftime("%H:%M:%S")
    print("End Time =", end_time)

if __name__ == "__main__":
	main()