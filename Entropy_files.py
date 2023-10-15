import os
import pandas as pd
import numpy as np
import sys
from pychartdir import *
 
#Put the paths of all files into the listcsv list
def list_dir(file_dir):
    # list_csv = []
    dir_list = os.listdir(file_dir)
    for cur_file in dir_list:
        path = os.path.join(file_dir,cur_file)
        #Determine whether it is a folder or a file
        if os.path.isfile(path):
            # print("{0} : is file!".format(cur_file))
            dir_files = os.path.join(file_dir, cur_file)
        if os.path.isdir(path):
            # print("{0} : is dir".format(cur_file))
            # print(os.path.join(file_dir, cur_file))
            list_dir(path)            
        #Determine whether a .csv file exists. If it exists, obtain the path information and write it into the list_csv list.
        if os.path.splitext(path)[1] == '.csv':
            csv_file = os.path.join(file_dir, cur_file)            
            list_csv.append(csv_file)
    return list_csv
 

#Calculate the rose entropy of all outgoing or incoming flows for each city to represent symolic forces
def rose_entropy(df,cityname):
    
    # Calculate the unweighted intensity and weighted intensity of each bin(take 24 bins as an example)
    list_bin=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    dict_nonweight = dict.fromkeys(list_bin,0)
    dict_weighted = dict.fromkeys(list_bin,0)

    df_merge0 = df['COUNT_ODflow'].groupby(df['bin']).sum()
    dict0 = df_merge0.to_dict()

    df_merge1 = df['ODflowlength_Strength'].groupby(df['bin']).sum()
    dict1 = df_merge1.to_dict()
    dict_nonweight.update(dict0)
    dict_weighted.update(dict1)
    print(dict_nonweight,dict_weighted)

    data0 = list(dict_nonweight.values())
    data = list(dict_weighted.values())

    print(data0,data)

    #Calculate information entropy
    sum1 = sum(data0)
    ent_nonweight = ent_weighted =0.00
    for x in data0:
        if x !=0:
            pi = x/sum1
            logpi = np.log2(pi)
            ent_nonweight -= pi*logpi
        else:
            ent_nonweight +=0
    sum2 = sum(data)
    for y in data:
        if y !=0:
            pii = y/sum2
            logpii = np.log2(pii)
            ent_weighted -= pii*logpii
        else:
            ent_weighted +=0
    


    #Calculate the probability of each bin
    # a = 24
    # pi_data0 = [None]*a
    # pi_data = pi_data0  
    # for i in range(0, len(data0)) :
    #     pi_data0[i] = data0[i]/sum1
    # for i in range(0, len(data)) :
    #     pi_data[i] = data[i]/sum2
    # print(pi_data0,pi_data)


    #Draw a non-weighted wind rose map
    angles = [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270,
        285, 300, 315, 330, 345]
    c = PolarChart(460, 460, 0xffffff, 0x000000, 1)
    c.setPlotArea(230, 240, 180, 0xffffff)
    c.setGridStyle(0)
    c.angularAxis().setLinearScale(0, 360, 30)
    for i in range(0, len(data0)) :
        c.angularAxis().addZone(angles[i], angles[i] + 15, 0, data0[i], 0x0066ff, 0x000000)
    c.addLineLayer(data0, Transparent)
    c.makeChart("..\OCityRose\uw"+"_"+str(ent_nonweight)[:4]+cityname+".png")

    #Draw a length-weighted wind rose map
    b = PolarChart(460, 460, 0xffffff, 0x000000, 1)
    b.setPlotArea(230, 240, 180, 0xffffff)
    b.setGridStyle(0)
    b.angularAxis().setLinearScale(0, 360, 30)
    for i in range(0, len(data)) :
        b.angularAxis().addZone(angles[i], angles[i] + 15, 0, data[i], 0x0066ff, 0x000000)
    b.addLineLayer(data, Transparent)
    b.makeChart("..\OCityRose\w"+"_"+str(ent_weighted)[:4]+cityname+".png")

    return ent_nonweight,ent_weighted


#Output the symbolic force results for all cities
if __name__ == '__main__':
    paths = '..\OCitytables'
    list_csv = []
    list_dir(file_dir=paths)
    # print(list_csv)
    list_uw = []
    list_w = []
    list_city=[]
    for cfile in list_csv:
        df = pd.read_csv(cfile, header=0)
        csvname =  cfile.split('\\')[-1]
        tabname =  csvname.split('.')[0]
        cityname = tabname.split('_')[-1]
        uw,w = rose_entropy(df,cityname)
        list_uw.append(uw)
        list_w.append(w)
        list_city.append(cityname)
    df_ent = pd.DataFrame({'city':list_city,'w_ent':list_w,'uw_ent':list_uw})
    df_ent.to_csv("..\OCityRose\Entropy_OCity.csv",index = None,encoding = 'utf_8_sig')
    print('over')
