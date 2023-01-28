# This is it. This is when I need to start writing code.
# Yesterday I got called out in class for being distracted and I said I was working on something
# And now I need to follow through

# I think book-reading should be an easy one. Or a math computation of some kind.
# Maybe proof why order of adding digits together will come out the same. Yeah. That's a good one.
# Inputs: number
# Outputs: all possible ways of adding digits together, printed out

def print_all(n):
    s = str(n)
    for d in s:
        # I should make some tea. Black tea? To stay awake. I need to make good progress by tomorrow
        # Alice messaged me and wants to meet up to work on our essays together
        print(d)
        # Let's try an example
        # Suppose my number is 4371730
        # Then the final output needs to be...
        # 4371730: 4 + 3 + 7 + 1 + 7 + 3 + 0 = 25 => 2 + 5 = 7
        # 4|371730: 4 = 4, 3 + 7 + 1 + 7 + 3 + 0 = 21 => 4 = 4, 2 + 1 = 3 => 4 + 3 = 7
        # 43|71730: 4 + 3 = 7, 7 + 1 + 7 + 3 + 0 = 18 => 7 = 7, 1 + 8 = 9 => 7 + 9 = 16 => 1 + 6 = 7
        # 437|1730: 4 + 3 + 7 = 14, 1 + 7 + 3 + 0 = 11 => 1 + 4 = 5, 1 + 1 = 2 => 5 + 2 = 7
        # 4371|730: 4 + 3 + 7 + 1 = 15, 7 + 3 + 0 = 10 => 1 + 5 = 6, 1 + 0 = 1 => 6 + 1 = 7

        # It smells. Suspiciously so
        # Oh no, the kettle!!
        raise Exception

# Alice messaged me again, I think we are going on a real date now! It does make the kettle seem insignificant in the grand scheme of things
""""""
""""""
""""""
""""""
# It's been... a while. I should finish it up before Alice comes back from work
# She has been telling me how I should do something with all my free time, but I am busy petting my cat
# She doesn't get it

def print_summm(n):
    s = str(n)
    t = sum([int(d) for d in s])
    print(t)

def split(n):
    s = str(n)
    for i in range(len(str(n)) - 1):
        number_1 = int()

        # Alice! Alice, noooooo!!!! I will change I promise I promise
        # How can you do this to me
        # I was trying to change. Things would be different if you come back
        break


def get_TWO_numbers_from_ONE_number(ALL_number,split_poInt):
    s = str(ALL_number)
    FIRST_number = int(s[:split_poInt-1])
    SECOND_number = int(s[split_poInt:])
    return FIRST_number, SECOND_number
