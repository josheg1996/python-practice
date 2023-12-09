import sys

def reverse(word):
    a = ''
    for i in range(len(word)):
        a += word[len(word)-i-1]
    print(a)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: string_revesal.py <word>")
    else:
        # Get command-line arguments
        word = sys.argv[1]

        # Call reversal script
        reverse(word)