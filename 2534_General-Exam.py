while True:
    try:
        N, Q = input().split()
        number_grades = []
        for i in range(int(N)):
            num = int(input())
            number_grades.append(num)
        number_position = []
        for i in range(int(Q)):
            num = int(input())
            number_position.append(num)
        number_grades.sort(reverse=True)
        for i in range(int(Q)):
            print(number_grades[number_position[i] - 1])
    except EOFError:
        break