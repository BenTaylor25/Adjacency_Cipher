'''
Elevator question

JLQ VRI FBZ WMO ADK GAZ AUE CIN GLR DBQ EPI XUK ZQX CHP OXJ WPH SZG SLK WLP OSE MAS LQC DBV ZUM JQN RZF VLN KZC QBT WOL ZXG RUF QAW OUB LJV EMQ BLJ HAO TMY ZGX TWB
'''

from random import randint as rnd, choice as rch

get_key = lambda n1, n2 : n2 - n1

def get_code():
    while True:
        code_string = input("code: ")
        chars_valid = not len(list(filter( 
            lambda x : x!=' ' and not ord(x) in range(65, 91), code_string.upper()
        )))
        code_list = code_string.upper().split()
        lens = list(map(lambda x : len(x), code_list))

        if chars_valid and len(lens) and max(lens)==min(lens)==3:   # repeat until
            return code_list
        else:
            print(f"The input '{code_string}' is not valid")


def code_to_char(code):
    key = get_key(ord(code[0]), ord(code[1]))
    return chr(ord(code[2])+key)


def solve():
    print("format: J=L,Q=? V=R,I=? ... : 'JLQ VRI ...'")
    print("".join(list(map(code_to_char, get_code()))))
    

def get_message():
    while True:
        message = input("Enter a message: ")
        if not len(list(filter(
            lambda x : not ord(x) in range(65, 91), message.upper()
        ))):
            return message.upper()
        else:
            print(f"'{message}' is not a valid message, try removing non-letters")


def valid_rnd_shift(char):
    while True:
        rn = rnd(65-ord(char), 90-ord(char))
        if not rn:   # repeat until not
            continue   
        if abs(rn) == 25:
            rn = (rn/abs(rn))*24
        return rn

num_of_valid_vals = lambda sft : 25 - abs(sft)

def create():
    message = get_message()
    for char in message:
        shift = valid_rnd_shift(char)
        novv = num_of_valid_vals(shift)
        if shift < 0:
            valid_vals = [chr(x) for x in range(65, ord(char))]
            remaining = novv - len(valid_vals)
            valid_vals += [chr(x) for x in range(ord(char)+1, ord(char)+remaining+1)]
        else:
            valid_vals = [chr(x) for x in range(65+shift, ord(char))]
            valid_vals = [chr(x) for x in range(ord(char)+1, 91)]

        hint_char =  rch(valid_vals)
        print(valid_vals, len(valid_vals), shift)




def main():
    while True:
        if (mode := input("('s':solve, 'c':create  -->)").lower()) == 's':   # repeat until
            solve()
            break
        elif mode == 'c':   # or
            create()
            break
        else:
            print(f"The input '{mode}' is not valid")


if __name__ == '__main__':
    main()
