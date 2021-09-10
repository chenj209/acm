if __name__ == "__main__":
    num_students = int(input())
    inc_flag = bool(int(input()))
    print(inc_flag)
    grades_pair = []
    for i in range(num_students):
        pair_str = input().split()
        name = pair_str[0]
        grade = pair_str[1]
        grades_pair.append((name, grade))
    grades_pair.sort(key = lambda p: float(p[1]), reverse=inc_flag)
    for i in range(num_students):
        print(grades_pair[i][0] + " " + str(grades_pair[i][1]))
