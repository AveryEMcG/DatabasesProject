import Database
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

    def generateCandidateKeys(self):
        pass

    def checkNF(self):
        #   c. Evaluate the NF category for the user defined DB, ask user to 
        #either delete the entire table or add/remove FDs to boost 1 or
        #2NF tables to at least 3NF.
        pass

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


#ToDO: I/O
def main():
    # b. for each defined table ask users to input possible constraints, including Boolean conditions, FDs and MVDs (in this order)
    
    #   d. ask users to define keys for each table, if the user-defined keys
    #  disagree the keys reached by its FDs, deny them and make reasonable
    #  suggestions to the users.

    # a. users can input new tuples to all tables, your system should
    #deny those that violate FDs. The foreign key designation may
    #demand additional tuples in other tables (see the example in
    #I.c).
    database = Database()
    number_of_tables = database.validate_number_of_tables(None)
    database.trigger_table_input(number_of_tables)
    database.trigger_table_constraints()
    #for index in range(len(number_of_tables)):

    pass
  
if __name__== "__main__":
  main()