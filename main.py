import csv
import time

mons = []
results = []


def print_results():
    global results
    print("These Pokémon have the highest stat total: ")
    print()
    for row in results:
        name = row[0]
        total = row[1]
        print(name + ', ' + total)


def binary_search(mons):
    global results
    for row in mons:
        low = 0
        high = len(mons) - 1
        mid = 0
        max_val = int(0)
        while low <= high:
            mid = (high + low) // 2
            current_val = int(mons[mid][4])

            # If x is greater, ignore left half
            if current_val < max_val:
                low = mid + 1

            # If x is smaller, ignore right half
            elif current_val > max_val:
                high = mid - 1
                max_val = current_val
                results.clear()
                results.append([mons[mid][1], str(current_val)])
            elif current_val == max_val:
                high = mid - 1
                name = mons[mid][1]
                total = mons[mid][4]
                results.append([name, total])

    print(max_val)


# If we reach here, then the element was not present


def max_total():
    global mons
    max = 0
    for row in mons:
        num = row[0]
        name = row[1]
        print(row)
        total = int(row[4])

        if total > max:
            max = total


def sort():
    global mons
    mons = sorted(mons, key=lambda x: x[4], reverse=True)


def check_type_psn(reader):
    global mons
    print("The following Pokémon have the Poison type: ")
    print()
    for row in reader:
        if row[1] == "Name":
            continue
        name = row[1]
        t1 = row[2]
        t2 = row[3]
        legend = bool(row[12])
        if t1 == 'Poison' or t2 == 'Poison':
            print(name)
        mons.append(row)


with open('Pokemon_numerical.csv') as mon:
    if __name__ == '__main__':
        reader = csv.reader(mon)
        check_type_psn(reader)
        sort()
        binary_search(mons)
        print_results()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
