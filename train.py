# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:27:51 2019

@author: MX
"""

import os
import csv

def create_folders():

    dataset_path = 'dataset'
    train_data = 'train'

    
    files = os.listdir(train_data)
    
    #print(os.getcwd())
    
    with open('labels.csv', newline='') as csvFile:
        reader = csv.reader(csvFile, delimiter = ' ', quotechar='|') #reads all rows from the CSV file
        for row in reader: #Goes through all the rows on the data from the CSV      
            for file in files: #reads files from the training dataset
                print(file)
                if row[0].split(',')[0] == file.split('.')[0]: #Compares the ID's from the dataset and CSV
                    folder_name = str(row[0].split(',')[1])
                    os.makedirs(dataset_path+'/'+folder_name, exist_ok=True) #creates folder according to the breed name
                    source = train_data + '/' +  file 
                    destination = dataset_path+'/'+folder_name+'/'+file
                    os.rename(source, destination) #Moves file from training data to created folder
                    print("Dataset folders successfully created by breed name and copied all images in corresponding folders")


#main function
                    
def main():
    create_folders()
    
if __name__ == "__main__":
    main()