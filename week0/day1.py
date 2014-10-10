def nth_fibonacci(n):
    first = 1
    second = 1
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


def sum_of_digit(n):
    if (n < 0):
        n = abs(n)
    answer = 0
    while (n > 0):
        answer += n % 10
        n = n // 10
    return answer


def sum_of_divisors(n):
    n = abs(n)
    answer = n
    for number in range(1, (n//2) + 1):
        if (n % number == 0):
            answer += number
    return answer


def is_prime(n):
    n = abs(n)
    for number in range(2, (n//2) + 1):
        if (n % number == 0):
            return False
    return True


def prime_number_of_divisors(n):
    n = abs(n)
    count = 2
    for number in range(2, (n//2) + 1):
        if (n % number == 0):
            count += 1
    return is_prime(count)


def sevens_in_a_row(arr, n):
    answer = False
    for number in range(0, len(arr) - n):
        if (arr[number] == 7):
            for step in range(number, number + n):
                if (arr[step] == 7):
                    answer = True
                else:
                    answer = False
        if (answer):
            return answer
    return answer


def is_int_palindrome(n):
    return str(n) == str(n)[::-1]


def contains_digit(number, digit):
    return str(number).find(str(digit)) != -1


def contains_digits(number, digits):
    answer = True
    for element in digits:
        answer = contains_digit(number, element)
    return answer


def is_number_balanced(n):
    number = str(n)
    if(len(number) == 1):
        return True
    left = 0
    right = 0

    for count in range(0, len(number)//2):
        left += int(number[count])
        right += int(number[len(number) - count - 1])
    return left == right


def count_substrings(haystack, needle):
    return haystack.count(needle)


def count_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    answer = 0
    for vowel in vowels:
        answer += str.count(vowel)
    return answer


def count_consonants(str):
    consonants = "bcdfghjklmnpqrstvwxz"
    answer = 0
    str = str.lower()
    for consonant in consonants:
        answer += str.count(consonant)
    return answer


def number_to_list(n):
    l = list()
    for number in str(n):
        l.append(int(number))
    return l


def list_to_number(digits):
    number = 0
    for digit in digits:
        number *= 10
        number += digit
    return number


def biggest_difference(arr):
    answer = 0
    for number in range(0, len(arr)):
        for after_number in range(number, len(arr)):
            minimum = arr[number] - arr[after_number]
            answer = min(minimum, answer)
    return answer


def is_increasing(seq):
    for index in range(0, len(seq) - 1):
        if (seq[index] >= seq[index + 1]):
            return False
    return True


def is_decreasing(seq):
    for index in range(0, len(seq) - 1):
        if (seq[index] <= seq[index + 1]):
            return False
    return True


def zero_insert(n):
    number = str(n)
    answer = ""
    for index in range(0, len(number) - 1):
        answer += number[index]
        if (number[index] == number[index + 1]):
            answer += '0'
        elif ((int(number[index]) + int(number[index + 1])) % 10 == 0):
            answer += '0'
    answer += number[len(number) - 1]
    return answer


def sum_matrix(m):
    sum = 0
    for row in m:
        for number in row:
            sum += number
    return sum


def matrix_bonus_zeros(m):
    matrix = [[0 for i in range(len(m) + 2)] for j in range(len(m[0]) + 2)]
    for row in range(0, len(m)):
        for number in range(0, len(m[row])):
            matrix[row + 1][number + 1] = m[row][number]
    return matrix


def check_damage(row, column, m):
    matrix = matrix_bonus_zeros(m)
    for x in range(row, row + 3):
        for y in range(row, row + 3):
            if (matrix[x][y] <= matrix[row + 1][column + 1]):
                if (x != (row + 1) or y != (column + 1)):
                    matrix[x][y] = 0
            else:
                matrix[x][y] = matrix[x][y] - matrix[row + 1][column + 1]
    return sum_matrix(matrix)


def matrix_bombing_plan(m):
    answer = {}
    for row in range(0, len(m)):
        for number in range(0, len(m[row])):
            answer[row, number] = check_damage(row, number, m)

    return answer


def is_hack_number(n):
    binary = str(bin(n))[2:]
    palindrome_check = False
    odd_ones_check = False
    if (binary == binary[::-1]):
        palindrome_check = True
    if (binary.count('1') % 2 == 1):
        odd_ones_check = True

    return palindrome_check and odd_ones_check


def next_hack(n):
    if (is_hack_number(n) is True):
        n += 1
    while (is_hack_number(n) is False):
        n += 1
    return n


def nan_expand(times):
    number = ""
    if (times == 0):
        return number
    number = "NaN"
    for step in range(0, times):
        number = "Not a " + number
    return number


def iterations_of_nan_expand(expanded):

    iterations_count = expanded.count("Not a ")
    if (expanded == ""):
        return 0
    elif not (expanded.endswith("NaN")):
        return False
    elif (len(expanded) != (6 * iterations_count + 3)):
        return False
    else:
        return iterations_count


def prime_factorization(n):
    answer = []
    divider = 1
    while (n > 1):
        divider += 1
        if (n % divider == 0):
            count = 1
            n = n // divider
            while (n % divider == 0):
                n = n // divider
                count += 1
            answer.append((divider, count))
    return answer


def calculate_coins(sum):
    sum *= 100
    answer = {}
    coins = [100, 50, 20, 10, 5, 2, 1]
    for coin in range(0, len(coins)):
        coin_count = 0
        while (sum >= coins[coin]):
            coin_count += 1
            sum -= coins[coin]
        answer[coins[coin]] = coin_count
    return answer


def what_is_my_sign(day, month):
    if(month == 1):
        if(day > 20):
            return("Aquarius")
        else:
            return("Capricorn")
    elif(month == 2):
        if(day > 19):
            return("Pisces")
        else:
            return("Capricorn")
    elif(month == 3):
        if(day > 20):
            return("Aries")
        else:
            return("Pisces")
    elif(month == 4):
        if(day > 20):
            return("Taurus")
        else:
            return("Aries")
    elif(month == 5):
        if(day > 21):
            return("Gemini")
        else:
            return("Taurus")
    elif(month == 6):
        if(day > 21):
            return("Cancer")
        else:
            return("Gemini")
    elif(month == 7):
        if(day > 22):
            return("Leo")
        else:
            return("Cancer")
    elif(month == 8):
        if(day > 22):
            return("Virgo")
        else:
            return("Leo")
    elif(month == 9):
        if(day > 23):
            return("Libra")
        else:
            return("Virgo")
    elif(month == 10):
        if(day > 23):
            return("Scorpio")
        else:
            return("Libra")
    elif(month == 11):
        if(day > 22):
            return("Sagittarius")
        else:
            return("Scorpio")
    else:
        if (day > 21):
            return("Capricorn")
        else:
            return("Sagittarius")