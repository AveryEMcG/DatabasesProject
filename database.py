from table import Table
class Database:
    __tables = []

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
            table_name = input("Enter the name of table:\n")
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
