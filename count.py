MAX_LEN = 1004
DEBUG = 1
def clear_num(digits_lst):
    assert(len(digits_lst) == MAX_LEN)
    for i in range(MAX_LEN):
        digits_lst[i] = 0

def read_num(num_str):
    """
    reads a string representing a number and store it in
    a array in reversed order, i.e. the lower digit on
    the small index
    """
    digits_lst = [0] * 1004
    l = len(num_str)
    for i in range(l):
        digits_lst[i] = int(num_str[l-i-1])
    return digits_lst

def print_num(digits_lst):
    out = ""
    st = MAX_LEN - 1
    while st >= 0 and digits_lst[st] == 0:
        st -= 1
    while st >= 0:
        out += str(digits_lst[st])
        st -= 1
    return out

def inc_op(out_lst):
    out_lst[0] += 1
    for i in range(MAX_LEN-1):
        if out_lst[i] >= 10:
            out_lst[i+1] += 1
            out_lst[i] -=  10
        if out_lst[i+1] < 10:
            break

def count_string(l):
    count = [0] * MAX_LEN
    count2 = 0
    s = [""]
    while s:
        curr = s.pop()
        if len(curr) == l:
            # if DEBUG:
                # print(curr)
            inc_op(count)
            count2 += 1
            if (str(count2) != print_num(count)):
                print("not eq:",print_num(count))
                print(count2)
        else:
            for c in ["1", "2", "3"]:
                if len(curr) < 2 or \
                        (curr[-1] != c or curr[-2] != c):
                    s.append(curr+c)
    result_count = print_num(count)
    if len(result_count) > 16:
        result_count = "......" + result_count[-10:]
    print(result_count)
    print(count2)

def count_string2(l):
    if l == 0:
        return 1
    if l == 1:
        return 3
    if l == 2:
        return 9
    if l == 3:
        return 24
    return (count_string2(l-1)-count_string2(l-4)*2)*3


if __name__ == "__main__":
    str_l = int(input())
    print(count_string(str_l))

