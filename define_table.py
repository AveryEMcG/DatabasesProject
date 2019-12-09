def check_number_attrs():
    num_attr = int(input("Please enter the number of attributes in your table: "))
    if (num_attr > 4 or num_attr < 1):
        print("Unsupported table dimensions. Enter 'try again' to try again or 'q' to exit.")
        trial=input()
        if trial=='try again':
            return check_number_attrs()
        else:
            return None
    else:
        return num_attr

def check_attrs_type(i):
    print("Please declare the type of attribute {}. Only 'string' and 'int' are supported.".format(i))
    attr_type=input()
    if (attr_type != 'string' and attr_type != 'int'):
        print("Unsupported table type. Enter 'try again' to try again or 'q' to exit.")
        trial=input()
        if trial=='try again':
            return check_attrs_type(i)
        else:
            return None
    else:
        return attr_type

def type_attrs(num_attr):
    attr_types = []
    i = 1
    while (i <= num_attr):
        attr_type=check_attrs_type(i)
        attr_types.append(attr_type)
        i += 1 
    return attr_types
    
def define_table():
    print("Please enter name of the table.")
    table_name=input()
    num_attr=check_number_attrs()
    if num_attr!=None:
        all_attr_type=type_attrs(num_attr)
        print('Attributes names by defualt are from set {A, B, C , D} in order.')
        names=['A','B','C','D']
        attr_names=names[0:num_attr]
        print("Attribute_names",attr_names)
        print("Table_name",table_name)
        print("All_attributes_type",all_attr_type)
        return table_name, all_attr_type, attr_names
    else:
        return 'Failed! Define table from beginning.'
if __name__ == '__main__':
    define_table()
