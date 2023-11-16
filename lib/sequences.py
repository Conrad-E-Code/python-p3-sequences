#!/usr/bin/env python3
import ipdb
# def print_fibonacci(length):
#     pass
#     fib_sequence= []
#     current_int= 0
#     while length > 0:  
#         if current_int == 0:
#             fib_sequence.append(0)
#             current_int += 1
#         elif current_int == 1:
#             fib_sequence.append(1)
#             current_int += 1
#         else:
#             fib_sequence.append(current_int) 
#             current_int += current_int
#         length -= 1
#     print(fib_sequence)
def print_fibonacci(length):
    pass
    fib_sequence= []
    while length > 0:  
        if len(fib_sequence) < 1:
            fib_sequence.append(0)
        elif len(fib_sequence) == 1:
            fib_sequence.append(1)
        else :
            end_sum= fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(end_sum)
        length -= 1
    print(fib_sequence)
    # ipdb.set_trace()
print_fibonacci(3)


