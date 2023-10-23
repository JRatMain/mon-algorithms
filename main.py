import csv
import time

mons = []
results = []


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
        'On average, it took: ' + str(average_time2) + 'nanoseconds to find the Pokémon with the highest base stat '
                                                       'total.')


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


def sort():
    global mons
    mons = sorted(mons, key=lambda x: x[4], reverse=True)


def check_type_psn(reader):
    global mons
    print("The following Pokémon have the Poison type: ")
    print('===============================================')
    for row in reader:
        if row[1] == "Name":
            continue
        name = row[1]
        t1 = row[2]
        t2 = row[3]
        if t1 == 'Poison' or t2 == 'Poison':
            print(name)
        mons.append(row)
    print('===============================================')


with open('Pokemon_numerical.csv') as mon:
    if __name__ == '__main__':
        average_time = 0
        average_time2 = 0
        reader = csv.reader(mon)
        start = time.perf_counter_ns()
        for i in range(100):
            check_type_psn(reader)
        end = time.perf_counter_ns()
        average_time = (end - start) / 100
        sort()
        start2 = time.perf_counter_ns()
        for i in range(100):
            binary_search()
        end2 = time.perf_counter_ns()
        average_time2 = (end2 - start2) / 100
        print_results(average_time, average_time2)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
