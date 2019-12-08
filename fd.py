class FD:

    def is_equivalent(self, str1, str2):
        str1 = "".join(sorted(str1))
        str2 = "".join(sorted(str2))
        return str1 == str2


    def trigger_fd_input(self, table):
        name = table.get_table_name()
        table_attributes = table.get_table_attributes()
        print("The attribute list for table {} are {}".format(name, table_attributes))
        print("Please enter the FDs for table {} in format: A->B\nOr enter 'quit' to stop entering fds"
              " and 'delete' to delete fds.".format(name))
        while(True):
            fd = input()
            if fd == "quit":
                break
            if fd == "delete":
                count = 0
                fds = table.get_fds()
                fd = input("Enter the Functional dependency you want to remove from {}\n".format(fds))
                while(count == 0):
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
                        print("Invalid Functional Dependency. The attribute {} does not exist.".format(attribute))
                        count += 1
                        break
                for attribute in rhs:
                    if attribute not in table_attributes:
                        print("Invalid Functional Dependency. The attribute {} does not exist.".format(attribute))
                        count += 1
                        break
                if count == 0:
                    fds = table.get_fds()
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
                        table.append_fd(fd)
                        print("Valid Functional Dependency.")
                    else:
                        print("Trivial Functional Dependency. Can be derived from others.")
            else:
                print("Please enter Functional Dependencies in format A->B with uppercase attributes.")