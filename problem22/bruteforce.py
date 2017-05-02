import csv


def calc_name_sum(index, name):
    name = name.lower()
    name_value = 0
    for c in name:
        name_value += ord(c) - 96

    return index*name_value


def main():
    with open('names.txt', 'r') as names_file:
        reader = csv.reader(names_file)
        names = []
        for n in reader:
            names += n
    names = sorted(names)
    name_sum = 0
    for i in range(len(names)):
        name_sum += calc_name_sum(i+1, names[i])

    print(name_sum)

if __name__ == '__main__':
    main()
