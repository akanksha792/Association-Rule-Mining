# -*- coding: utf-8 -*-
"""

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gk32v47Cf_1rYyjqAZwBrQqvN-GhU543
"""

#Import libraries
import pandas as pd
import numpy as np
import re
from google.colab import drive


def runner(path):

    train_data = "C:/Users/Akanksha/Desktop/Mtech/Mtech_Sem1/DMG/Assignments/DMG_ASSIGNMENT3/dataset/training.csv"

    test_data = path

    train_df=pd.read_csv(train_data)

    train_df

    columns=train_df.columns
    columns


    print(train_df.Elevation.unique())
    print(train_df.Aspect.unique())
    print(train_df.Slope.unique())
    print(train_df.Wilderness.unique())
    print(train_df.Soil_Type.unique())
    
    print(train_df.Hillshade_9am.unique())
    print(train_df.Hillshade_noon.unique())
    
    print(train_df.Horizontal_Distance_To_Hydrology.unique())
    print(train_df.Vertical_Distance_To_Hydrology.unique())
        
    print(train_df.Horizontal_Distance_To_Fire_Points.unique())
    print(train_df.Label.unique())
    

    train_df[:10]



    pathFile="C:/Users/Akanksha/Desktop/Mtech/Mtech_Sem1/DMG/Assignments/DMG_ASSIGNMENT3/dataset/r1.txt"
    file=open(pathFile)
    content=file.read()
    #content[1115:]
    
    rules=[]
    rule=""
    for ch in content:
        if(ch !='\n'):
            rule+=ch
        else:
            rules.append(rule)
            rule=""

    rules


    processed_rule=[]
    for string in rules:
        string=re.sub(r'[0-9]+[.]','',string)
        string=re.sub(r'[0-9]+[0-9]+','',string)
        string=string[:-9].strip()
        string=re.sub(r'[A-Za-z_]+[=]+','',string)
        processed_rule.append(string)

    processed_rule=processed_rule[46:]
    processed_rule

    # now dividing the processed rules into X=>Y
    processed_rule[0].partition('==>')

    x=[]
    y=[]
    c=0
    for string in processed_rule:
        x.append(string.partition('==>')[0].strip())
        y.append(string.partition('==>')[2].strip())
        # print(c)
        c=c+1

    # reading the test file and preprocess it
    test_data
    file=open(test_data)
    test_file=file.read()


    df_test=pd.read_csv(test_data)
    df_test2 = pd.read_csv(test_data)
    del df_test['id']
    del df_test['Horizontal_Distance_To_Hydrology']
    del df_test['Vertical_Distance_To_Hydrology']


    df_test


    # x[0],y[0]  they represents the first rule

    # dataframe is prepared
    # now we will take a rule and match it against the test-case provided

    #  'Elevation=elevation_ultra Hillshade_noon=hillnoon_min',

    r_no=1
    list_label_ans=[]
    for row in df_test.itertuples(index=True):
        # storing the elements of the row in a set
        # print(r_no)
        r_no+=1
        row_set=set()
        row_set.add(getattr(row, "Elevation"))
        row_set.add(getattr(row, "Aspect"))
        row_set.add(getattr(row, "Slope"))
        row_set.add(getattr(row, "Wilderness"))
        row_set.add(getattr(row, "Soil_Type"))
        row_set.add(getattr(row, "Hillshade_9am"))
        row_set.add(getattr(row, "Hillshade_noon"))
        row_set.add(getattr(row, "Horizontal_Distance_To_Fire_Points"))
        
        
          # print(row_set)
        max_count=-1
        temp_solution=""
        
        for i in range(len(x)):
            rule=x[i].split(' ')
            if  len(rule)<3:
                continue
            count=0  
            flag=True
            for elem in rule:
                if(elem not in row_set):
                    flag=False
                    break
                else:
                    count+=1
      
            if flag==True:
                if(count>max_count):
                    max_count=count
                    temp_solution=y[i] 
                    break
                
          # print(temp_solution)
        if(temp_solution==""):
            list_label_ans.append('ONE')
        else:
            list_label_ans.append(temp_solution)


    # print(temp_solution+" "+str(max_count))
  
    df_test['Label']=list_label_ans



    # keeping track of rule that is matching the most of the times
    df_test.Label.unique()
    # row_set
    df_test[1:50]

    c = 0
    for w in df_test['Label']:
        if (w == "ZERO"):
            df_test['Label'][c] = 0
            c = c+1
        elif w == "ONE":
            df_test['Label'][c] = 1
            c = c+1
        elif w == "TWO":
            df_test['Label'][c] = 2
            c = c+1
        elif w == "THREE":
            df_test['Label'][c] = 3
            c = c+1
        elif w == "FOUR":
            df_test['Label'][c] = 4
            c = c+1
        elif w == "FIVE":
            df_test['Label'][c] = 5
            c = c+1
        elif w == "SIX":
            df_test['Label'][c] = 6
            c = c+1
        else:
            df_test['Label'][c] = 7
            c = c+1
    df_test[200:250]



    lst1 = []
    lst2 = []
    fin = pd.DataFrame()
    for w in df_test2['id']:
        lst1.append(w)
    for w in df_test['Label']:
        lst2.append(w)
    fin['id'] = lst1
    fin['label'] = lst2
    fin.to_csv("C:/Users/Akanksha/Desktop/Mtech/Mtech_Sem1/DMG/Assignments/DMG_ASSIGNMENT3/dataset/result.csv",index=False)


if __name__ == "__main__":
        path2 = "C:/Users/Akanksha/Desktop/Mtech/Mtech_Sem1/DMG/Assignments/DMG_ASSIGNMENT3/dataset/test_X.csv"
        runner(path2)


