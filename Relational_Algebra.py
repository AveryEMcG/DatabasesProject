import numpy as np
import pandas as pd
from texttable import Texttable

class RelationalAlgebra:
    def union_of_tables(self, data_a, data_b, attribute):
        print("Entered in union")
        col_a = []
        col_b = []
        for key in data_a:
            col_a.append(key)
        for key in data_b:
            col_b.append(key)
        df_a = pd.DataFrame(data_a, columns=col_a)
        df_b = pd.DataFrame(data_b, columns=col_b)
        print(pd.merge(df_a, df_b, on=attribute, how='outer'))

    def intersection_of_tables(self, data_a, data_b, attribute):
        print("Entered in Intersection")
        col_a = []
        col_b = []
        for key in data_a:
            col_a.append(key)
        for key in data_b:
            col_b.append(key)
        df_a = pd.DataFrame(data_a, columns=col_a)
        df_b = pd.DataFrame(data_b, columns=col_b)
        print(pd.merge(df_a, df_b, on=attribute, how='inner'))


    def diff_pd(self, data_a, data_b):
        print("Entered in Difference")
        col_a = []
        col_b = []
        for key in data_a:
            col_a.append(key)
        for key in data_b:
            col_b.append(key)
        df_a = pd.DataFrame(data_a, columns=col_a)
        df_b = pd.DataFrame(data_b, columns=col_b)
        try :
            assert (df_a.columns == df_b.columns).all(), \
            "DataFrame column names are different"
        except:
            print("The tables are not similar.")
            return
        if any(df_a.dtypes != df_b.dtypes):
            "Data Types are different, trying to convert"
            df_b = df_b.astype(df_a.dtypes)
        if df_a.equals(df_b):
            return None
        else:
            diff_mask = (df_a != df_b) & ~(df_a.isnull() & df_b.isnull())
            ne_stacked = diff_mask.stack()
            changed = ne_stacked[ne_stacked]
            changed.index.names = ['id', 'col']
            difference_locations = np.where(diff_mask)
            changed_from = df_a.values[difference_locations]
            changed_to = df_b.values[difference_locations]
            print(pd.DataFrame({'from': changed_from, 'to': changed_to},
                                index=changed.index))

    def match(self, row1, row2,t1atts,t2atts):
        t1columns = set(t1atts)
        t2columns = set(t2atts)
        t1map = {k: i for i, k in enumerate(t1atts)}
        t2map = {k: i for i, k in enumerate(t2atts)}
        join_on = t1columns & t2columns
        return all(row1[t1map[rn]] == row2[t2map[rn]] for rn in join_on)

    def natural_join(self, t1atts,t2atts,t1tuples,t2tuples):
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
                if self.match(t1row, t2row,t1atts,t2atts):
                    row = t1row[:]
                    for rn in diff:
                        row.append(t2row[t2map[rn]])
                    results.append(row)
        t = Texttable()
        t.add_rows(results)
        print(t.draw())

    def df_crossjoin(self, df1, df2, **kwargs):
        print("Entered the cross join")
        df1['_tmpkey'] = 1
        df2['_tmpkey'] = 1
        res = pd.merge(df1, df2, on='_tmpkey', **kwargs).drop('_tmpkey', axis=1)
        res.index = pd.MultiIndex.from_product((df1.index, df2.index))
        df1.drop('_tmpkey', axis=1, inplace=True)
        df2.drop('_tmpkey', axis=1, inplace=True)
        print(res)
