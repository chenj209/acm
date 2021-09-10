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

def add_op(num1_lst, num2_lst, out_lst):
    clear_num(out_lst)
    adv_bit = 0
    for i in range(MAX_LEN):
        if DEBUG:
            print("adding", num1_lst[i], "and", num2_lst[i])
        if not (adv_bit or num1_lst[i] or num2_lst[i]):
            break
        cur_bit = num1_lst[i] + num2_lst[i] + adv_bit
        if cur_bit >= 10:
            adv_bit = 1
            cur_bit %= 10
        else:
            adv_bit = 0
        out_lst[i] = cur_bit
        if DEBUG:
            print("=>", out_lst[i], "adv_bit:", adv_bit)

def big_num_op(num1, op_name, num2):
    num1_lst = read_num(num1)
    # print("num1_lst", num1_lst)
    print("print_num 1:", print_num(num1_lst))
    num2_lst = read_num(num2)
    # print("num2_lst", num2_lst)
    print("op name:", op_name)
    print("print_num 2:", print_num(num2_lst))
    out_lst = [0] * MAX_LEN
    if op_name == "+":
        add_op(num1_lst, num2_lst, out_lst)
    print("Result:", print_num(out_lst))
    return

if __name__ == "__main__":
    first_num, op, second_num = input().split()
    big_num_op(first_num, op, second_num)

