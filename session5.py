import math

def main():
    num_points = 1000
    start = 0
    end = 2 * math.pi
    step = (end - start) / (num_points - 1)

    print("x\t\tsin(x)")
    print("-" * 24)

    for i in range(num_points):
        x = start + i * step
        y = math.sin(x)
        print(f"{x:.6f}\t{y:.6f}")


main()
