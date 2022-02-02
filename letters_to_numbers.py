# get a string as input, output the same string but each letter is its
# position in the alphabet

alphabet = "abcdefghijklmnopqrstuvwxyz"
number_letters = {1: "a",
                  2: "b",
                  3: "c",
                  4: "d",
                  5: "e",
                  6: "f",
                  7: "g",
                  8: "h",
                  9: "i",
                  10: "j",
                  11: "k",
                  12: "l",
                  13: "m",
                  14: "n",
                  15: "o",
                  16: "p",
                  17: "q",
                  18: "r",
                  19: "s",
                  20: "t",
                  21: "u",
                  22: "v",
                  23: "w",
                  24: "x",
                  25: "y",
                  26: "z"
                  }
letter_numbers = {"a": 1,
                  "b": 2,
                  "c": 3,
                  "d": 4,
                  "e": 5,
                  "f": 6,
                  "g": 7,
                  "h": 8,
                  "i": 9,
                  "j": 10,
                  "k": 11,
                  "l": 12,
                  "m": 13,
                  "n": 14,
                  "o": 15,
                  "p": 16,
                  "q": 17,
                  "r": 18,
                  "s": 19,
                  "t": 20,
                  "u": 21,
                  "v": 22,
                  "w": 23,
                  "x": 24,
                  "y": 25,
                  "z": 26
                  }


def to_numbers(in_string, as_string = True):
    """
    return a string with all letters replaced by their place in the alphabet
    :param in_string: the string to replace
    :return: string with numbers
    """
    in_string = in_string.lower()
    work_list = []
    for letter in in_string:
        if letter in alphabet:
            # print("replacing", letter, letter_numbers[letter])
            work_list.append(str(letter_numbers[letter]))
        else:
            work_list.append(letter)
    out_string = "-".join(work_list)

    if as_string:
        return out_string
    else:
        return work_list


# Bonus: digit sum, because sometimes the numbers are too big for pin codes
def digit_sum(input_list):
    """
    gets a list with integers, returns list with digit sums of original numbers
    :param in_list: list with integers
    :return: list of integers
    """
    integer_list = convert_str_to_int_list(input_list)
    digit_list = []
    for num in integer_list:
        print(num, integer_list)
        if type(num) == int:
            # calculate digit sum of num
            string_num = str(num)
            print(num)
            if len(string_num) > 1:
                for elem in string_num:
                    sum_int = + int(elem)
            else:
                sum_int = int(string_num)
            digit_list.append(sum_int)
        else:
            # single digit, just same number
            digit_list.append(num)

        return digit_list


def convert_str_to_int_list(str_list):
    """
    gets a list of numbers as strings, returns a list of numbers as integers
    :param str_list: a list of numbers as string
    :return: list of numbers as int
    """
    int_list = []
    for number in str_list:
        if number in "0123456789":
            int_list.append(int(number))
        else:
            pass
    return int_list


if __name__ == "__main__":
    input_word = "lena"  # str(input("What word do you want to convert to a string? "))
    numbered_word = to_numbers(input_word, False)
    print(numbered_word)
    digit_summed_word = digit_sum(numbered_word)
    print(digit_summed_word)

    # scendgame = "SuperCorp Endgame"
    # sceg_num = to_numbers(scendgame)
    # print(sceg_num)

    # lena = "Lena Luthor"
    # lena_num = to_numbers(lena)
    # print(lena_num)
