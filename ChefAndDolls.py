import sys

def main():
    # Read all input at once for speed
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    # First line is T, the number of test cases
    t = int(input_data[ptr])
    ptr += 1
    
    for _ in range(t):
        # First line of each test case is N, the number of dolls
        n = int(input_data[ptr])
        ptr += 1
        
        missing_doll = 0
        # XOR all doll types in the current test case
        for _ in range(n):
            doll_type = int(input_data[ptr])
            missing_doll ^= doll_type
            ptr += 1
            
        # The result is the doll type that doesn't have a pair
        print(missing_doll)

if __name__ == '__main__':
    main()
