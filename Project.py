from database import Database
from table import Table
from fd import FD
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
    tables = database.get_tables()
    for table in tables:
        print(table.get_attribute_constraints())
    database.trigger_table_fd()
    database.generate_table_key()
    database.compute_normal_form()
    database.trigger_key_input()
    database.insert_rows()
    #database.trigger_foregin_key(tables)
    #database.trigger_table_mvds(tables)
    #for index in range(len(number_of_tables)):

    pass

if __name__== "__main__":
  main()