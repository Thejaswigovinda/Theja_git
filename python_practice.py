def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Please enter a non-negative integer.")
            else:
                print(f"The factorial of {num} is {factorial(num)}.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
