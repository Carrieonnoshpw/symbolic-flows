#Identify place symbols from restaurant names
#Match the identified place symbols to prefecture-level cities
import cpca
import pandas as pd

##f is the total table of restaurant POIs
f=pd.read_csv('...\restaurantname.csv', header=0)
listf = f['purename'].tolist()
loc = cpca.transform(listf)
loc = loc.drop(['省','市','区','地址'],axis=1)
dft = pd.concat([f,loc], axis=1)
dft.to_csv('...\df.csv')

# df is the total table after calculating cpca
df = pd.read_csv('..\df.csv', header=0)

# df1 is the table where cpca is not empty
# df0 is the table that needs to be processed in the next step
df1 = df[df['code'].notna()]
df0 = df[df['code'].isnull()] 


#Extract restaurant names containing city historical names
df0.loc[df0['purename'].str.contains('北平|京华|京都|帝都|首都|京城', na=False),'code']='110000'
df0.loc[df0['purename'].str.contains('津门|津沽', na=False),'code']='120000'
df0.loc[df0['purename'].str.contains('石门', na=False),'code']='130100'
df0.loc[df0['purename'].str.contains('晋阳|龙城', na=False),'code']='140100'
df0.loc[df0['purename'].str.contains('呼市|蒙古', na=False),'code']='150100'

df0.loc[df0['purename'].str.contains('奉天|盛京', na=False),'code']='210100'
df0.loc[df0['purename'].str.contains('喜都', na=False),'code']='220100'
df0.loc[df0['purename'].str.contains('冰城|上京|松花江', na=False),'code']='230100'

df0.loc[df0['purename'].str.contains('沪上|申城|魔都', na=False),'code']='310000'
df0.loc[df0['purename'].str.contains('金陵|建康', na=False),'code']='320100'
df0.loc[df0['purename'].str.contains('阳澄湖|藏书', na=False),'code']='320500'
df0.loc[df0['purename'].str.contains('盱眙', na=False),'code']='320800'
df0.loc[df0['purename'].str.contains('杭城|临安|钱塘', na=False),'code']='330100'
df0.loc[df0['purename'].str.contains('甬城', na=False),'code']='330200'
df0.loc[df0['purename'].str.contains('庐州|霸都', na=False),'code']='340100'
df0.loc[df0['purename'].str.contains('淮南', na=False),'code']='340400'
df0.loc[df0['purename'].str.contains('闽都', na=False),'code']='350100'
df0.loc[df0['purename'].str.contains('思明', na=False),'code']='350200'
df0.loc[df0['purename'].str.contains('豫章', na=False),'code']='360100'
df0.loc[df0['purename'].str.contains('齐鲁|泉城|齐州', na=False),'code']='370100'

df0.loc[df0['purename'].str.contains('中原|商都', na=False),'code']='410100'
df0.loc[df0['purename'].str.contains('逍遥镇', na=False),'code']='411600'
df0.loc[df0['purename'].str.contains('荆楚|江城', na=False),'code']='420100'
df0.loc[df0['purename'].str.contains('湘楚|星城', na=False),'code']='430100'
df0.loc[df0['purename'].str.contains('南粤|花城|羊城', na=False),'code']='440100'
df0.loc[df0['purename'].str.contains('鹏城', na=False),'code']='440300'
df0.loc[df0['purename'].str.contains('西粤|邕城', na=False),'code']='450100'
df0.loc[df0['purename'].str.contains('椰城', na=False),'code']='460100'

df0.loc[df0['purename'].str.contains('山城|雾都|巫山|万州', na=False),'code']='500000'
df0.loc[df0['purename'].str.contains('天府|蓉城|蜀都|成都', na=False),'code']='510100'
df0.loc[df0['purename'].str.contains('富顺', na=False),'code']='510300'
df0.loc[df0['purename'].str.contains('花溪', na=False),'code']='520100'
df0.loc[df0['purename'].str.contains('春城', na=False),'code']='530100'
df0.loc[df0['purename'].str.contains('逻些|日光城', na=False),'code']='540100'

df0.loc[df0['purename'].str.contains('长安|镐京|三秦|秦都', na=False),'code']='610100'
df0.loc[df0['purename'].str.contains('岐山', na=False),'code']='610300'
df0.loc[df0['purename'].str.contains('潼关', na=False),'code']='610500'
df0.loc[df0['purename'].str.contains('金城|兰州', na=False),'code']='620100'
df0.loc[df0['purename'].str.contains('西海', na=False),'code']='630100'
df0.loc[df0['purename'].str.contains('乌市|迪化', na=False),'code']='650100'

#df2 is a city table whose secondary alias is not empty
#df00 is a table that needs to be processed in the next step
df2 = df0[df0['code'].notnull()]
df00 = df0[df0['code'].isnull()]



#Extract restaurant names containing city abbreviation name
df00.loc[df00['purename'].str.contains('川|蜀', na=False),'code']='510100'
df00.loc[df00['purename'].str.contains('鲁', na=False),'code']='370100'
df00.loc[df00['purename'].str.contains('粤', na=False),'code']='440100'
df00.loc[df00['purename'].str.contains('浙', na=False),'code']='330100'
df00.loc[df00['purename'].str.contains('闽', na=False),'code']='350100'
df00.loc[df00['purename'].str.contains('湘', na=False),'code']='430100'
df00.loc[df00['purename'].str.contains('徽|皖', na=False),'code']='340100'
df00.loc[df00['purename'].str.contains('沪|申', na=False),'code']='310000'
df00.loc[df00['purename'].str.contains('杭|浙', na=False),'code']='330100'
df00.loc[df00['purename'].str.contains('甬', na=False),'code']='330200'
df00.loc[df00['purename'].str.contains('赣', na=False),'code']='360100'
df00.loc[df00['purename'].str.contains('渝', na=False),'code']='500000'
df00.loc[df00['purename'].str.contains('豫', na=False),'code']='410100'
df00.loc[df00['purename'].str.contains('鄂', na=False),'code']='420100'
df00.loc[df00['purename'].str.contains('黔', na=False),'code']='520100'
df00.loc[df00['purename'].str.contains('滇', na=False),'code']='530100'
df00.loc[df00['purename'].str.contains('藏', na=False),'code']='540100'
df00.loc[df00['purename'].str.contains('陕', na=False),'code']='610100'
df00.loc[df00['purename'].str.contains('冀', na=False),'code']='130100'
df00.loc[df00['purename'].str.contains('晋', na=False),'code']='140100'

#df3 is a city table whose abbreviation is not empty
df3 = df00[df00['code'].notnull()]

#df_code is the city table with encoding, df_output is the processed total table
df_code0 = pd.concat([df1,df2], axis=0)
df_code = pd.concat([df_code0,df3], axis=0)
df_output = pd.concat([df_code0,df00],axis=0)

#Output processing results
df_code.to_csv('...\df_code.csv')
df_output.to_csv('...\df_output.csv')
