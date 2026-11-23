
n = int(input("Enter the number of terms in the Fibonacci series: "))


def fibonaci_series(n):
    a = 0
    b = 1
    series = []
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series


print(fibonaci_series(n))
