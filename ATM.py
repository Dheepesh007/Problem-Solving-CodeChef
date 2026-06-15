# cook your dish here
import sys

def main():
    # Read the single line containing X and Y
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # X is the amount to withdraw (integer)
    X = int(input_data[0])
    # Y is the initial balance (float)
    Y = float(input_data[1])
    
    # Check if X is a multiple of 5 AND there is enough money including the 0.50 fee
    if X % 5 == 0 and Y >= (X + 0.50):
        Y -= (X + 0.50)
        
    # Print the remaining balance formatted to 2 decimal places
    print(f"{Y:.2f}")

if __name__ == '__main__':
    main()
