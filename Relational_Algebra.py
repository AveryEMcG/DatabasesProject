import numpy as np
import pandas as pd
from texttable import Texttable

#------------------------------------------------------------------------------
#Union:
def union_of_tables(df_a, df_b):  #df_a , df_b : pandas.DataFrame
    print("Entered in union");
    print(pd.merge(df_a, df_b, on='subject_id', how='outer'))
    return pd.merge(df_a, df_b, on='subject_id', how='outer')
    #return pd.concat([df_a,df_b])

data_a = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
data_b = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

df_a = pd.DataFrame(data_a, columns = ['subject_id', 'first_name', 'last_name'])
df_b = pd.DataFrame(data_b, columns = ['subject_id', 'first_name', 'last_name'])
#print("The df_a in union is:",df_a,"The df_b in union is:",df_b)
union_of_tables(df_a, df_b)

#------------------------------------------------------------------------------
#Intersection
def intersection_of_tables(df_a, df_b): #df_a , df_b : pandas.DataFrame
    print("Entered in Intersection")
    print(pd.merge(df_a, df_b, on='subject_id', how='inner'))
    return pd.merge(df_a, df_b, on='subject_id', how='inner')

data_a = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
data_b = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

df_a = pd.DataFrame(data_a, columns = ['subject_id', 'first_name', 'last_name'])
df_b = pd.DataFrame(data_b, columns = ['subject_id', 'first_name', 'last_name'])
#print("The df_a in interection is:",df_a,"The df_b in intersection is:",df_b)
#print("The intesection of 2 tables is:")
intersection_of_tables(df_a, df_b)

#------------------------------------------------------------------------------
#Difference 
def diff_pd(df1, df2):
    print("Entered in Difference")
    assert (df1.columns == df2.columns).all(), \
        "DataFrame column names are different"
    if any(df1.dtypes != df2.dtypes):
        "Data Types are different, trying to convert"
        df2 = df2.astype(df1.dtypes)
    if df1.equals(df2):
        return None
    else:
        diff_mask = (df1 != df2) & ~(df1.isnull() & df2.isnull())
        ne_stacked = diff_mask.stack()
        changed = ne_stacked[ne_stacked]
        changed.index.names = ['id', 'col']
        difference_locations = np.where(diff_mask)
        changed_from = df1.values[difference_locations]
        changed_to = df2.values[difference_locations]
        print(pd.DataFrame({'from': changed_from, 'to': changed_to},
                            index=changed.index))
        return pd.DataFrame({'from': changed_from, 'to': changed_to},
                            index=changed.index)

data_a = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
data_b = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

df_a = pd.DataFrame(data_a, columns = ['subject_id', 'first_name', 'last_name'])
df_b = pd.DataFrame(data_b, columns = ['subject_id', 'first_name', 'last_name'])
#print("The df_a in difference is:",df_a,"The df_b in difference is:",df_b)
diff_pd(df_a, df_b)

#------------------------------------------------------------------------------
#Natural_Join
def match(row1, row2,t1atts,t2atts):
    t1columns = set(t1atts)
    t2columns = set(t2atts)
    t1map = {k: i for i, k in enumerate(t1atts)}
    t2map = {k: i for i, k in enumerate(t2atts)}
    join_on = t1columns & t2columns
    return all(row1[t1map[rn]] == row2[t2map[rn]] for rn in join_on)

def Natural_Join(t1atts,t2atts,t1tuples,t2tuples):
    print("Natural join")
    t1columns = set(t1atts)
    t2columns = set(t2atts)
    t1map = {k: i for i, k in enumerate(t1atts)}
    t2map = {k: i for i, k in enumerate(t2atts)}
    join_on = t1columns & t2columns
    diff = t2columns - join_on
    results = []
    for t1row in t1tuples:
        for t2row in t2tuples:
            if match(t1row, t2row,t1atts,t2atts):
                row = t1row[:]
                for rn in diff:
                    row.append(t2row[t2map[rn]])
                results.append(row)
    t = Texttable()
    t.add_rows(results)
    print(t.draw())

t1atts = ('Name','EmpId','DeptName')
t2atts = ('DeptName','Manager')
t1tuples=[['Harry',3415, 'Finance'],['Sally', 2241, 'Sales'],['George', 3401, 'Finance'],['Harriet',	2202, 'Sales']]
t2tuples = [['Finance', 'George'],['Sales', 'Harriet'],['production', 'Charles']]
#print("The Natural join")
Natural_Join(t1atts,t2atts,t1tuples,t2tuples)

#------------------------------------------------------------------------------
#Cross_Join 
def df_crossjoin(df1, df2, **kwargs):
    print("Entered the cross join")
    df1['_tmpkey'] = 1
    df2['_tmpkey'] = 1
    res = pd.merge(df1, df2, on='_tmpkey', **kwargs).drop('_tmpkey', axis=1)
    res.index = pd.MultiIndex.from_product((df1.index, df2.index))
    df1.drop('_tmpkey', axis=1, inplace=True)
    df2.drop('_tmpkey', axis=1, inplace=True)
    print(res)
    return res


origin_cities = ['Berlin',  'Hamburg', 'Munich']
destination_cities = ['London',  'New York City', 'Moscow', 'Sydney', 'Istanbul']
origin_coords = {'lat':  [52.5, 53.5, 48.1],'lng':  [13.4, 9.9,  11.5]}
destination_coords = {'lat':  [51.5,  40.7, 55.7,-33.8, 41.01],'lng':  [-0.1, -74, 37.6, 151.2, 28.9]}
df_orig = pd.DataFrame(origin_coords, index=origin_cities)
df_dest = pd.DataFrame(destination_coords, index=destination_cities)
#print("The df_org in cross is:",df_orig,"The df_dest in cross is:",df_dest)
df_crossjoin(df_orig, df_dest, suffixes=('_orig', '_dest'))
