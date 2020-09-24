# %matplotlib inline # LaTeX Printer friendly!
# %matplotlib notebook # Fancy version that doesn't work if you print it
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def find_median(mlist: list, is_sorted=True) -> float:
    """
    Finds median

    :param mlist: list to be entered
    :param is_sorted: will presort if set to false
    :return: float median
    """
    # If unsorted, sort
    if(is_sorted==False):
        return find_median(sorted(mlist))
    # Else continue
    llength = len(mlist)
    if llength == 0:
        return False
    if llength == 1:
        return mlist[0]
    if llength % 2:
        return mlist[int(llength/2)]
    else:
        return (mlist[int(llength/2) - 1] + mlist[int(llength/2)]) / 2


def find_mean(mlist: list)-> float:
    """
    Finds mean

    :param mlist: list to be entered
    :return: float mean
    """
    mean = 0
    for num in mlist:
        mean += num
    return(mean / len(mlist))


def find_range(mlist: list, is_sorted=True) -> float:
    """
    Finds range

    :param mlist: list to be entered
    :param is_sorted: will presort if set to false
    :return: float range
    """
    # If not sorted, sort
    if(is_sorted==False):
        return find_range(sorted(mlist))
    # Else continue
    # Max - min unless there's only 1 item which it's 0
    llen = len(mlist)
    if (llen == 1):
        return 0
    return(mlist[len(mlist) - 1] - mlist[0])


def find_variance_defi_method(mlist: list, is_sorted=True) -> float:
    """
    Finds variance with definition method
    :param mlist: list to be entered
    :param is_sorted: will presort if set to false
    :return: float variance
    """
    # If not sorted, sort
    if(is_sorted==False):
        return find_variance_defi_method(sorted(mlist))
    # Else calculate mean
    mean = find_mean(mlist)
    # Calculate summation
    summation = 0
    for num in mlist:
        # For each number, calculate the distance from the mean and square it, add to sum
        summation += (num - mean) ** 2
    # Multiply summation by 1/(n-1) & return
    return summation / (len(mlist) - 1)


def find_variance_shortcut_method(mlist: list, is_sorted=True) -> float:
    """
    Finds variance with shortcut method
    :param mlist: list to be entered
    :param is_sorted: will presort if set to false
    :return: float variance
    """
    # If not sorted, sort
    if(is_sorted==False):
        return find_variance_shortcut_method(sorted(mlist))
    # Else calculate mean
    mean = find_mean(mlist)
    # Calculate shortcut summation
    summation = 0
    for num in mlist:
        # For each number, return the square
        summation += num ** 2
    # Calculate the n * mean^2
    n = len(mlist)
    difference = n * (mean ** 2)
    # Divide summation less difference by (n-1) & Return
    return (summation - difference) / (n-1)


def split_arr_for_quartiles(mlist: list):
    """Parses the array into two"""
    mlen = len(mlist)
    if mlen == 1: # If 1
        return
    if mlen % 2: # If odd, remove the center
        t_mlist = mlist[:]
        del t_mlist[int(mlen/2)]
        mlen -= 1
        # Return the splice
        return t_mlist[0:int(mlen/2)], t_mlist[int(mlen/2):mlen]
    else: # Else if even, return splice
        return mlist[0:int(mlen/2)], mlist[int(mlen/2):mlen]


def find_outliers(mlist: list, is_sorted=True) -> list:
    """
    Returns outliers given list

    :param mlist: list to be entered
    :param is_sorted: will presort if set to false
    :return: list of outliers
    """
    if is_sorted == False:
        find_outliers(sorted(mlist))
    A1, A2 = split_arr_for_quartiles(mlist)
    Q1 = find_median(A1)
    Q3 = find_median(A2)
    IQR = Q3-Q1
    LF = Q1 - 1.5 * IQR
    UF = Q3 + 1.5 * IQR
    outliers = []
    for item in mlist:
        if item < LF or item > UF:
            outliers.append(item)
    return outliers


def find_outliers_given_q1_q3(mlist: list, Q1: float, Q3: float):
    """
    Returns outliers given list

    :param mlist: list to be entered
    :param is_sorted: will presort if set to false
    :return: list of outliers
    """
    IQR = Q3-Q1
    LF = Q1 - 1.5 * IQR
    UF = Q3 + 1.5 * IQR
    outliers = []
    for item in mlist:
        if item < LF or item > UF:
            outliers.append(item)
    return outliers
