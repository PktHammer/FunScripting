import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math


def find_ex(x_l: list, px_l: list, show_work=False) -> float:
    """
    :param x_l: list of x
    :param px_l: list of px
    :param show_work: print formatted work
    :return: E(X)
    """
    ex = 0
    for c, x_val in enumerate(x_l):
        ex += x_val * px_l[c]
        if(show_work):
            print("| " + str(x_val) + " * " + str(px_l[c]) + " = " + str(x_val * px_l[c]))
    return ex


def find_ex2(x_l: list, px_l: list, show_work=False) -> float:
    """
    :param x_l: list of x
    :param px_l: list of px
    :param show_work: print formatted work
    :return: E(X)^2
    """
    ex2 = 0
    for c, x_val in enumerate(x_l):
        ex2 += (x_val ** 2) * px_l[c]
        if show_work:
            print("| " + str(x_val ** 2) + " * " + str(px_l[c]) + " = " + str((x_val ** 2) * px_l[c]))
    return ex2


def find_vx(x_l: list, px_l: list, show_work=False) -> float:
    """
    :param x_l: list of x
    :param px_l: list of px
    :param show_work: print formatted work
    :return: V(X)
    """
    ex = find_ex(x_l, px_l)
    vx = 0
    for c, x_val in enumerate(x_l):
        vx += ((x_val - ex) ** 2) * px_l[c]
        if show_work:
            print("| " + str((x_val - ex) ** 2) + " * " + str(px_l[c]) + " = " + str(((x_val - ex) ** 2) * px_l[c]))
    return vx


def nCr(n: float, r: float) -> float:
    """
    :param n: number total
    :param r: number chosen
    :return: nCr : the number of combinations you can choose r in n
    """
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))


def binomial_dist_chance(n: float, p: float, x: float) -> float:
    """
    :param n: sample size
    :param p: probability of success
    :param x: number of successes
    :return: probability of exactly x successes given dist
    """
    return nCr(n, x) * pow(p, x) * pow(1-p, n-x)


def binomial_ex(n: float, p: float) -> float:
    """
    :param n: sample size
    :param p: probability of success
    :return: E(X) : Expected value of p
    """
    return n*p


def binomial_vx(n: float, p: float) -> float:
    """
    :param n: sample size
    :param p: probability of success
    :return: V(X) : Expected variance
    """
    return n*p*(1-p)


def binomial_sdev(n: float, p: float) -> float:
    """
    :param p: probability of success
    :param n: sample size
    :return: Standard Deviation
    """
    return pow(binomial_vx(n, p), 0.5)


def binomial_all_stats(n: float, p: float):
    """
    :param p: probability of success
    :param n: sample size
    """
    print("E(X) = np = " + str(n) + " * " + str(p) + " = " + str(binomial_ex(n, p)))
    print("V(X) = np(1-p) = " + str(n) + " * " + str(p) + " ( 1 - " + str(p) + ") = " + str(binomial_vx(n, p)))
    print("sdev(x) = sqrt(V(X)) = " + str(binomial_sdev(n, p)))


if __name__ == "__main__":
    print("Hello world!")
    x = [1,2,3,4,5]
    px = [0.23, 0.15, 0.18, 0.34, 0.12]
    print(find_ex(x, px, show_work=True))
    print(find_ex2(x, px, show_work=True))
    print(find_vx(x, px, show_work=True))

""" # Example code
    x = [13.5, 15.9, 19.1]
    px = [0.2, 0.5, 0.3]
    print(find_ex(x, px, show_work=True))
    print(find_ex2(x, px, show_work=True))
    print(find_vx(x, px, show_work=True))

    mod_x = []
    for k in x:
        mod_x.append((25*k)-8.5)
    print(mod_x)
    print(find_vx(mod_x, px, show_work=True))

    x2 = [0, 500, 4500, 9500]
    px2 = [0.8,0.2,0.08,0.02]
    print(find_ex(x2, px2, show_work=True))

    x3 = [25, 0]
    px3 = [.3, .7]
    print(find_vx(x3, px3, show_work=True))

    print(str(binomial_ex(5, 0.4)))
    binomial_all_stats(5.0, 0.4)"""
