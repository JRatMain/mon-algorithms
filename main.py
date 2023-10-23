# CSV module imported for reading data from a file.
import csv
# Time module imported for tracking program run time.
import time

# Global list variables; one stores data from the csv file,
# and the other stores the results from the binary search.
mons = []
results = []


# Prints results from previous functions. Arguments include the average times (in nanoseconds)
def print_results(average_time, average_time2):
    global results
    print("These Pokémon have the highest stat total: ")
    print()
    for row in results:
        name = row[0]
        total = row[1]
        print(name + ', ' + str(total))

    print('On average, it took: ' + str(average_time) + ' nanoseconds to find every Poison type in the CSV file.')
    print(
        'On average, it took: ' + str(average_time2) + ' nanoseconds to find the Pokémon with the highest base stat '
                                                       'total.')


# Uses a binary search to find the highest base stat total for each Pokémon.
# It starts searching from the middle, going left or right in the list depending on the value of the 5th row.
def binary_search():
    global results, mons
    low = 0
    high = len(mons) - 1
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
            results = [[mons[mid][1], current_val]]

        elif current_val == max_val:
            name = mons[mid][1]
            total = mons[mid][4]
            new_mon = [name, total]
            results.append(new_mon)
            high = mid - 1

        if current_val == max_val and high == -1:
            name = mons[mid + 1][1]
            total = mons[mid + 1][4]
            new_mon = [name, total]
            results.append(new_mon)


# Creates a new list by sorting data by the 5th column in descending order
def sort():
    global mons
    mons = sorted(mons, key=lambda x: x[4], reverse=True)


# Checks for the Poison type from each row in the file.
def check_type_psn(reader):
    global mons

    for row in reader:
        if row[1] == "Name":
            continue
        name = row[1]
        t1 = row[2]
        t2 = row[3]
        if t1 == 'Poison' or t2 == 'Poison':
            print(name)
        mons.append(row)


# opens the csv file to read data from it; also the main function.
with open('Pokemon_numerical.csv') as mon:
    if __name__ == '__main__':
        average_time = 0
        average_time2 = 0
        reader = csv.reader(mon)
        print("The following Pokémon have the Poison type: ")
        print('===============================================')
        start = time.perf_counter_ns()
        for i in range(100):
            check_type_psn(reader)
        end = time.perf_counter_ns()
        print('===============================================')
        average_time = (end - start) / 100
        sort()
        start2 = time.perf_counter_ns()
        for i in range(100):
            binary_search()
        end2 = time.perf_counter_ns()
        average_time2 = (end2 - start2) / 100
        print_results(average_time, average_time2)


