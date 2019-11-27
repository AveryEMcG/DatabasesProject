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
                if(number_of_attributes < 5 and number_of_attributes > 1):
                    print("Please enter a positive integer between 1 and 5 for table {}\n".format(table_name))
                    number_of_attributes = None
            except:
                print("Please enter a positive integer between 1 and 5 for table {}\n".format(table_name))
        return number_of_attributes



    def trigger_table_input(self, number_of_tables):
        for index1 in range(len(number_of_tables)):
            table_name = input("Enter the name of table:\n")
            number_of_attributes = self.validate_number_of_attributes(table_name, None)
            for index2 in range(number_of_attributes):
                print("hello.")
        pass


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



    def __init__(self,name,attributes):
        #   a. define new tables: table name, attribute names and types 
        pass

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

    #for index in range(len(number_of_tables)):

    pass
  
if __name__== "__main__":
  main()