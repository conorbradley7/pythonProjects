#Script Name: functions
#Author: Conor Bradley 119408464
#Date: Friday 27/09/2019
import math
import random

# Semester1=================================================================================================================
# ==========================================================================================================================

# Lab 2=================================================================================================================
def rugby_score():
    team1 = input('Please enter the first team: ')
    team2 = input('please enter the second team: ')

    team1_tries = int(input('Please enter the number of tries scored by the first team: '))
    team2_tries = int(input('Please enter the number of tries scored by the first team: '))

    team1_other_points = int(input('Please enter the number of points scored by team 1 '
                                   'through conversions and penalties: '))
    team2_other_points = int(input('Please enter the number of points scored by team 2 '
                                   'through conversions and penalties: '))

    total_team1 = (team1_tries * 5) + team1_other_points
    total_team2 = (team2_tries * 5) + team2_other_points

    print('Teams', '\t\t', 'Tries', '\t', 'Conversion/Penalty Points', '\t', 'Final Score')
    print('-----------------------------------------------------------------')
    print("%2.10s \t %3d \t %12.d \t %18.d" % (team1, team1_tries, team1_other_points, total_team1))
    print("%2.10s \t %3d \t %12.d \t %18.d" % (team2, team2_tries, team2_other_points, total_team2))


def separated_function(string1,string2,string_sep,string_end):
    string1 = string1.capitalize()
    string2 = string2.capitalize()
    string_sep = string_sep.capitalize()
    string_end = string_end.capitalize()
    print(string1, string2, sep=string_sep, end=string_end)

    print("The value of __name__ is:", repr(__name__))


def mathsy_problems():
    def mins_and_secs():
        mins = int(input('How Many Minutes?: '))
        seconds = int(input('How Many Seconds?: '))

        only_seconds = mins * 60 + seconds
        print(only_seconds, 'seconds', sep=' ')

    def km_to_miles():
        km = float(input('How many kilometers do you wish to convert?: '))
        miles = km * 1.61
        print(km, 'kilometers is equivalent to', miles, 'miles.', sep=' ')

    def pace_per_distance():
        ans_1 = input('Is the race length in kilometers or miles?: ')
        ans_1 = ans_1[:1].capitalize()
        if ans_1 == 'K':
            distance = int(input('How Long Was The Race in kilometers?: '))
            time = int(input('How long did the race take in MINUTES?: '))
            pace_per_distance = time / distance
            print('Your pace per kilometer was:', pace_per_distance, 'minutes per kilometer', sep=' ')
        elif ans_1 == 'M':
            distance = int(input('How Long Was The Race in miles?: '))
            time = int(input('How long did the race take in MINUTES?: '))
            pace_per_distance = time / distance
            print('Your pace per mile was:', pace_per_distance, 'minutes per mile', sep=' ')

    def average_pace():

        ans_1 = input('Is the race length in kilometers or miles?: ')
        ans_1 = ans_1[:1].capitalize()

        if ans_1 == 'K':
            print('Must you be so awkward??? We will have to convert that to miles')
            km = int(input('How manny kilometers was the race?: '))
            miles = km * 1.61
        else:
            miles = int(input('How many miles was the race?: '))

        ans_2 = input('Do you wish to enter your race time in HOURS or minutes and seconds?: ')
        ans_2 = ans_2[:1].capitalize()

        if ans_2 == 'M' and ans_1 == 'K':
            print("Why so awkward man? I don't like you.... alright let me convert that to hours *sigh")
            mins = int(input('How Many Minutes?: '))
            leftover_seconds = int(input('How Many Seconds?: '))
            hours = mins / 60 + leftover_seconds / 3600
        elif ans_2 == 'M' and ans_1 == 'M':
            print("Must you be so awkward??? We will have to convert that to hours only")
            mins = int(input('How Many Minutes?: '))
            leftover_seconds = int(input('How Many Seconds?: '))
            hours = mins / 60 + leftover_seconds / 3600
        else:
            hours = float(input('How long did the race take you in hours?: '))

        average_speed = miles / hours
        print('Your average speed was ', int(average_speed), ' mph', '(', average_speed, ' mph)', sep='')

    pace_per_distance()
    average_pace()
    km_to_miles()
    mins_and_secs()

# Lab 3 ================================================================================================================

def three_numbers(num1, num2, num3):
    if num1 == num2 == num3:
        return True
    else:
        return False


def seasons(num):
    if num == 1:
        print('Winter')

    if num == 2:
        print('Spring')

    if num == 3:
        print('Summer')

    if num == 4:
        print('Autumn')

    if num > 4 or num < 1:
        print('Error, there are only 4 seasons. Please pass through a number from 1 to 4')


def grades(num):
    if num >= 0 and num <= 24:
        print('F')
    if num >= 25 and num <= 39:
        print('E')
    if num >= 40 and num <= 54:
        print('D')
    if num >= 54 and num <= 69:
        print('C')
    if num >= 70 and num <= 84:
        print('B')
    if num >= 85 and num <= 100:
        print('A')
    if num < 0 or num > 100:
        print('Error: Minimum score = 0, Maximum scorre = 100. Please pass through a number within this range')


def equal_numbers(num1, num2):
    if num1 == num2:
        print(math.sqrt(num1))
    else:
        print('Num 1 squared = ', num1 ** 2)
        print('Num 2 squared = ', num2 ** 2)


def fizz_buzz_sem1(num):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    if num % 3 == 0 and num % 5 != 0:
        print('Fizz')
    if num % 3 != 0 and num % 5 == 0:
        print('Buzz')
    if num % 3 != 0 and num % 5 != 0:
        print(num)

# Lab 4 ================================================================================================================

def seasons_list(num):
    season = ["Winter","Spring","Summer","Autumn"]
    if num == 1:
        print(season[0])

    if num == 2:
        print(season[1])

    if num == 3:
        print(season[2])

    if num == 4:
        print(season[3])

    if num > 4 or num < 1:
        print('Error, there are only 4 seasons. Please pass through a number from 1 to 4')


def grade_or_range(grade):
    if type(grade) == int:
        if grade >= 0 and grade <= 24:
            print('F')
        if grade >= 25 and grade <= 39:
            print('E')
        if grade >= 40 and grade <= 54:
            print('D')
        if grade >= 55 and grade <= 69:
            print('C')
        if grade >= 70 and grade <= 84:
            print('B')
        if grade >= 85 and grade <= 100:
            print('A')
        if grade < 0 or grade > 100:
            print('Error: Minimum score = 0, Maximum scorre = 100. Please pass through a number within this range')
    elif type(grade) == str:
        grade.capitalize()
        if grade == "A":
            print('85-100')
        elif grade == "B":
            print('70-84')
        elif grade == "C":
            print('55-69')
        elif grade == "D":
            print('40-54')
        elif grade == "E":
            print('25-39')
        elif grade == "F":
            print('0-24')
        else:
            print('Error: Input provided is not a valid grade. Please enter a letter from A-F')
    else:
        print('Type Error: Pleae enter an  integer between 0 and 100 or a letter (string) from A to F')


def fizz_buzz_divisors(num,divisor1,divisor2):
    if num % divisor1 == 0 and num % divisor2 == 0:
        print('FizzBuzz')
    elif num % divisor1 == 0:
        print('Fizz')
    elif num % divisor2 == 0:
        print('Buzz')
    else:
        print(num, "Isn't a multiple of",divisor1,"or",divisor2, sep = ' ')

def slice_reverse(input_value):
    reversed_input_value = input_value[::-1]
    if input_value == reversed_input_value:
        print("True")
    else:
        print("False")

def add_to_list(value, list):
    if value not in list:
        list.append(value)
    list.sort()
    print(list)

# Lab 5 ================================================================================================================
def while_loop(max_number=10, even = False, factorial = False):
    i = 1
    accum = 0
    list = []
    fac = 1
    if even == True:
        if max_number > 0:
            while i <= max_number:
                if i % 2 == 0:
                    list.append(i)
                    accum += i
                    if i == 12:
                        break
                i += 1
        elif max_number < 0:
            while i >= max_number:
                if i % 2 == 0:
                    list.append(i)
                    accum += i
                    if i == -12:
                        break
                i -= 1
    elif even == False:
                if max_number > 0:
                    while i <= max_number:
                        list.append(i)
                        accum += i
                        if i == 12:
                            break
                        i += 1
                elif max_number < 0:
                    while i >= max_number:
                        list.append(i)
                        accum += i
                        if i == -12:
                            break
                        i -= 1

    if factorial == True and max_number <= 0:
        print('Error cannot obtain the factorial of a negative number')

    elif factorial == True:
        for i in range(1,list[-1]):
            fac*=i


    list.append(accum)
    if fac != 1:
        list.append(fac)
    print(list)

# Lab 6 ================================================================================================================
def count(list = 'hello',value = 'l'):
    count = 0
    i = 0
    while i < len(list):
        if list[i] == value:
            count += 1
        i += 1
    return count


def index(list = 'hello', value = 'o'):
    i = 0
    while i < len(list):
        if list[i] == value:
            break
        i+=1
    if value not in list:
        return -1
    else:
        return i


def get_value(list='hello',index=4):
    i = 0
    while i < len(list):
        if i == index:
            return list[i]
        i += 1

def insert(list='hello',index=1,value='a'):
    i = 0
    list_of_list = []
    str_output = ''

    for x in list:
        list_of_list.append(x)

    if index > len(list)-1:
        list_of_list.append(value)
    else:
        while i < len(list):
            if i == index:
                list_of_list[i] = value
            i += 1
    for z in list_of_list:
        str_output += z
    return str_output

def value_in_list(list='hello',value='l'):
    i = 0
    while i < len(list):
        if list[i] == value:
            return True
        i += 1
    else:
        return False

def concat(list1='hello',list2=' world'):
    return list1 + list2


def remove(list = 'hello',value = 'l'):
    i = 0
    while i < len(list):
        if list[i] == value:
            list = list[0:i] + list[i+1:]
            break
        i += 1
    return list

# Lab 7 ================================================================================================================
def is_stairs(list=['a','b','c']):
# Test base case
    if len(list) < 2:
        return False
        '''
        => if descending stairs reverse list to work with ascending stairs
                - means I don't have to duplicate code for each case
            => If integer list, convert them to string versions of int value and use
            ascii values as I have to do this if string input (alphabetical letters)
            anyway.... less duplicated code
            '''
    if ord(str(list[0]).lower()) > ord(str(list[1]).lower()):
        list = list[::-1]
    for i in range(len(list)-1):
        if ord(str(list[i+1]).lower()) != ord(str(list[i]).lower()) + 1:
            return False
    return True



def factorial(n=10):
    fac = 1
    # Test base cases
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 1
    # Test rest
    else:
        for x in range(1, n+1):
             fac *= x
    return fac



def gremlins(name='Gizmo'):
    for i in range(1,6):
        if okay_to_feed() == False:
            name = 'Stripe'

        if is_too_bright() == True and is_wet() == False:
            print(name, 'is no more. :(',sep = ' ')
            break
        elif is_too_bright() == True and is_wet() == True:
            print(name, 'is a triplet, but sadly is no more. :(', sep=' ')
            break
        elif is_wet() == True and is_too_bright() == False:
            print(name,'is a triplet', sep=' ')
        elif is_too_bright() == False and is_wet() == False:
            print(name, 'rules', sep = ' ')

def is_wet():
    ans = random.choice(['Wet', 'Dry'])
    if ans == 'Wet':
        return True
    else:
        return False

def okay_to_feed(time=random.randint(0,24)):
    if time > 0 and time < 4:
        return False
    else:
        return True

def is_too_bright(lux_level=random.randint(0,160)):
    if lux_level > 80:
        return True
    else:
        return False


# Semester2=================================================================================================================
# ==========================================================================================================================

# Lab1=================================================================================================================
def three_numbers_sem2(number_1, number_2, number_3):
  if ord(str(number_1)) == ord(str(number_2)) and ord(str(number_2)) == ord(str(number_3)):
    return True
  else:
   return False



def seasons_sem2(n):
    season_dict = {1:'Winter', 2:'Spring', 3:'Summer', 4:'Autumn'}
    try:
        if int(n) not in season_dict.keys():
            print(n, 'is not an acceptable value. Please input an integer between 1 and 4.')
            return seasons(input('Please enter a new input:'))
        else:
            return season_dict[int(n)]
    except Exception as e:
        error_message = "You didn't input an integer and therefore an error occurred... The error was the following: "
        return error_message + '\n' + str(e)



def grades_sem2(n):
    grade_dict = {'A': [x for x in range(85,101)], 'B': [x for x in range(70,85)],
                  'C':[x for x in range(55,70)], 'D':[x for x in range(40,55)],
                  'E':[x for x in range(25,40)], 'F': [x for x in range(0,25)]}
    try:
        for letter, range_grade in grade_dict.items():
            if (str(n)).capitalize() == letter:
                return 'Range of possible scores: ' + str(range_grade[0]) + '-' + str(range_grade[-1])
        for letter, range_grade in grade_dict.items():
            if int(n) in range_grade:
                return letter

    except Exception as e:
        return "You entered a character input outside the acceptable ranges which caused an error in the program."
    return "You entered a number input outside the acceptable range"


def slice_reverse_sem2(input_value):
    start = 0
    end = len(input_value) - 1
    while start < end:
        if input_value[start] == input_value[end]:
            start += 1
            end -= 1
        else:
            return "'" + str(input_value) + "'" + ' is not a palindrome.'
    return "'" +str(input_value) + "'" + ' is a palindrome.'


def add_to_list_sem2(value, list):
    if value not in list:
        list.append(value)
    list.sort()
    return list

# Lab2=================================================================================================================
def power():
    return [i*i for i in range(1,6) if i % 2 == 0]

def F(s1,s2):
    r = []
    e1 = -1
    e2 = -1
    while e1 < len(s1)-1:
        e1 += 1
        while e2 < len(s2)-1:
            e2 += 1
            if s1[e1] == s2[e2]:
                r += [s1[e1]]
                break
        e2 = -1
    return r


def reducedFeeEntitlement(d):
    return [x for x,y in d.items() if len(y) < 2]

def commonModules(d, s1, s2):
    return [x for x in d[s1] for y in d[s2] if x == y]

def iter_factorial(n):
    ans = 1
    counter = 1
    while counter <= n:
        ans *= counter
        counter += 1
    return ans

def fizz_buzz_sem2():
    count = 1
    while count <= 100:
        if count % 3 == 0 and count % 5 == 0:
            print('FizzBuzz')
        elif count % 3 == 0:
            print('fizz')
        elif count % 5 == 0:
            print('buzz')
        else:
            print(count)
        count +=  1
