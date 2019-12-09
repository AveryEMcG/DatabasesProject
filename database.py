from table import Table
from fd import FD
from mvd import MVD
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
                      "for attribute {}  or enter @$ to finish entering constraints for the attribute\n"
                      .format(table_attributes[index2]))
                string_attribute_constraints = {"==" : [], "<>" : []}
                integer_attribute_constraints = {"==" : [], "<>" :[], "<=" : [], "<" :[], ">" : [], ">=" :[]}
                while(True):
                    constraint = input()
                    if(constraint == '@$'):
                        break
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
                                print("Valid constraint.")
                            else:
                                print("Invalid constraint. Exists in not equal constraint.")
                        elif "<>" in constraint:
                            if len(string_attribute_constraints["=="]) > 0:
                                print("Invalid constraint. Equality constraint already exists.")
                            else:
                                string_attribute_constraints["<>"].append(constraint.split("<>")[1])
                                print("Valid constraint.")
                        else :
                            print("Please enter == or <> as the constraints for string type.")
                    # Pending for integer data-type.
                    else:
                        if "==" in constraint:
                            try:
                                int(constraint.split("==")[1])
                            except:
                                print("Invalid constraint. Enter a numerical value for comparison.")
                                continue
                            if (len(integer_attribute_constraints["=="]) == 1):
                                print("Invalid constraint. Equals constraint already exists. Please enter others.")
                                continue
                            elif(constraint.split("==")[1] not in integer_attribute_constraints["<>"]):
                                count = 0
                                if len(integer_attribute_constraints["<"]) > 0:
                                    print("Invalid constraint. Less than constraint exists with {}.".format(
                                        integer_attribute_constraints["<"][0]))
                                    count += 1
                                if len(integer_attribute_constraints["<="]) > 0:
                                    print("Invalid constraint. Less than equal to constraint exists with {}.".format(
                                        integer_attribute_constraints["<="][0]))
                                    count += 1
                                if len(integer_attribute_constraints[">"]) > 0:
                                    print("Invalid constraint. Greater than constraint exists with {}.".format(
                                        integer_attribute_constraints[">"][0]))
                                    count += 1
                                if len(integer_attribute_constraints[">="]) > 0:
                                    print("Invalid constraint. Greater than equal to constraint exists with {}.".format(
                                        integer_attribute_constraints[">="][0]))
                                    count += 1
                                if len(integer_attribute_constraints["<>"]) > 0:
                                    print("Invalid constraint. Not equal to constraint exists with {}.".format(
                                        integer_attribute_constraints["<>"][0]))
                                    count += 1
                                if count == 0:
                                    integer_attribute_constraints["=="].append(constraint.split("==")[1])
                                    print("Valid constraint.")
                            else:
                                print("Invalid constraint. The value exists as an inequality constraint.")
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
                                print("Invalid constraint. Equality constraint already exists with".format(
                                    integer_attribute_constraints["=="][0]))
                            if len(integer_attribute_constraints["<"]) > 0:
                                if int(constraint.split(">")[1]) > int(integer_attribute_constraints["<"][0]):
                                    print("Invalid constraint. Enter values less than {}".format(
                                        int(integer_attribute_constraints["<"][0]) - 1))
                                    count += 1
                            if len(integer_attribute_constraints["<="]) > 0:
                                if int(constraint.split(">")[1]) > int(integer_attribute_constraints["<="][0]):
                                    print("Invalid constraint. Enter values less than {}".format(
                                        integer_attribute_constraints["<="][0]))
                                    count += 1
                            if len(integer_attribute_constraints[">="]) > 0:
                                if int(constraint.split(">")[1]) > int(integer_attribute_constraints[">="][0]):
                                    print("Invalid constraint. Enter values less than {}".format(
                                        integer_attribute_constraints[">="][0]))
                                    count += 1
                            if len(integer_attribute_constraints[">"]) > 0:
                                count += 1
                                print("Invalid constraint. Greater than constraint already exists.")
                            if count == 0:
                                print("Valid constraint.")
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
                                print("Invalid constraint. Equality constraint already exists with {}".format(
                                    integer_attribute_constraints["=="][0]))
                            if len(integer_attribute_constraints["<"]) > 0:
                                    if int(constraint.split(">=")[1]) > int(integer_attribute_constraints["<"][0]):
                                        print("Invalid constraint. Enter values less than {}".format(int(integer_attribute_constraints["<"][0]) - 1))
                                        count += 1
                            if len(integer_attribute_constraints["<="]) > 0:
                                    if int(constraint.split(">=")[1]) > int(integer_attribute_constraints["<="][0]):
                                        print("Invalid constraint. Enter values less than {}".format(
                                            integer_attribute_constraints["<="][0]))
                                        count += 1
                            if len(integer_attribute_constraints[">"]) > 0:
                                if int(constraint.split(">=")[1]) <= int(integer_attribute_constraints[">"][0]):
                                    print("Invalid constraint. Enter values greater than {}".format(
                                        integer_attribute_constraints[">"][0]))
                                    count += 1
                            if len(integer_attribute_constraints[">="]) > 0:
                                count += 1
                                print("Invalid constraint. Greater than equal to constraint already exists.")
                            if count == 0:
                                print("Valid constraint.")
                                integer_attribute_constraints[">="].append(constraint.split(">=")[1])
                        elif "<" in constraint and "<=" not in constraint:
                            count = 0
                            try:
                                int(constraint.split("<")[1])
                            except:
                                print("Invalid constraint. Enter a numerical value for comparison.")
                                continue
                            if len(integer_attribute_constraints["=="]) > 0:
                                count += 1
                                print("Invalid constraint. Equality constraint already exists with {}".format(
                                    integer_attribute_constraints["=="][0]))
                            if len(integer_attribute_constraints[">"]) > 0:
                                if int(constraint.split("<")[1]) < int(integer_attribute_constraints[">"][0]):
                                    print("Invalid constraint. Enter values greater than {}".format(
                                        int(integer_attribute_constraints[">"][0]) + 1))
                                    count += 1
                            if len(integer_attribute_constraints[">="]) > 0:
                                if int(constraint.split("<")[1]) < int(integer_attribute_constraints[">="][0]):
                                    print("Invalid constraint. Enter values greater than {}".format(
                                        integer_attribute_constraints[">="][0]))
                                    count += 1
                            if len(integer_attribute_constraints["<="]) > 0:
                                if int(constraint.split("<")[1]) < int(integer_attribute_constraints["<="][0]):
                                    print("Invalid constraint. Enter values greater than {}".format(
                                        integer_attribute_constraints["<="][0]))
                                    count += 1
                            if len(integer_attribute_constraints["<"]) > 0:
                                count += 1
                                print("Invalid constraint. Less than constraint already exists.")
                            if count == 0:
                                print("Valid constraint.")
                                integer_attribute_constraints["<"].append(constraint.split("<")[1])
                        elif "<=" in constraint:
                            count = 0
                            try:
                                int(constraint.split("<=")[1])
                            except:
                                print("Invalid constraint. Enter a numerical value for comparison.")
                                continue
                            if len(integer_attribute_constraints["=="]) > 0:
                                count += 1
                                print("Invalid constraint. Equality constraint already exists with {}".format(
                                    integer_attribute_constraints["=="][0]))
                            if len(integer_attribute_constraints[">"]) > 0:
                                if int(constraint.split("<=")[1]) < int(integer_attribute_constraints[">"][0]):
                                    print("Invalid constraint. Enter values greater than {}".format(
                                        int(integer_attribute_constraints[">"][0])))
                                    count += 1
                            if len(integer_attribute_constraints[">="]) > 0:
                                if int(constraint.split("<=")[1]) < int(integer_attribute_constraints[">="][0]):
                                    print("Invalid constraint. Enter values greater than {}".format(
                                        integer_attribute_constraints[">="][0]))
                                    count += 1
                            if len(integer_attribute_constraints["<"]) > 0:
                                if int(constraint.split("<=")[1]) >= int(integer_attribute_constraints["<"][0]):
                                    print("Invalid constraint. Enter values less than {}".format(
                                        integer_attribute_constraints["<"][0]))
                                    count += 1
                            if len(integer_attribute_constraints["<="]) > 0:
                                count += 1
                                print("Invalid constraint. Less than equal to constraint already exists.")
                            if (count == 0):
                                print("Valid constraint.")
                                integer_attribute_constraints["<="].append(
                                        constraint.split("<=")[1])
                        else:
                            print("Invalid constraint. Enter valid constraints from <, <=, ==, <>, >=, and >.")
                            continue
                if(attribute_types[index2] == "string"):
                    attribute_constraints.append(string_attribute_constraints)
                else:
                    attribute_constraints.append(integer_attribute_constraints)
            self.__tables[index1].set_attribute_constraints(attribute_constraints)

    def trigger_table_fd(self):
        fd = FD()
        for table in self.__tables:
            fd.trigger_fd_input(table)

    def trigger_table_mvds(self):
        mvd = MVD()
        for table in self.__tables:
            mvd.define_MVDs(table.get_table_attributes(), len(table.get_table_attributes()))

    def generate_table_key(self):
        for table in self.__tables:
            fds = table.get_fds()
            fd_left = []
            fd_right = []
            for fd in fds:
                attributes = fd.split("->")
                fd_left.append(attributes[0])
                fd_right.append(attributes[1])
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
            table.set_normal_form(normal_form)

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


    def insert_rows(self):
        for table in self.__tables:
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
                tuple = row.split(",")
                if(len(tuple) == len(table.get_table_attributes())):
                    types = table.get_attribute_types()
                    for index in range(0, len(types)):
                        if types[index] == "integer":
                            try:
                                int(tuple[index])
                                for constraint, values in table.get_attribute_constraints()[index].items():
                                    if constraint == "==" and len(values) > 0:
                                        if(tuple[index] != int(values[0])):
                                            count+=1
                                            print("Invalid Value. Enter values equal to {}\n".format(values[0]))
                                            break
                                    elif constraint == "<>" and len(values) > 0:
                                        for value in values:
                                            if(tuple[index] == value):
                                                count+=1
                                                print("Invalid Value. Enter values not equal to {}\n".format(value))
                                                break
                                    elif constraint == "<" and len(values) > 0:
                                        if tuple[index] >= values[0]:
                                            count+=1
                                            print("Invalid Value. Enter values less than {}\n".format(values[0]))
                                            break
                                    elif constraint == "<=" and len(values) > 0:
                                        if tuple[index] > values[0]:
                                            count += 1
                                            print("Invalid Value. Enter values less than equal to {}\n".format(values[0]))
                                            break
                                    elif constraint == ">=" and len(values) > 0:
                                        if tuple[index] < values[0]:
                                            count += 1
                                            print("Invalid Value. Enter values greater than equal to {}\n".format(values[0]))
                                            break
                                    elif constraint == ">" and len(values) > 0:
                                        if tuple[index] <= values[0]:
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
                        table.append_tuple(tuple)
                        print("Valid value. Added to the table {}".format(table.get_table_name()))
                else:
                    print("The number of values do not match the attributes. Please re-enter.")

