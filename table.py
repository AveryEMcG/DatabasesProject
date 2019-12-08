
class Table:
    # To reduce the complexity of your program, the following constraints
    #are in effect:
    #  1. _at most_ four attributes for a table.
    #  2. single character (upper case) attribute names.
    #  3. the type for ALL attributes is either string or integer.
    #  4. for boolean conditions, only "attr op value" is allowed. For
    #     string type attribute, operator can only be == or <>; for int
    #     type attribute, operator can be >, >=, ==, <>, <, and <=. No
    #     need for other forms.
    __table_name = ""
    __table_attributes = []
    __attribute_types = []
    __attribute_constraints = []
    __tuples = []
    __key = ""
    __normal_form = ""
    __candidate_keys = []
    __fds = []



    def __init__(self, table_name, table_attributes, attribute_types):
        #   a. define new tables: table name, attribute names and types
        self.__table_name = table_name
        self.__table_attributes = table_attributes
        self.__attribute_types = attribute_types


    def get_table_attributes(self):
        return self.__table_attributes

    def get_attribute_types(self):
        return self.__attribute_types

    def get_table_name(self):
        return self.__table_name

    def set_attribute_constraints(self, attribute_constraints):
        self.__attribute_constraints = attribute_constraints

    def get_fds(self):
        return self.__fds

    def append_fd(self, fd):
        self.__fds.append(fd)

    def set_candidate_keys(self, candidate_keys):
        self.__candidate_keys = candidate_keys

    def set_key(self, key):
        self.__key = key

    def get_candidate_keys(self):
        return self.__candidate_keys

    def set_normal_form(self, normal_form):
        self.__normal_form = normal_form

    def checkConstraints(self):
        #  The legitimacy of constrains should be checked:
        #1. ignore conflicting Boolean conditions such as A>10 and
        #   A<5;
        #2. trivial and redundant FDs should be denied entry with a
        #   feedback to the user;
        #3. Users have the choice to remove some FDs;
        #4. trivial MVD or MVD that is trivialized by an existing FD,
        #   e.g., A->->B is trivialized by A->B or table with only two
        # attributes AB.
        #  5. foreign key designation, e.g., ssn in table roster is the
        #     key in table student. If one wants to input a tuple in roster
        #     and the ssn is non-existent, the user will be prompted to
        #     either quit the input or inserting a new tuple to the student
        #     table. if one wants to delete a record in table student,
        #     corresponding tuples in roster should also be deleted.
        pass

    def processConstraints(self):
        # The legitimacy of constrains should be checked:
        #1. ignore conflicting Boolean conditions such as A>10 and
        # A<5;
        #2. trivial and redundant FDs should be denied entry with a
        #   feedback to the user;
        #3. Users have the choice to remove some FDs;
        #4. trivial MVD or MVD that is trivialized by an existing FD,
        #  e.g., A->->B is trivialized by A->B or table with only two
        # attributes AB.
        #  5. foreign key designation, e.g., ssn in table roster is the
        #     key in table student. If one wants to input a tuple in roster
        #     and the ssn is non-existent, the user will be prompted to
        #     either quit the input or inserting a new tuple to the student
        #     table. if one wants to delete a record in table student,
        #     corresponding tuples in roster should also be deleted.
        pass

    def is_subset(self, str1, str2):
        count = 0
        for char1 in str1:
            for char2 in str2:
                if(char1 == char2):
                    count += 1
        return count == len(str1)

    def is_equivalent(self, str1, str2):
        return str1 == str2

    def compute_closure(self, lhs, rhs, seed):
        closure = ""
        while(len(closure) < len(seed)):
            closure = seed
            for index in range (0, len(lhs)):
                if(self.is_subset(lhs[index], seed)
                    and not self.is_subset(rhs[index], seed)):
                    seed += rhs[index]
        return closure

    def compute_subsets(self, remaining_attributes):
        subsets = []
        size = len(remaining_attributes)

        for index1 in range(0,(1 << size)):
            subset = ""
            for index2 in range (0, size):
                if((index1 & (1 << index2)) > 0):
                    subset += remaining_attributes[index2]
            subsets.append(subset)
        return subsets

    def generate_candidate_keys(self, lhs, rhs, attributes):
        key = ''
        keys = []
        rhs_attributes = []
        remaining_attributes = []
        for index in range(0, len(rhs)):
            attrs = list(rhs[index])
            for attr in attrs:
                if (not attr in rhs_attributes):
                    rhs_attributes.append(attr)
        for attr in attributes:
            if (attr not in rhs_attributes):
                key += attr
            else:
                remaining_attributes.append(attr)
        subsets = self.compute_subsets(remaining_attributes)
        subsets = sorted(subsets, key=len)
        # print(subsets)
        size = len(key)
        # print(key)
        for index in range(0, len(subsets)):
            seed = key + subsets[index]
            current_size = len(seed)
            # print(seed)
            if (size == current_size):
                closure = self.compute_closure(lhs, rhs, seed)
                if (len(closure) == len(attributes)):
                    keys.append(seed)
            else:
                if (len(keys) > 0):
                    return keys
                else:
                    size += 1
                    closure = self.compute_closure(lhs, rhs, seed)
                    if (len(closure) == len(attributes)):
                        keys.append(seed)

    def compute_normal_form(self, lhs, rhs, keys, attributes):
        #   c. Evaluate the NF category for the user defined DB, ask user to
        #either delete the entire table or add/remove FDs to boost 1 or
        #2NF tables to at least 3NF.
        key_attributes = ""
        for key in keys:
            for attribute in key:
                if (attribute not in key_attributes):
                    key_attributes += attribute

        non_key_attributes = ""
        for attribute in attributes:
            if (attribute not in key_attributes):
                non_key_attributes += attribute

        lhs_attributes = ""
        for group in lhs:
            for attribute in group:
                if attribute not in lhs_attributes:
                    lhs_attributes += attribute

        if len(attributes) == 2:
            return "Fifth Normal Form."
        for index1 in range(0, len(lhs)):
            for index2 in range(0, len(lhs_attributes)):
                for index3 in range(0, len(keys)):
                    if (not self.is_equivalent(lhs[index1], keys[index3]) and self.is_subset(lhs[index1], keys[
                        index3]) and not self.is_subset(rhs[index1], key_attributes)):
                        return "First Normal Form."

        count1 = 0
        count2 = 0
        for index1 in range(0, len(lhs)):
            for index2 in range(0, len(keys)):
                if (self.is_subset(rhs[index1], keys[index2]) and not self.is_equivalent(rhs[index1], keys[index2])):
                    count2 += 1
                    break
            for index2 in range(0, len(keys)):
                if (self.is_subset(keys[index2], lhs[index1])
                        or (self.is_subset(lhs[index1], keys[index2]) and self.is_subset(rhs[index1], key_attributes))):
                    count1 += 1
                    break

        if (count2 != 0 and count1 == len(lhs)):
            return "Third Normal Form."
        elif (count1 == len(lhs)):
            return "Boyce-Codd Normal Form."

        return "Second Normal Form."

    def checkFDForTuple(self):
        #   a. users can input new tuples to all tables, your system should
        #deny those that violate FDs. The foreign key designation may
        #demand additional tuples in other tables (see the example in
        #I.c).
        pass

    def findTuple(self):
        #   c. users can perform actions below for one table:
        #i) find tuples that satisfy conditions for some attributes
        pass

    def groupTuples(self):
        #c. users can perform actions below for one table:
        #i) find tuples that satisfy conditions for some attributes
        #ii) group tuples based on one or several chosen attribute
        pass

    def addTuple(self):
        #   a. users can input new tuples to all tables, your system should
        #deny those that violate FDs. The foreign key designation may
        #demand additional tuples in other tables (see the example in
        #I.c).
        pass

    def deleteTuple(self):
        #   b. users can delete a tuple based on key value, and again take
        #care of the cross-table dependencies
        pass


#   d. users can choose to perform the following operators for two
#      tables:
#       cross join, natural join, union, intersection, difference
def join(table1,table2):
    pass

def crossJoin(table1,table2):
    pass

def naturalJoin(table1, table2):
    pass

def union(table1,table2):
    pass

def intersection(table1,table2):
    pass

def difference(table1,table2):
    pass

def deleteTable(table):
    #   e. users can delete a table and ensure the across-table integrity.
    pass


