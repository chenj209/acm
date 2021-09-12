MAX_LEN = 10
DEBUG = 1
def debug_log(*msg, flag=True):
    if DEBUG and flag:
        print(*msg)

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
    digits_lst = [0] * MAX_LEN
    l = len(num_str)
    for i in range(l):
        digits_lst[i] = int(num_str[l-i-1])
    return digits_lst

def print_num(digits_lst):
    out = ""
    st = MAX_LEN - 1
    while st > 0 and digits_lst[st] == 0:
        st -= 1
    while st >= 0:
        out += str(digits_lst[st])
        st -= 1
    return out

def add_op(num1_lst, num2_lst, out_lst):
    clear_num(out_lst)
    for i in range(MAX_LEN-1):
        debug_log("adding", num1_lst[i], "and", num2_lst[i])
        out_lst[i] += num1_lst[i] + num2_lst[i]
        if out_lst[i] >= 10:
            out_lst[i+1] += 1
            out_lst[i] -=  10
        debug_log("=>", out_lst[i], "adv_bit:", out_lst[i+1])

def sub_op(num1_lst, num2_lst, out_lst):
    clear_num(out_lst)
    for i in range(MAX_LEN-1):
        debug_log("subing", num1_lst[i], "and", num2_lst[i])
        out_lst[i] += num1_lst[i] - num2_lst[i]
        if out_lst[i] < 0:
            out_lst[i+1] -= 1
            out_lst[i] +=  10
        debug_log("=>", out_lst[i], "sub_bit:", out_lst[i+1])

def mult_op(num1_lst, num2_lst, out_lst):
    clear_num(out_lst)
    for i in range(MAX_LEN-1):
        debug_log("out digit", i)
        for j in range(0, i+1):
            temp = num1_lst[j] * num2_lst[i-j]
            debug_log("temp:", temp, flag=temp)
            out_lst[i] += temp
        if out_lst[i] >= 10:
            out_lst[i+1] += out_lst[i] // 10
            out_lst[i] %= 10
        debug_log("=>", out_lst[i], "adv bit:", out_lst[i+1])

def greater_eq(num1, num2, num1_last_digit, l2):
    if (num1[num1_last_digit+l2] != 0):
        return True
    # equal length
    for i in range(l2):
        if num1[num1_last_digit+l2-1-i] > num2[l2-i-1]:
            return True
        if num1[num1_last_digit+l2-1-i] < num2[l2-i-1]:
            return False
    return True



def div_op(num1_lst, num2_lst, out_remain, out_qt):
    clear_num(out_remain)
    clear_num(out_qt)
    l1 = MAX_LEN
    while l1 >= 0 and num1_lst[l1-1] == 0:
        l1 -= 1
    l2 = MAX_LEN
    while l2 >= 0 and num2_lst[l2-1] == 0:
        l2 -= 1
    for i in range(MAX_LEN):
        out_remain[i] = num1_lst[i]

    for cur_digit in range(max(l1-l2,0),-1,-1):
        print("computing digit:", cur_digit)
        while greater_eq(out_remain,num2_lst,cur_digit,l2):
            # import ipdb; ipdb.set_trace()
            for i in range(l2):
                out_remain[cur_digit+i] -= num2_lst[i]
                if out_remain[cur_digit+i] < 0:
                    out_remain[cur_digit+i+1] -= 1
                    out_remain[cur_digit] += 10
            out_qt[cur_digit] += 1
            if DEBUG:
                print(print_num(out_remain))

    remainder_str = print_num(out_remain)
    if remainder_str:
        print("Remainder:", remainder_str)







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
    if op_name == "-":
        sub_op(num1_lst, num2_lst, out_lst)
    if op_name == "*":
        mult_op(num1_lst, num2_lst, out_lst)
    if op_name == "/":
        remainder = [0] * MAX_LEN
        div_op(num1_lst, num2_lst, remainder, out_lst)

    print("Result:", print_num(out_lst))
    return

if __name__ == "__main__":
    first_num, op, second_num = input().split()
    big_num_op(first_num, op, second_num)

