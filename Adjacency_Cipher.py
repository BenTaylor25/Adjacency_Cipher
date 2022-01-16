'''
Elevator question

JLQ VRI FBZ WMO ADK GAZ AUE CIN GLR DBQ EPI XUK ZQX CHP OXJ WPH SZG SLK WLP OSE MAS LQC DBV ZUM JQN RZF VLN KZC QBT WOL ZXG RUF QAW OUB LJV EMQ BLJ HAO TMY ZGX TWB
'''


get_key = lambda n1, n2 : n2 - n1

def get_code():
    while True:
        code_string = input("code: ")
        chars_valid = not len(list(filter( 
            lambda x : x!=' ' and not ord(x) in range(65, 91), code_string.upper()
        )))
        code_list = code_string.upper().split()
        lens = list(map(lambda x : len(x), code_list))

        if chars_valid and len(lens) and max(lens)==min(lens)==3:
            return code_list
        else:
            print(f"The input '{code_string}' is not valid")


def code_to_char(code):
    key = get_key(ord(code[0]), ord(code[1]))
    return chr(ord(code[2])+key)

def solve():
    print("format: J=L,Q=? V=R,I=? ... : 'JLQ VRI ...'")
    print("".join(list(map(code_to_char, get_code()))))

    

def create():
    print("[create]")


def main():
    while True:
        if (mode := input("('s':solve, 'c':create  -->)").lower()) == 's':
            solve()
            break
        elif mode == 'c':
            create()
            break
        else:
            print(f"The input '{mode}' is not valid")


if __name__ == '__main__':
    main()
