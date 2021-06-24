def main():
    number_of_points = eval(input('Enter Number of Points: '))
    
    if number_of_points == 1:
        complete_list = [1]
        print(complete_list)
        
    else:
        pivot =get_pivot(number_of_points)

        # get the first part of the list
        list_1 = print_seq_to_pivot(pivot, number_of_points)

        #get the decending part of the list
        list_2 = print_pivot_to_end(list_1[-1])

        complete_list = list_1 + list_2
        print(complete_list)


def get_pivot(num):
    try:
        if num % 2 == 0:
            pivot = num - 1
        else:
            pivot = num
        return pivot
    except NameError:
        print('Number of Points should be an Integer')

def print_seq_to_pivot(pivot, number_of_points):
    starting_digit = 1
    list_1 = []

    if number_of_points % 2 == 0:

        while starting_digit != pivot+2:
            # print((starting_digit, pivot))
            list_1.append(starting_digit)
            starting_digit += 2
        list_1.append(starting_digit-1)
    else:
        while starting_digit != pivot:
            # print((starting_digit, pivot))
            list_1.append(starting_digit)
            starting_digit += 2
        list_1.append(starting_digit)
        starting_digit -= 1
        list_1.append(starting_digit)
        
    return list_1

def print_pivot_to_end(last_digit_from_list_1):

    stopper = 2
    list_2 = []
    while last_digit_from_list_1 != 2:
        last_digit_from_list_1 -= 2
        list_2.append(last_digit_from_list_1)
    # list_2.append(last_digit_from_list_1)

    return list_2





main()