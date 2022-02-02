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


def to_numbers(in_string):
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
    return out_string


if __name__ == "__main__":
    input_word = str(input("What word do you want to convert to a string? "))
    new_word = to_numbers(input_word)
    print(new_word)
    # scendgame = "SuperCorp Endgame"
    # sceg_num = to_numbers(scendgame)
    # print(sceg_num)

    # lena = "Lena Luthor"
    # lena_num = to_numbers(lena)
    # print(lena_num)
