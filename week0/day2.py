def count_words(arr):
    answer = {}
    for word in arr:
        if(word in answer):
            answer[word] += 1
        else:
            answer[word] = 1
    return answer


def unique_words_count(arr):
    answer = set()
    for word in arr:
        answer.add(word)
    return len(answer)


def groupby(func, seq):
    answer = {}
    for value in seq:
        answer.setdefault(func(value), []).append(value)

    return answer


def prepare_meal(number):
    answer = ""
    while(number % 3 == 0):
        answer += 'spam '
        number = number // 3
    if (len(answer) == 0 and number % 5 == 0):
        answer += 'eggs '
        number = number // 5
    while(number % 5 == 0):
        answer += 'and eggs '
        number = number // 5
    return answer


def reduce_file_path(path):
    answer = ""
    while(path.endswith('/') and len(path) > 1):
        path = path[:len(path) - 1]
    for count in range(0, path.count("..")):
        index = path.index("..")
        for step in range(index - 1, -2, -1):
            if(step == 0):
                if(path[step] == '/'):
                    answer = path[0: step + 1]
                    answer += path[index + 2:]
                    path = answer
                    break
            if(path[step - 1] == '/'):
                answer = path[0: step]
                answer += path[index + 2:]
                path = answer
                break
    path = path.replace("/.", "")
    path = path.replace("//", "/")
    return path


def is_an_bn(word):
    half_len = len(word) // 2
    left_part = word[:half_len]
    right_part = word[half_len:]
    if(len(left_part) == left_part.count('a')
    and len(right_part) == right_part.count('b')):
        if (len(left_part) == len(right_part)):
            return True
    return False


def simplify_fraction(fraction):
    import fractions
    left = max(fraction[0], fraction[1])
    right = min(fraction[0], fraction[1])
    x = 0
    while(x != 1):
        x = fractions.gcd(left, right)
        left //= x
        right //= x
    print((right, left))


def sort_fractions(fractions):
    fractions.sort(key=lambda tup: (tup[0]/tup[1]))
    return fractions


def nth_fib_lists(listA, listB, n):
    first = listA
    second = listB
    if (n <= 0):
        return False
    elif (n == 1):
        return first
    elif (n == 2):
        return second
    else:
        for x in range(2, n):
            temp = first + second
            first = second
            second = temp
        return temp


def member_of_nth_fib_lists(listA, listB, needle):
    answer = []
    n = 1
    while(answer != needle):
        answer = nth_fib_lists(listA, listB, n)
        n += 1
        if (len(answer) > len(needle)):
            return False
    return True


def is_prime(n):
    n = abs(n)
    for number in range(2, (n//2) + 1):
        if (n % number == 0):
            return False
    return True


def goldbach(n):
    answer = []
    for number in range(1, (n // 2) + 1):
        if(is_prime(number)):
            if(is_prime(n - number)):
                answer.append((number, n - number))
    return answer


def magic_square(matrix):
    sum_d1 = 0
    sum_d2 = 0
    for x in range(0, len(matrix)):
        sum_d1 += int(matrix[x][x])
        sum_d2 += int(matrix[len(matrix) - x - 1][x])
    if(sum_d1 == sum_d2):
        for row in range(0, len(matrix)):
            sum_row = 0
            sum_col = 0
            for column in range(0, len(matrix)):
                sum_row += matrix[row][column]
                sum_col += matrix[column][row]
            if (sum_row != sum_d1 or sum_col != sum_d1):
                return False
    else:
        return False
    return True


def sudoku_solved(sudoku):
    for row in range(0, len(sudoku)):
        check_set_row = set()
        check_set_col = set()
        sum_row = 0
        sum_col = 0
        for col in range(0, len(sudoku)):
            check_set_row.add(sudoku[row][col])
            sum_row += sudoku[row][col]
            check_set_col.add(sudoku[col][row])
            sum_col += sudoku[col][row]
        if(sum_row != sum_col and len(check_set_col) != len(check_set_row)):
            return False

    for row in range(0, len(sudoku), 3):
        for col in range(0, len(sudoku), 3):
            check_set = set()
            sum_square = 0
            for x in range(0, 3):
                for y in range(0, 3):
                    check_set.add(sudoku[row + x][col + y])
                    sum_square += sudoku[row + x][col + y]
            if(sum_square != 45 and len(check_set) != 9):
                return False

    return True