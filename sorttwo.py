#!/bin/usr/env python3



def main():
    n, m = input().split()

    if n <= m:
        print("{0} {1}".format(n,m))
    else:
        print("{0} {1}".format(m,n))


if __name__ == "__main__":
    main()