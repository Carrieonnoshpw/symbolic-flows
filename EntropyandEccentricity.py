import numpy as np
import pandas as pd
import os
import math
from decimal import *
 

#Construct a standard dataframe, delete the "OID" column, merge rows with the same bin, and output in the order of bin, 'COUNT_ODflow', 'ODflow_int'
def shortarray(df,colnum,colname1,colname2,gname):
    df.drop(columns=colnum, axis=1,inplace=True)
    df_1 = df[colname1].groupby(df[gname]).sum()
    df_2 = df[colname2].groupby(df[gname]).sum()
    df_sum = pd.concat([df_1,df_2],axis=1)
    df_sum[gname]=df_sum.index
    df_sum.reset_index(drop=True,inplace=True)
    order = [gname,colname1,colname2]
    df_sum = df_sum[order]
    return df_sum

#Construct a standard dataframe, and fill in the missing bins with 0
def standardarray(df_short):
    list0 = np.arange(1,25,1)
    list1 = df_short['bin'].tolist()
    list2=set(list0).difference(set(list1))
    list3 = [0]*len(list2)
    c = [list2,list3,list3]
    df_add=pd.DataFrame(c)
    df_add=df_add.T
    df_add.rename(columns={0:'bin',1:'COUNT_ODflow',2:'ODflow_int'},inplace=True)
    df_st=pd.concat([df_short, df_add], ignore_index=True)
    df_st.sort_values('bin',inplace=True)
    return(df_st)

#Construct an orientation vector
# 0 and 1 respectively represent whether there is a bin in the specified orientation
def azimutharray(list0):
    list1 = []
    for item in list0:
        if item !=0:
            item = 1
        list1.append(item)

    return list1

#Insert a row of data in the specified row
def insert(df, i, df_add):
    df1 = df.iloc[:i, :]
    df2 = df.iloc[i:, :]
    df_new = pd.concat([df1, df_add, df2], ignore_index=True)
    return df_new

    

#Calculate symbolic eccentricity
def spatial_pianxindu(list_value):
    list_pxd = [None]*3
    xs,ys,asum,xi_1,yi_1,i=0,0,0,0,0,0
    for item in list_value:
        area = 0.5*item*item*math.sin(math.pi/12)
        xi = item*(math.sin((math.pi/12)*(i+1)))
        yi = item*(math.cos((math.pi/12)*(i+1)))
        xi_1 = item*(math.sin((math.pi/12*i)))
        yi_1 = item*(math.cos((math.pi/12*i)))
        # x_ = (xi+xi_1)/3
        # y_ = (yi+yi_1)/3
        xs = ((xi+xi_1)/3)*area+xs
        ys = ((yi+yi_1)/3)*area+ys
        asum = area+asum
        i = i+1

    x = xs/asum
    y = ys/asum
    pxd = math.sqrt(x*x+y*y) 
    list_pxd[0] = x
    list_pxd[1] = y
    list_pxd[2] = pxd
    #print('jieguo',list_pxd)
    return (list_pxd)


#Calculate length-weighted information entropy to represent symbolic force
def entropy_len(data):
    sum2 = sum(data)
    ent_weighted = 0
    for y in data:
        if y !=0:
            pii = y/sum2
            logpii = np.log2(pii)
            ent_weighted -= pii*logpii
        else:
            ent_weighted +=0
    return(ent_weighted)


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
        #Determine whether a .csv file exists. If it exists, obtain the path information and write it into the list_csv list.
        if os.path.splitext(path)[1] == '.csv':
            csv_file = os.path.join(file_dir, cur_file)
            # print(os.path.join(file_dir, cur_file))
            # print(csv_file)
            list_csv.append(csv_file)
        if os.path.isdir(path):
            # print("{0} : is dir".format(cur_file))
            # print(os.path.join(file_dir, cur_file))
            list_dir(path)
    return list_csv
 
##Output the csv of the standard windrose dataframe and the attributes of a single city
if __name__ == '__main__':
    #Input folder
    paths = '...\Input'
    #Output folder
    pathp = '...\Output'
    list_cityname = []
    list_entropy= []
    list_bcb = []
    list_pxd0 = []
    list_pxd1 = []
    list_pxd2 = []
    list_pxd3 = []
    list_pxd4 = []
    list_pxd5 = []
    list_csv = []
    list_dir(file_dir=paths)
    for cfile in list_csv:
        cname = cfile.split('_')[1]
        cpath = os.path.join(pathp,cname)
        df = pd.read_csv(cfile, header=0)        
        df_sum = shortarray(df,'OID_','COUNT_ODflow','ODflow_int','bin')
        df_st = standardarray(df_sum)
        #print(df_st)
        #df_st.to_csv(cpath,index = None,encoding = 'utf_8_sig')
        ##Output the csv of the standard windrose dataframe
        
        #Calculate the symbolic eccentricity and force(information entropy) of each city
        cityname = cname.strip('.csv')
        pxd_list = spatial_pianxindu(df_st['ODflow_int']) 
        entropy_length = entropy_len(df_st['ODflow_int'])
        #分列存入列表
        list_cityname.append(cityname)
        list_entropy.append(entropy_length)
        list_pxd0.append(pxd_list[0])
        list_pxd1.append(pxd_list[1])
        list_pxd2.append(pxd_list[2])
        # list_pxd3.append(ppxd_list[0])
        # list_pxd4.append(ppxd_list[1])
        # list_pxd5.append(ppxd_list[2])
        # print(gravity_points(df_st['ODflow_int']) )
    #result = pd.DataFrame({'cityname':list_cityname,'entropy':list_entropy,'bocchangbi':list_bcb,'scenterx':list_pxd0,'scentery':list_pxd1,'spianxindu':list_pxd2,'gcenterx':list_pxd3,'gcentery':list_pxd4,'gpianxindu':list_pxd5})
    result = pd.DataFrame({'cityname':list_cityname,'entropy':list_entropy,'bocchangbi':list_bcb,'scenterx':list_pxd0,'scentery':list_pxd1,'spianxindu':list_pxd2})
    result.to_csv('...\OputResult\result_cities.csv',index = None,encoding = 'utf_8_sig')#Output the calculation results of all cities
        # array_df=df_st[['ODflow_int']].to_numpy()
        # print(df_sum,df_st)



