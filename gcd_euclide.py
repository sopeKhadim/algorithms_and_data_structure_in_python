def gcd_euclid(a, b):
    if b == 0:
        return a
    else:
        return gcd_euclid(b, a % b)


if __name__ == "__main__":
    print(gcd_euclid(12, 3))
