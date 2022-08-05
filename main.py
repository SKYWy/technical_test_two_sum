"""
FUNCTION check_for_sum
Input :
the_array : python list with integer values
the_sum_value : integer 
Output : 
boolean : whether or not there exist two elements in the_array whose sum is exactly the_sum_value.
"""


def check_for_sum(the_array, the_sum_value):
    the_array.sort()
    length = len(the_array)

    for i in range(length):
        for j in range(i + 1, length):
            sum = the_array[i] + the_array[j]

            if sum == the_sum_value:
                return True

            if sum > the_sum_value:
                break

    return False


"""
MAIN
"""


def main():

    the_array = [0, -1, 2, -3, 1]
    the_sum = -2

    if check_for_sum(the_array, the_sum):
        print("Your algorithm returned the right answer. Good for you!")
    else:
        print("You got it wrong. Please try again.")


if __name__ == "__main__":
    main()
