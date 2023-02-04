# HMMMM what should i do
# I think book-reading should be an easy one. Or a math computation of some kind.
# Inputs: number
# Outputs: all possible ways of adding digits together, printed out

def print_all(n):
    s = str(n)
    for d in s:
        # I should make some tea. Black tea? To stay awake. I need to make good progress by tomorrow
        print(d)
        # Let's try an example
        # Suppose my number is 4371730
        # Then the final output needs to be...
        # 4371730:
        # 4 + 3 + 7 + 1 + 7 + 3 + 0 = 25 =>
        # 2 + 5 = 7
        # 4|371730:
        # 4 = 4, 3 + 7 + 1 + 7 + 3 + 0 = 21 =>
        # 4 = 4, 2 + 1 = 3 =>
        # 4 + 3 = 7
        # 43|71730: 4 + 3 = 7, 7 + 1 + 7 + 3 + 0 = 18 => 7 = 7, 1 + 8 = 9 => 7 + 9 = 16 => 1 + 6 = 7
        # 437|1730: 4 + 3 + 7 = 14, 1 + 7 + 3 + 0 = 11 => 1 + 4 = 5, 1 + 1 = 2 => 5 + 2 = 7
        # 4371|730: 4 + 3 + 7 + 1 = 15, 7 + 3 + 0 = 10 => 1 + 5 = 6, 1 + 0 = 1 => 6 + 1 = 7
        # It's cool that it's always 7. The proof is actually in the fact that we work with a decimal system but this is a neat little demonstration that it does work

        # It smells. Suspiciously so
        # Oh no, the kettle!!
        raise Exception

def print_summm(n):
    s = str(n)
    t = sum([int(d) for d in s])
    return t

def get_TWO_numbers_from_ONE_number(ALL_number,split_poInt):
    s = str(ALL_number)
    FIRST_number = int(s[:split_poInt+1])
    SECOND_number = int(s[split_poInt+1:])
    return FIRST_number, SECOND_number

def split_and_print(numberone,numbertwo):
    print("{} = {}, {} = {}".format(" + ".join(map(str, str(numberone))), print_summm(numberone),
                                       " + ".join(map(str, str(numbertwo))),
                                       print_summm(numbertwo)))
    numberone = print_summm(numberone)
    numbertwo = print_summm(numbertwo)
    if len(str(numberone)) > 1 or len(str(numbertwo)) > 1:
        #print(len(str(numberone)), len(str(numbertwo)))
        split_and_print(numberone, numbertwo)
    return print_summm(numberone), print_summm(numbertwo)

def do_it_all(n):
    n = str(n)
    for i in range(len(n)-1):   # for 4371730 it would be 0,1,2,3,4,5
        a_number, another_number_second_part = get_TWO_numbers_from_ONE_number(n,i)
        print("{}|{}:".format(a_number, another_number_second_part))
        #print(split_and_print(a_number, another_number_second_part))
        finsum1, finsumm2 = split_and_print(a_number, another_number_second_part)
        if len(str(finsum1 + finsumm2)) > 1:
            summm = str(finsum1 + finsumm2)
            print("{} + {} = {}".format(finsum1, finsumm2, finsum1 + finsumm2))
            print("{} + {} = {}{}{}".format(int(summm[0]), int(summm[1]), '\033[1m', int(summm[0]) + int(summm[1]), '\033[0m'))
        else:
            print("{} + {} = {}{}{}".format(finsum1, finsumm2, '\033[1m', finsum1 + finsumm2, '\033[0m'))


do_it_all(4371730)


