MAX_LEN = 1004
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

def add_op(num1_lst, num2_lst, out_lst):
    clear_num(out_lst)
    for i in range(MAX_LEN-1):
        out_lst[i] += num1_lst[i] + num2_lst[i]
        if out_lst[i] >= 10:
            out_lst[i+1] += 1
            out_lst[i] -=  10

if __name__ == "__main__":
    num1, num2 = input().split()
    num1_l = read_num(num1)
    num2_l = read_num(num2)
    out = [0] * MAX_LEN
    add_op(num1_l, num2_l, out)
    print(print_num(out))
