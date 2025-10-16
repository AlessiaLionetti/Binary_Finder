import time

'''
beginning of the coursework

the idea is to follow the following steps considering a given input and a given integer (N)

1. Extracting all the possible strings of a given input;
2. Converting all the substrings of the given input into decimal;
4. Creating a function just to check if a number is prime
4. Identifying all the prime numbers less than given integer (N)
5. Outputting the answer giving less than 5 primes if <6 or the first 3 smallest and last 3 largest if >6

Also including the following:

- Evaluating the error in the case the given input is a string: 'INVALID BINARY STRING'
- Evaluating the error of no prime number found: 'NO PRIME NUMBER FOUND'
- Evaluating the error if prime number is written with blank spaces: 'BLANK SPACE'
- Evaluating the error if binary number is an integer and not a string: 'INPUT MUST BE STRING'

IDEAS:

1. usage of sets as data structure into extract_substring function
PRO: no duplicates
CONS: unordered

2. usage of built-in method to convert binary into decimal (x,2) into convert_decimal function to include in the first function

3. Raising errors in main
4. Usage of lists to store all the prime


'''


'''EXTRACTION OF ALL THE POSSIBLE SUBSTRINGS FROM A BINARY NUMBER'''

#VALUES TO TEST THROUGHOUT THE WRITING OF THE CODE INSTEAD OF TAKING ALL THE EXAMPLES
# binary = '010000010110110001100101'
# max_value = 999999


#function to extract all the substrings
#1. loop of loop to check all possible combinations and store them without duplicate
#2. Converting them immediately into decimal
#3.exiting the loop in advance if possible string found above limit given

def extract_substring(binario, limit):

    dec_substring = set()

    length_binario = len(binario)

    for i in range (length_binario):
        number = 0
        #print(i)
        for j in range (i, length_binario):
            #print(j)
            #print('//')
            number = number * 2 + int(binario[j])
            #print (number)
            if number >= limit:
                break
            dec_substring.add(number)


    return dec_substring

'''TEST extract_substring function'''
#print(extract_substring(binary, max_value))



'''PRIME FUNCTION'''

#single function to check only if a single value is a prime number
#it will then be used in the main function in a loop
#1. check first if number equal 2 to return True because it is prime
#2. Then return false if it is below 1 or 0 and if it is divisible by 2
#3. Then loop in range 3 and square root of given int by checking odd numbers only with module != 0

def is_prime(num):

    if num == 2:
        return True

    if num <= 1 or num % 2 == 0:
        return False

    for x in range(3, int(num ** 0.5) + 1, 2):
        if num % x == 0:
            return False

    return True

'''MAIN FUNCTION'''

#main function raising all the errors
#creation of an empty list where to store prime numbers
#1. first we store all the substrings into a variable called substring
#2. then we check if any of the substrings (decimal) found are prime numbers and, we store them into an empty list
#3. prime_lst has to be sorted and if length >6 then return a list with 3 smallest and 3 largest


def main(bin_string, li):

    if not isinstance(bin_string,str):
        raise TypeError('Input must be string.')

    if not isinstance(li,int):
        raise TypeError('Limit must be an integer value.')

    if " " in bin_string:
        raise ValueError('There are blank spaces in your string, make sure there is no gap')

    if set(bin_string) - {'0', '1'}:
        raise ValueError('String must contain only 0s and 1s')

    #decimal substring
    substrings = extract_substring(bin_string, li)

    #TEST SUBSTRINGS
    #print(substrings)

    #checking prime numbers inside the set of substrings and moving them into a list
    prime_lst = [sub for sub in substrings if is_prime(sub)]
    # print(prime_lst)

    #handling the case if not prime number is found
    if not prime_lst:
        return 'No prime number found'

    prime_lst.sort()
    #print(prime_lst.sort())
    length_lst = len(prime_lst)
    #print(length_lst, end=":")




    if length_lst >= 6:
        return prime_lst[:3] + prime_lst[-3:]
    else:
        return prime_lst




    #TEST ORDERED PRIME NUMBERS
    #print(ordered_lst)

# print(main("0100000101001100", 123456))


tests = [("0100001101001111", 999999),
             ("01000011010011110100110101010000", 999999),
             ("1111111111111111111111111111111111111111", 999999),
            ("0100000101001100", 123456),
             ("010000110100111101001101010100000011000100111000", 999999999),
             ("01000011010011110100110101010000001100010011100000110001", 123456789012),
             ("0100001101001111010011010101000000110001001110000011000100111001", 123456789012345),
             ("010000110100111101001101010100000011000100111000001100010011100100100001", 123456789012345678),
             ("01000011010011110100110101010000001100010011100000110001001110010010000101000001", 1234567890123456789),
             ("0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100", 1234567890123456789),
             ("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011", 12345678901234567890)
    ]

tot_time = []

for t in tests:
    start = time.time()
    print(main(t[0], t[1]))

    result = time.time()-start
    print(result)

    tot_time.append(result)

print(sum(tot_time))





