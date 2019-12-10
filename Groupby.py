import pandas as pd

def group_by_attrs(data_dict,attrs_lst):
    df = pd.DataFrame(data_dict)
    print('Table:')
    print(df)
    n=len(data_dict[attrs_lst[0]])
    values=[]
    for i in range(n):
        row_values=[]
        for attr in attrs_lst:
            row_values.append(data_dict[attr][i])
        row_values=tuple(row_values)
        values.append(row_values)
    values=list(set(values))
    for value in values:
        print('Group by {}'.format(value))
        print(df.groupby(attrs_lst).get_group(value))
        print('-------------------------------')

data_dict={'X' : ['B','A', 'C', 'B', 'B','B','A'], 'Y' : [7,1, 4, 3, 2,5,6],'Z' : [30,10, 40, 20, 30,20,10],'W':['Mary','Tom','Bob','Eli','Mary','Eli','Tom'],'Q':[00,11,22,33,44,55,66]}
attrs_lst=['X','Z','W']
group_by_attrs(data_dict,attrs_lst)
    



