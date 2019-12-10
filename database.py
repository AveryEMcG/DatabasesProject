from table import Table
from mvd import MVD
from Relational_Algebra import RelationalAlgebra as RA
class Database:
    __tables = []

    def get_tables(self):
        return self.__tables

    def validate_number_of_tables(self, number_of_tables):
        while number_of_tables is None:
            try:
                number_of_tables = int(input("Enter the number of tables you want to store in the database.\n"))
                if(number_of_tables < 0):
                    print("Please enter a positive integral value for the number of tables.\n")
                    number_of_tables = None
            except:
                print("Please enter a positive integral value for the number of tables.\n")
        return number_of_tables



    def validate_number_of_attributes(self, table_name, number_of_attributes):
        while number_of_attributes is None:
            try:
                number_of_attributes = int(input("Enter the number of attributes for table {}\n".format(table_name)))
                if(number_of_attributes > 5 and number_of_attributes < 1):
                    print("Please enter a positive integer between 1 and 5 for table {}\n".format(table_name))
                    number_of_attributes = None
            except:
                print("Please enter a positive integer between 1 and 5 for table {}\n".format(table_name))
        return number_of_attributes

    def validate_attribute_type(self, attribute_type):
        return attribute_type.lower() == 'integer' or attribute_type.lower() == 'string'

    def validate_attribute_name(self, attribute_name):
        return len(attribute_name) == 1 and attribute_name == attribute_name.upper()

    def trigger_table_input(self, number_of_tables):
        for index1 in range(number_of_tables):
            table_name = ''
            while table_name == '':
                table_name = input("Enter the name of table number {}:\n".format(index1 + 1))

            number_of_attributes = self.validate_number_of_attributes(table_name, None)
            print("Please enter the attribute type and attribute name in the format - attribute_type:attribute_name\n")
            table_attributes = []
            attribute_types = []
            index2 = 0
            while index2 < number_of_attributes:
                attribute_description = input("Please enter attribute number {}\n".format(index2 + 1))
                try:
                    attribute_tokens = attribute_description.split(":")
                    if not self.validate_attribute_type(attribute_tokens[0]):
                        print("Please enter string or integer as the attribute type. For instance: string\n")
                        continue
                    elif not self.validate_attribute_name(attribute_tokens[1]):
                        print("Please enter uppercase attribute name of length 1. For instance: A\n")
                        continue
                    elif attribute_tokens[1] in table_attributes:
                        print("Please choose another name for attribute as it already exists within the table.\n")
                        continue
                    table_attributes.append(attribute_tokens[1])
                    attribute_types.append(attribute_tokens[0])
                except:
                    print("Please enter the attribute type and attribute name in the format - attribute_type:attribute_name\n")
                    continue
                index2 += 1
            self.__tables.append(Table(table_name, table_attributes, attribute_types))

    def trigger_table_constraints(self):
        for index1 in range(len(self.__tables)):
            print("Please enter the constraints for table {}\n".format(self.__tables[index1].get_table_name()))
            table_attributes = self.__tables[index1].get_table_attributes()
            attribute_types = self.__tables[index1].get_attribute_types()
            attribute_constraints = []
            for index2 in range(len(table_attributes)):
                print("Please enter the constraints in format (attribute_name operator comparator) "
                      "for attribute {}  or enter 'quit' to finish entering constraints for the attribute\n"
                      .format(table_attributes[index2]))
                string_attribute_constraints = {"==" : [], "<>" : []}
                integer_attribute_constraints = {"==" : [], "<>" :[], "<=" : [], "<" :[], ">" : [], ">=" :[]}
                while(True):
                    constraint = input()
                    if(constraint == 'quit'):
                        break
                    elif(constraint==''):
                        print("Please enter the constraints in format (attribute_name operator comparator) "
                            "for attribute {}  or enter @$ to finish entering constraints for the attribute\n"      
                            .format(table_attributes[index2]))                                              
                    elif(constraint[0] != table_attributes[index2]):
                        print("Enter attributes for {}".format(table_attributes[index2]))
                        continue
                    # Completed for string data-type.
                    if(attribute_types[index2] == 'string'):
                        if "==" in constraint:
                            if(len(string_attribute_constraints["=="]) == 1):
                                print("Equals constraint already exists. Please enter others.")
                                continue
                            elif(constraint.split("==")[1] not in string_attribute_constraints["<>"]):
                                string_attribute_constraints["=="].append(constraint.split("==")[1])
                                print("Valid constraint. Please enter others or enter @$ to finish entering constraints for the attribute")
                            else:
                                print("Invalid constraint. Exists in not equal constraint. Please enter others or enter @$ to finish entering constraints for the attribute")
                        elif "<>" in constraint:
                            if len(string_attribute_constraints["=="]) > 0:
                                print("Invalid constraint. Equality constraint already exists. Please enter others or enter @$ to finish entering constraints for the attribute")
                            else:
                                string_attribute_constraints["<>"].append(constraint.split("<>")[1])
                                print("Valid constraint. Please enter others or enter @$ to finish entering constraints for the attribute")
                        else :
                            print("Please enter == or <> as the constraints for string type.")
                    # Pending for integer data-type.
                    else:
                        if "==" in constraint:
                            try:
                                int(constraint.split("==")[1])
                            except:
                                print("Invalid constraint. Enter a numerical value for comparison. Please enter others or enter @$ to finish entering constraints for the attribute")
                                continue
                            if (len(integer_attribute_constraints["=="]) == 1):
                                print("Invalid constraint. Equals constraint already exists. Please enter others.")
                                continue
                            elif(constraint.split("==")[1] not in integer_attribute_constraints["<>"]):
                                count = 0
                                if len(integer_attribute_constraints["<"]) > 0:
                                    print("Invalid constraint. Less than constraint exists with {}. Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                        integer_attribute_constraints["<"][0]))
                                    count += 1
                                if len(integer_attribute_constraints["<="]) > 0:
                                    print("Invalid constraint. Less than equal to constraint exists with {}. Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                        integer_attribute_constraints["<="][0]))
                                    count += 1
                                if len(integer_attribute_constraints[">"]) > 0:
                                    print("Invalid constraint. Greater than constraint exists with {}. Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                        integer_attribute_constraints[">"][0]))
                                    count += 1
                                if len(integer_attribute_constraints[">="]) > 0:
                                    print("Invalid constraint. Greater than equal to constraint exists with {}. Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                        integer_attribute_constraints[">="][0]))
                                    count += 1
                                if len(integer_attribute_constraints["<>"]) > 0:
                                    print("Invalid constraint. Not equal to constraint exists with {}. Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                        integer_attribute_constraints["<>"][0]))
                                    count += 1
                                if count == 0:
                                    integer_attribute_constraints["=="].append(constraint.split("==")[1])
                                    print("Valid constraint. Please enter others or enter @$ to finish entering constraints for the attribute")
                            else:
                                print("Invalid constraint. The value exists as an inequality constraint. Please enter others or enter @$ to finish entering constraints for the attribute")
                        elif "<>" in constraint:
                            try:
                                int(constraint.split("<>")[1])
                            except:
                                print("Invalid constraint. Enter a numerical value for comparison.")
                                continue
                            if len(integer_attribute_constraints["=="]) > 0:
                                print("Invalid constraint. Equality constraint exists with {}".format(
                                    integer_attribute_constraints["=="][0]))
                        elif ">" in constraint and ">=" not in constraint:
                            count = 0
                            try:
                                int(constraint.split(">")[1])
                            except:
                                print("Invalid constraint. Enter a numerical value for comparison.")
                                continue
                            if len(integer_attribute_constraints["=="]) > 0:
                                count += 1
                                print("Invalid constraint. Equality constraint already exists with Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                    integer_attribute_constraints["=="][0]))
                            if len(integer_attribute_constraints["<"]) > 0:
                                if int(constraint.split(">")[1]) > int(integer_attribute_constraints["<"][0]):
                                    print("Invalid constraint. Enter values less than {} Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                        int(integer_attribute_constraints["<"][0]) - 1))
                                    count += 1
                            if len(integer_attribute_constraints["<="]) > 0:
                                if int(constraint.split(">")[1]) > int(integer_attribute_constraints["<="][0]):
                                    print("Invalid constraint. Enter values less than {} Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                        integer_attribute_constraints["<="][0]))
                                    count += 1
                            if len(integer_attribute_constraints[">="]) > 0:
                                if int(constraint.split(">")[1]) > int(integer_attribute_constraints[">="][0]):
                                    print("Invalid constraint. Enter values less than {} Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                        integer_attribute_constraints[">="][0]))
                                    count += 1
                            if len(integer_attribute_constraints[">"]) > 0:
                                count += 1
                                print("Invalid constraint. Greater than constraint already exists. Please enter others or enter @$ to finish entering constraints for the attribute")
                            if count == 0:
                                print("Valid constraint. Please enter others or enter @$ to finish entering constraints for the attribute")
                                integer_attribute_constraints[">"].append(constraint.split(">")[1])
                        elif ">=" in constraint:
                            count = 0
                            try:
                                int(constraint.split(">=")[1])
                            except:
                                print("Invalid constraint. Enter a numerical value for comparison.")
                                continue
                            if len(integer_attribute_constraints["=="]) > 0:
                                count += 1
                                print("Invalid constraint. Equality constraint already exists with {} Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                    integer_attribute_constraints["=="][0]))
                            if len(integer_attribute_constraints["<"]) > 0:
                                    if int(constraint.split(">=")[1]) > int(integer_attribute_constraints["<"][0]):
                                        print("Invalid constraint. Enter values less than {} Please enter others or enter @$ to finish entering constraints for the attribute".format(int(integer_attribute_constraints["<"][0]) - 1))
                                        count += 1
                            if len(integer_attribute_constraints["<="]) > 0:
                                    if int(constraint.split(">=")[1]) > int(integer_attribute_constraints["<="][0]):
                                        print("Invalid constraint. Enter values less than {} Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                            integer_attribute_constraints["<="][0]))
                                        count += 1
                            if len(integer_attribute_constraints[">"]) > 0:
                                if int(constraint.split(">=")[1]) <= int(integer_attribute_constraints[">"][0]):
                                    print("Invalid constraint. Enter values greater than {} Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                        integer_attribute_constraints[">"][0]))
                                    count += 1
                            if len(integer_attribute_constraints[">="]) > 0:
                                count += 1
                                print("Invalid constraint. Greater than equal to constraint already exists. Please enter others or enter @$ to finish entering constraints for the attribute")
                            if count == 0:
                                print("Valid constraint. Please enter others or enter @$ to finish entering constraints for the attribute")
                                integer_attribute_constraints[">="].append(constraint.split(">=")[1])
                        elif "<" in constraint and "<=" not in constraint:
                            count = 0
                            try:
                                int(constraint.split("<")[1])
                            except:
                                print("Invalid constraint. Enter a numerical value for comparison. Please enter others or enter @$ to finish entering constraints for the attribute")
                                continue
                            if len(integer_attribute_constraints["=="]) > 0:
                                count += 1
                                print("Invalid constraint. Equality constraint already exists with {} Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                    integer_attribute_constraints["=="][0]))
                            if len(integer_attribute_constraints[">"]) > 0:
                                if int(constraint.split("<")[1]) < int(integer_attribute_constraints[">"][0]):
                                    print("Invalid constraint. Enter values greater than {} Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                        int(integer_attribute_constraints[">"][0]) + 1))
                                    count += 1
                            if len(integer_attribute_constraints[">="]) > 0:
                                if int(constraint.split("<")[1]) < int(integer_attribute_constraints[">="][0]):
                                    print("Invalid constraint. Enter values greater than {} Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                        integer_attribute_constraints[">="][0]))
                                    count += 1
                            if len(integer_attribute_constraints["<="]) > 0:
                                if int(constraint.split("<")[1]) < int(integer_attribute_constraints["<="][0]):
                                    print("Invalid constraint. Enter values greater than {} Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                        integer_attribute_constraints["<="][0]))
                                    count += 1
                            if len(integer_attribute_constraints["<"]) > 0:
                                count += 1
                                print("Invalid constraint. Less than constraint already exists. Please enter others or enter @$ to finish entering constraints for the attribute")
                            if count == 0:
                                print("Valid constraint. Please enter others or enter @$ to finish entering constraints for the attribute")
                                integer_attribute_constraints["<"].append(constraint.split("<")[1])
                        elif "<=" in constraint:
                            count = 0
                            try:
                                int(constraint.split("<=")[1])
                            except:
                                print("Invalid constraint. Enter a numerical value for comparison. Please enter others or enter @$ to finish entering constraints for the attribute")
                                continue
                            if len(integer_attribute_constraints["=="]) > 0:
                                count += 1
                                print("Invalid constraint. Equality constraint already exists with {} Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                    integer_attribute_constraints["=="][0]))
                            if len(integer_attribute_constraints[">"]) > 0:
                                if int(constraint.split("<=")[1]) < int(integer_attribute_constraints[">"][0]):
                                    print("Invalid constraint. Enter values greater than {} Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                        int(integer_attribute_constraints[">"][0])))
                                    count += 1
                            if len(integer_attribute_constraints[">="]) > 0:
                                if int(constraint.split("<=")[1]) < int(integer_attribute_constraints[">="][0]):
                                    print("Invalid constraint. Enter values greater than {} Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                        integer_attribute_constraints[">="][0]))
                                    count += 1
                            if len(integer_attribute_constraints["<"]) > 0:
                                if int(constraint.split("<=")[1]) >= int(integer_attribute_constraints["<"][0]):
                                    print("Invalid constraint. Enter values less than {} Please enter others or enter @$ to finish entering constraints for the attribute".format(
                                        integer_attribute_constraints["<"][0]))
                                    count += 1
                            if len(integer_attribute_constraints["<="]) > 0:
                                count += 1
                                print("Invalid constraint. Less than equal to constraint already exists. Please enter others or enter @$ to finish entering constraints for the attribute")
                            if (count == 0):
                                print("Valid constraint. Please enter others or enter @$ to finish entering constraints for the attribute")
                                integer_attribute_constraints["<="].append(
                                        constraint.split("<=")[1])
                        else:
                            print("Invalid constraint. Enter valid constraints from <, <=, ==, <>, >=, and >. Please enter others or enter @$ to finish entering constraints for the attribute")
                            continue
                if(attribute_types[index2] == "string"):
                    attribute_constraints.append(string_attribute_constraints)
                else:
                    attribute_constraints.append(integer_attribute_constraints)
            self.__tables[index1].set_attribute_constraints(attribute_constraints)

    def is_equivalent(self, str1, str2):
        str1 = "".join(sorted(str1))
        str2 = "".join(sorted(str2))
        return str1 == str2

    def trigger_table_fd(self):
        for table in self.__tables:
            name = table.get_table_name()
            table_attributes = table.get_table_attributes()
            table_fds = []
            print("The attribute list for table {} are {}".format(name, table_attributes))
            print("Please enter the FDs for table {} in format: A->B\nOr enter 'quit' to stop entering fds"
                  " and 'delete' to delete fds.".format(name))
            while (True):
                fd = input()
                if fd == "quit":
                    break
                if fd == "delete":
                    count = 0
                    fds = table_fds
                    fd = input("Enter the Functional dependency you want to remove from {}\n".format(fds))
                    while (count == 0):
                        try:
                            fds.remove(fd)
                            count += 1
                        except:
                            print("Invalid entry. Please enter the functional dependency from the {}".format(fds))
                            fd = input("Enter the Functional dependency you want to remove from {}\n".format(fds))
                    print("Deleted successfully.")
                    continue
                if "->" in fd:
                    attributes = fd.split("->")
                    lhs = attributes[0]
                    rhs = attributes[1]
                    count = 0
                    if self.is_equivalent(lhs, rhs):
                        print("Trivial Functional Dependency. Each attribute determines itself.")
                        continue
                    for attribute in lhs:
                        if attribute not in table_attributes:
                            print(
                                "Invalid Functional Dependency. The attribute {} does not exist.".format(attribute))
                            count += 1
                            break
                    for attribute in rhs:
                        if attribute not in table_attributes:
                            print(
                                "Invalid Functional Dependency. The attribute {} does not exist.".format(attribute))
                            count += 1
                            break
                    if count == 0:
                        fds = table_fds
                        fds_left = []
                        fds_right = []
                        for index in range(0, len(fds)):
                            temp = fds[index].split("->")
                            fds_left.append(temp[0])
                            fds_right.append(temp[1])
                        closure1 = table.compute_closure(fds_left, fds_right, lhs)
                        fds_left.append(lhs)
                        fds_right.append(rhs)
                        closure2 = table.compute_closure(fds_left, fds_right, lhs)
                        if not self.is_equivalent(closure1, closure2):
                            table_fds.append(fd)
                            print("Valid Functional Dependency.")
                        else:
                            print("Trivial Functional Dependency. Can be derived from others.")
                else:
                    print("Please enter Functional Dependencies in format A->B with uppercase attributes.")
            table.set_fds(table_fds)

    def trigger_table_mvds(self):
        mvd = MVD()
        for table in self.__tables:
            mvd.define_MVDs(table.get_fds(), table.get_table_attributes(), len(table.get_table_attributes()))

    def generate_table_key(self):
        for table in self.__tables:
            fds = table.get_fds()
            fd_left = []
            fd_right = []
            for fd in fds:
                attributes = fd.split("->")
                fd_left.append(attributes[0])
                fd_right.append(attributes[1])
            candidate_key = ""
            if len(fds) == 0:
                for attribute in table.get_table_attributes():
                    candidate_key += attribute
                candidate_keys = [candidate_key]
            else :
                candidate_keys = table.generate_candidate_keys(fd_left, fd_right, table.get_table_attributes())
            print("The candidate keys for the table {} is/are {}".format(table.get_table_name(), candidate_keys))
            table.set_candidate_keys(candidate_keys)

    def compute_normal_form(self):
        for table in self.__tables:
            fds = table.get_fds()
            fd_left = []
            fd_right = []
            for fd in fds:
                attributes = fd.split("->")
                fd_left.append(attributes[0])
                fd_right.append(attributes[1])
            candidate_keys = table.get_candidate_keys()
            attributes = table.get_table_attributes()
            normal_form = table.compute_normal_form(fd_left, fd_right, candidate_keys, attributes)
            print("The table {} is in {}".format(table.get_table_name(), normal_form))
            if normal_form == "First Normal Form" or normal_form == "Second Normal Form":
                print("Please delete the whole table or edit the functional dependencies\n"
                      "for the table to be in Third Normal Form or Boyce-Codd Normal Form.\n")
            table.set_normal_form(normal_form)

    def Natural_Join(T1,T2):
        at1 = T1.__table_attributes
        at2 = T2.__table_attributes       
        tup1 = T1.__tuples
        tup2 = T2.__tuples 
        join = RA.Natural_Join(at1,at2,tup1,tup2)
        ck = join.get_candidate_keys()

        if T1.key in ck:
            join.set_key(T1.key)
        elif T2.key in ck:
            join.set_key(T1.key)
        elif len(ck)>=1:
            join.set_key(ck[0])
        else:
            print("Error, no key determined for crossjoin")
        return join      

    def Cross_Join(T1,T2):
        at1 = T1.__table_attributes
        at2 = T2.__table_attributes       
        tup1 = T1.__tuples
        tup2 = T2.__tuples 
        join = RA.Natural_Join(at1,at2,tup1,tup2)
        ck = join.get_candidate_keys()

        if T1.key in ck:
            join.set_key(T1.key)
        elif T2.key in ck:
            join.set_key(T1.key)
        elif len(ck)>=1:
            join.set_key(ck[0])
        else:
            print("Error, no key determined for crossjoin")

        return join        

    def trigger_key_input(self):
        for table in self.__tables:
            while(True):
                key = input("Please enter the key for table {}\n".format(table.get_table_name()))
                if key in table.get_candidate_keys():
                    table.set_key(key)
                    print("Valid key.")
                    break
                else:
                    print("Invalid key. Please choose one of {}".format(table.get_candidate_keys()))

    def trigger_foreign_key_input(self):
        if len(self.__tables) < 2:
            print("Insufficient number of tables for foreign key assignment.\n")
            return
        for table in self.__tables:
            while(True):
                if(table.get_foreign_key() != ""):
                    break
                foreign = input("Please enter the foreign key for table {} in format\n"
                                "table_name:attribute_name. Enter 'quit' to exit.\n"
                                .format(table.get_table_name(), self.__tables))
                if foreign == "quit":
                    break
                if ":" not in foreign:
                    print("Please enter the foreign key in the format table_name:attribute_name")
                    continue
                else:
                    count = 0
                    inp = foreign.split(":")
                    foreign_table = inp[0]
                    foreign_key = inp[1]
                    table_names = []
                    for table in self.__tables:
                        table_names.append(table.get_table_name())
                    if foreign_table not in table_names:
                        print("Table does not exist")
                        continue
                    for t in self.__tables:
                        if t.get_table_name() == foreign_table:
                            if foreign_key not in t.get_table_attributes():
                                count += 1
                                print("Attribute does not exist. Please re-enter")
                                break
                            else:
                                table.set_foreign_key(foreign_key)
                                table.set_foreign_table(t)
                                print("Foreign key added successfully.")



    def insert_rows(self):
        for table in self.__tables:
            table_tuples = []
            while(True):
                row = input("Please enter row values separated by commas for table {} \n"
                            "with attributes {} of type {} in the order that they appear.\n"
                            "For example: Attributes ABC with data type integer, string, integer should be input as\n"
                            "1,hello,2. Enter 'quit' to stop entering the input.\n"
                            "".format(table.get_table_name(), table.get_table_attributes(), 
                                                  table.get_attribute_types()))
                count = 0
                if row == 'quit':
                    break
                if "," in row:
                    tuple = row.split(",")
                    if(len(tuple) == len(table.get_table_attributes())):
                        key = table.get_key()
                        key_index = 0
                        attributes = table.get_table_attributes()
                        for index in range(len(attributes)):
                            if key == attributes[index]:
                                key_index = index
                        for row in table.get_tuples():
                            if tuple[key_index] == row[key_index]:
                                count += 1
                        if count != 0:
                            print("The value {} already exists".format(tuple[key_index]))
                            continue
                        if (table.get_foreign_key() != ""):
                            foreign_table = table.get_foreign_table()
                            foreign_attributes = foreign_table.get_table_attributes()
                            if table.get_foreign_key() not in foreign_attributes:
                                print("Invalid attribute entered. Please re-enter.\n")
                                continue
                            table_attributes = table.get_table_attributes()
                            table_index = 0
                            for index in range(len(table_attributes)):
                                if (table.get_foreign_key() == table_attributes[index]):
                                    table_index = index

                            foreign_index = 0
                            for index in range(len(foreign_attributes)):
                                if table.get_foreign_key() == foreign_attributes[index]:
                                    foreign_index = index
                            table_rows = foreign_table.get_tuples()
                            for row in table_rows:
                                if row[foreign_index] != tuple[table_index]:
                                    count = 1
                                else:
                                    count = 0
                                    break
                            if count == 1:
                                print("The value does not exist. Please enter it in the foreign table first.\n")
                                continue
                        types = table.get_attribute_types()
                        for index in range(0, len(types)):
                            if types[index] == "integer":
                                try:
                                    int(tuple[index])
                                    for constraint, values in table.get_attribute_constraints()[index].items():
                                        if constraint == "==" and len(values) > 0:
                                            if(int(tuple[index]) != int(values[0])):
                                                count+=1
                                                print("Invalid Value. Enter values equal to {}\n".format(values[0]))
                                                break
                                        elif constraint == "<>" and len(values) > 0:
                                            for value in values:
                                                if int(tuple[index]) == int(value):
                                                    count+=1
                                                    print("Invalid Value. Enter values not equal to {}\n".format(value))
                                                    break
                                        elif constraint == "<" and len(values) > 0:
                                            if int(tuple[index]) >= int(values[0]):
                                                count+=1
                                                print("Invalid Value. Enter values less than {}\n".format(values[0]))
                                                break
                                        elif constraint == "<=" and len(values) > 0:
                                            if int(tuple[index]) > int(values[0]):
                                                count += 1
                                                print("Invalid Value. Enter values less than equal to {}\n".format(values[0]))
                                                break
                                        elif constraint == ">=" and len(values) > 0:
                                            if int(tuple[index]) < int(values[0]):
                                                count += 1
                                                print("Invalid Value. Enter values greater than equal to {}\n".format(values[0]))
                                                break
                                        elif constraint == ">" and len(values) > 0:
                                            if int(tuple[index]) <= int(values[0]):
                                                count += 1
                                                print("Invalid Value. Enter values greater than {}\n".format(values[0]))
                                                break
                                        if count != 0:
                                            break
                                    if count != 0:
                                        break
                                except:
                                    print("Invalid data type entered. Please re-enter row values.\n")
                                    break
                            else:
                                for constraint, values in table.get_attribute_constraints()[index].items():
                                    if constraint == "==" and len(values) > 0:
                                        if tuple[index] != values[0]:
                                            count += 1
                                            print("Invalid Value. Enter values equal to {}\n".format(values[0]))
                                            break
                                    elif constraint == "<>" and len(values) > 0:
                                        for value in values:
                                            if tuple[index] == value:
                                                count += 1
                                                print("Invalid Value. Enter values that are not equal to {}\n".format(value))
                                                break
                                    if count != 0:
                                        break
                            if count != 0:
                                break
                        if count == 0:
                            table_tuples.append(tuple)
                            print("Valid value. Added to the table {}\n".format(table.get_table_name()))
                    else:
                        print("The number of values do not match the attributes. Please re-enter.\n")
                    table.set_tuple(table_tuples)

    def trigger_relational_algebra(self):
        while(True):
            rel = input("Choose the relational algebra operators Union, Intersection, "
                        "Difference, Natural Join, or Cross Join on two tables.\n")
            if rel == "quit":
                break
            elif rel.lower() == "union":
                tables = input("Please enter the tables in format: table1,table2\n")
                if "," in tables:
                    t = tables.split(",")
                    for table in self.__tables:
                        if t[0] == table.get_table_name():
                            table1 = table
                        elif t[1] == table.get_table_name():
                            table2 = table
                else:
                    print("Invalid input format. Please re-enter.\n")
                    continue
                attribute = input("Enter attribute for union.\n")
                if attribute in table1.get_table_attributes() and attribute in table2.get_table_attributes():
                    table1_attributes = table1.get_table_attributes()
                    table2_attributes = table2.get_table_attributes()
                    dict1 = {}
                    dict2 = {}
                    for table_attribute in table1_attributes:
                        dict1[table_attribute] = []
                    for table_attribute in table2_attributes:
                        dict2[table_attribute] = []
                    for row in table1.get_tuples():
                        for index in range(len(row)):
                            dict1[table1_attributes[index]].append(row[index])
                    for row in table2.get_tuples():
                        for index in range(len(row)):
                            dict2[table2_attributes[index]].append(row[index])
                    RA().union_of_tables(dict1, dict2, attribute)
                else:
                    print("The attribute entered is not common to both tables. Hence union cannot be done.\n")
            elif rel.lower() == "intersection":
                tables = input("Please enter the tables in format: table1,table2\n")
                if "," in tables:
                    t = tables.split(",")
                    for table in self.__tables:
                        if t[0] == table.get_table_name():
                            table1 = table
                        elif t[1] == table.get_table_name():
                            table2 = table
                else:
                    print("Invalid input format. Please re-enter.\n")
                    continue
                attribute = input("Enter attribute for Intersection.\n")
                if attribute in table1.get_table_attributes() and attribute in table2.get_table_attributes():
                    table1_attributes = table1.get_table_attributes()
                    table2_attributes = table2.get_table_attributes()
                    dict1 = {}
                    dict2 = {}
                    for table_attribute in table1_attributes:
                        dict1[table_attribute] = []
                    for table_attribute in table2_attributes:
                        dict2[table_attribute] = []
                    for row in table1.get_tuples():
                        for index in range(len(row)):
                            dict1[table1_attributes[index]].append(row[index])
                    for row in table2.get_tuples():
                        for index in range(len(row)):
                            dict2[table2_attributes[index]].append(row[index])
                    RA().intersection_of_tables(dict1, dict2, attribute)
                else:
                    print("The attribute entered is not common to both tables. Hence Intersection cannot be done.\n")
            elif rel.lower() == "difference":
                tables = input("Please enter the tables in format: table1,table2\n")
                if "," in tables:
                    t = tables.split(",")
                    for table in self.__tables:
                        if t[0] == table.get_table_name():
                            table1 = table
                        elif t[1] == table.get_table_name():
                            table2 = table
                else:
                    print("Invalid input format. Please re-enter.\n")
                    continue
                attribute = input("Enter attribute for difference.\n")
                if attribute in table1.get_table_attributes() and attribute in table2.get_table_attributes():
                    table1_attributes = table1.get_table_attributes()
                    table2_attributes = table2.get_table_attributes()
                    dict1 = {}
                    dict2 = {}
                    for table_attribute in table1_attributes:
                        dict1[table_attribute] = []
                    for table_attribute in table2_attributes:
                        dict2[table_attribute] = []
                    for row in table1.get_tuples():
                        for index in range(len(row)):
                            dict1[table1_attributes[index]].append(row[index])
                    for row in table2.get_tuples():
                        for index in range(len(row)):
                            dict2[table2_attributes[index]].append(row[index])
                    RA().diff_pd(dict1, dict2)
                else:
                    print("The attribute entered is not common to both tables. Hence Difference cannot be done.\n")
            elif rel.lower() == "natural join":
                tables = input("Please enter the tables in format: table1,table2\n")
                if "," in tables:
                    t = tables.split(",")
                    for table in self.__tables:
                        if t[0] == table.get_table_name():
                            table1 = table
                        elif t[1] == table.get_table_name():
                            table2 = table
                else:
                    print("Invalid input format. Please re-enter.\n")
                    continue
                attribute = input("Enter attribute for natural join.\n")
                if attribute in table1.get_table_attributes() and attribute in table2.get_table_attributes():
                    table1_attributes = table1.get_table_attributes()
                    table2_attributes = table2.get_table_attributes()
                    dict1 = {}
                    dict2 = {}
                    for table_attribute in table1_attributes:
                        dict1[table_attribute] = []
                    for table_attribute in table2_attributes:
                        dict2[table_attribute] = []
                    for row in table1.get_tuples():
                        for index in range(len(row)):
                            dict1[table1_attributes[index]].append(row[index])
                    for row in table2.get_tuples():
                        for index in range(len(row)):
                            dict2[table2_attributes[index]].append(row[index])
                    RA().natural_join(table1_attributes, table2_attributes, table1.get_tuples(), table2.get_tuples())
                else:
                    print("The attribute entered is not common to both tables. Hence natural join cannot be done.\n")
            else:
                print("Invalid value entered. Please re-enter.\n")
                continue





    def delete_rows(self):
        for table in self.__tables:
            while(True):
                key = input("Enter the value of a key for table {} to remove the corresponding row, or 'list' to see the table's attributes. Enter 'quit' to exit.\n"
                            .format(table.get_table_name()))
                if key == "quit":
                    break
                elif key == "list":
                    for t in table.get_tuples():
                        print(t)
                else:
                    if table.get_foreign_key() != "":
                        count = 0
                        foreign_table = table.get_foreign_table()
                        foreign_attributes = foreign_table.get_table_attributes()
                        foreign_index = 0
                        for index in range(len(foreign_attributes)):
                            if foreign_attributes[index] == table.get_foreign_key():
                                foreign_index = index
                        tuples = foreign_table.get_tuples()
                        foreign_attribute_type = foreign_table.get_attribute_types()[foreign_index]
                        if foreign_attribute_type == "integer":
                            for row in tuples:
                                try:
                                    if int(row[foreign_index]) == int(key):
                                        print("The row cannot be deleted without maintaining cross-table integrity.\n")
                                        count += 1
                                        break
                                except:
                                    print("Enter numerical value for the key.\n")
                                    break
                        else:
                            for row in tuples:
                                if row[foreign_index] == key:
                                    print("The row cannot be deleted without maintaining cross-table integrity.\n")
                                    count += 1
                                    break
                        rows = table.get_tuples()
                        for row in rows:
                            if count == 0:
                                rows.remove(row)
                                table.set_tuple(rows)
                                print("Deleted row successfully.")
                                break
                        continue
                    count = 1
                    primary_key = table.get_key()
                    table_attributes = table.get_table_attributes()
                    table_index = 0
                    for index in range(len(table_attributes)):
                        if table_attributes[index] == primary_key:
                            table_index = index
                    if table.get_attribute_types()[table_index] == "integer":
                        tuples = table.get_tuples()
                        for row in tuples:
                            try:
                                if int(row[table_index]) == int(key):
                                    tuples.remove(row)
                                    table.set_tuple(tuples)
                                    count = 0
                                    print("Row deleted successfully.\n")
                            except:
                                print("Please enter numerical value for the key.\n")
                                break
                        if count == 1:
                            print("Row could not be deleted because of invalid values that do not exist.\n")
                    else:
                        tuples = table.get_tuples()
                        for row in tuples:
                            if row[table_index] == key:
                                tuples.remove(row)
                                table.set_tuple(tuples)
                                count = 0
                                print("Row deleted successfully.")
                        if count == 1:
                            print("Row could not be deleted because of invalid values that do not exist.\n")

    def delete_table(self):
        while(True):
            count = 0
            if len(self.__tables) > 0:
                table_name = input("Please enter the name of the table you want to delete.\n")
                deletion_table = None
                table_names = []
                for table in self.__tables:
                    table_names.append(table.get_table_name())
                if table_name not in table_names:
                    print("Table does not exist. Please enter a valid table name.\n")
                    continue
                else:
                    for table in self.__tables:
                        if table_name == table.get_table_name():
                            deletion_table = table
                            break
                    for table in self.__tables:
                            if deletion_table.get_foreign_table() != None \
                                    and deletion_table.get_foreign_table().get_table_name() == table.get_table_name():
                                print("Table deletion has cross table integrity issues. Hence cannot be deleted.\n")
                                count += 1
                if count == 0:
                    self.__tables.remove(deletion_table)
                    print("Table deleted successfully.\n")
            else:
                break
