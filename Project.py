from database import Database

def main():
    database = Database()
    number_of_tables = database.validate_number_of_tables(None)
    database.trigger_table_input(number_of_tables)
    database.trigger_table_constraints()
    database.trigger_table_fd()
    database.generate_table_key()
    database.compute_normal_form()
    database.trigger_key_input()
    database.trigger_foreign_key_input()
    database.insert_rows()
    database.delete_rows()
    database.delete_table()

if __name__== "__main__":
  main()