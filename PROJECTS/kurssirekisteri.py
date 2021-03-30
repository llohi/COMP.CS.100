"""
COMP.CS.100 Kurssirekisteri
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def check_file(file):
    """
    check for errors with file
    """

    rows = []

    # check for correct data format
    try:
        for row in file:

            row = row.rstrip().split(";")

            if len(row) != 3:

                print("Error in file!")
                return

            else:

                rows.append(row)

        return rows

    except TypeError:
        print("Error in file!")
        return


def sort_data(data):
    """
    return data format:
        {'dep_1 ': {'course': credit}, 'dep_2': {'course': credit}}
    """

    outer_dict = {}

    for row in data:

        inner_dict = {}

        # add dictionaries to correct departments
        if row[0] not in outer_dict:

            inner_dict[row[1]] = int(row[2])
            outer_dict[row[0]] = inner_dict

        else:

            inner_dict.update({row[1]: int(row[2])})
            outer_dict[row[0]][row[1]] = int(row[2])

        # sort data into correct order
        for key in outer_dict:

            outer_dict[key] = dict(sorted(outer_dict[key].items()))

    return outer_dict


def print_all(data):
    """
    print all data in dict
    """

    for dep in sorted(data.keys()):
        print("*{}*".format(dep))

        for course in sorted(data[dep].keys()):
            print("{} : {} cr".format(course, data[dep][course]))


def print_dep(data, dep):
    """
    prind data for department
    """
    if dep in data:
        print("*{}*".format(dep))

        for course in sorted(data[dep].keys()):
            print("{} : {} cr".format(course, data[dep][course]))

    else:
        print("Department not found!")


def calculate_credits(data, dep):
    """
    calculate total credits in department
    """
    if dep in data:

        sum = 0
        for course in data[dep]:
            sum += data[dep][course]

        print("Department {} has to offer {} cr.".format(dep, sum))

    else:
        print("Department not found!")


def add(data, dep, course, credit):
    """
    add department and course to data
    """
    if dep in data:
        data[dep][course] = int(credit)
        print("\nAdded course {} to department {}".format(course, dep))

    else:
        data[dep] = {course: int(credit)}
        print("\nAdded department {} with course {}".format(dep, course))


def delete(command, data, dep, course, credit):
    """
    delete department and/or course from data
    """
    if command == "d {}".format(dep):

        if dep in data:
            data.pop(dep)
            print("\nDepartment {} removed.".format(dep))

        else:
            print("\nDepartment {} not found!".format(dep))

    # DELETE COURSE A: course title has no integer
    # course -> credit due to method at beginning of function
    elif command == "d {} {}".format(dep, credit):

        if credit in data[dep]:
            data[dep].pop(credit)
            print("\nDepartment {} course {} removed.".format(dep, credit))

        else:
            print("\nCourse {} from {} not found!".format(course, dep))

    # DELETE COURSE B: course title has integer
    # last integer -> credit due to method at beginning of function
    elif command == "d {} {} {}".format(dep, course, credit):

        # notice previous method takes last number as credit
        course = "{} {}".format(course, credit)

        if course in data[dep]:
            data[dep].pop(course)
            print("\nDepartment {} course {} removed.".format(dep, course))

        else:
            print("\nCourse {} from {} not found!".format(course, dep))


def command_line(data):
    """
    -> create command line
    -> execute user input
    """

    command = ""

    while command != "q":

        # prompt user
        print("\n[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int department / [Q]uit")
        command = input("Enter command: ")

        # declare parts of command
        cmd = ""
        dep = ""
        course = ""
        credit = ""

        # divide command into parts
        if len(command.split()) == 2:
            dep = command.split()[1]

        elif len(command.split()) > 2:
            cmd = command.split()[0]
            dep = command.split()[1]
            credit = command.split()[-1]

            # course = FULL COMMAND - cmd - dep - credit
            course = command.split()
            course.remove(cmd)
            course.remove(dep)
            course.remove(credit)
            course = " ".join(course)

        # PRINT ALL
        if command == "p":
            print()
            print_all(data)

        # PRINT DEPARTMENT
        elif command == "r {}".format(dep):
            print()
            print_dep(data, dep)

        # CALCULATE DEPARTMENT CREDITS
        elif command == "c {}".format(dep):
            print()
            calculate_credits(data, dep)

        # ADD
        elif command == "a {} {} {}".format(dep, course, credit):

            add(data, dep, course, credit)

        # DELETE DEPARTMENT
        elif command.split()[0] == "d":
            delete(command, data, dep, course, credit)

        # QUIT PROGRAM
        elif command == "q":
            pass

        # INVALID COMMAND
        else:
            print("Invalid command!")

    print("Ending program.")


def main():

    filename = input("Enter file name: ")
    # check for OSError
    try:

        file = open(filename, mode="r")

    except OSError:

        print("Error opening file!")
        return

    # check for errors
    data = check_file(file)

    # break function if data is empty
    if data == None:
        return

    else:
        pass

    # txt file -> dict
    data = sort_data(data)
    command_line(data)


if __name__ == "__main__":
    main()
