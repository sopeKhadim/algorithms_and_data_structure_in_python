def remove_duplicates(string):

    clean_dict = dict()
    for char in string:
        if char not in clean_dict.keys():
            clean_dict[char] = 0
        clean_dict[char] += 1
    clean_str = "".join(clean_dict.keys())

    return clean_str


def remove_space(string):

    str_array = string.split(' ')
    clean_str = "".join(str_array)

    return clean_str


def remove_duplicates_spaces(string):

    clean_dict = dict()
    for char in string:
        if char != ' ':
            if char not in clean_dict.keys():
                clean_dict[char] = 0
            clean_dict[char] += 1
    clean_str = "".join(clean_dict.keys())

    return clean_str


if __name__ == "__main__":
    s1 = "aadbddaaccbe"
    print("Remove duplicates")
    print(remove_duplicates(s1))

    s2 = " aad bd da acc be "
    print("Remove spaces")
    print(remove_space(s2))
    print("Remove duplicates and spaces")
    print(remove_duplicates_spaces(s2))

