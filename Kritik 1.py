def question4():
    #get input
    x = float(input("Enter a value for x: "))

    #check if x is within [0, 1]
    if x < 0 or x > 1:
        print("Error!")
        return
    #initialize variables
    approximation = 0
    previous_approximation = 0
    error_bound = float('inf')
    n = 0

    #continue adding terms until the error is <= 0.0001
    while error_bound > 0.0001:
        term = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
        approximation += term
        error_bound = abs(approximation - previous_approximation)
        previous_approximation = approximation
        n += 1

    #output tuple
    print(f"({approximation}, {n}, {error_bound})")
    print("(a, n, error_bound)")

question4()
