# This problem was asked by Google.

# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a
# Monte Carlo method.

# Hint: The basic equation of a circle is x^2 + y^2 = r^2.

import random
import math

def monte_carlo_pi(n):
    circle_count = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if math.sqrt((x-0.5)**2+(y - 0.5)**2) <= 0.5:
            circle_count += 1        
    return round(4*(circle_count/n),3)


def main():
    print("17/12/2020, this problem was asked by Google.")
    n = int(input("N = "))
    rep = int(input("Repetition = "))
    temp = 0
    for i in range(rep):
        result = monte_carlo_pi(n)
        temp += result
        print("Trial #{}: Monte Carlo's pi ({} points) = {}".format(i+1,n,result))

    print("Overall = {}".format(temp/rep))




if __name__ == "__main__":
    main()
