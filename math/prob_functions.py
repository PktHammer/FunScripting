from math import comb


def greater_than_n_wins(wins_req: int, total_chances: int, win_rate: float) -> float:
    """Summation of number of equally likely chances multiplied by their probability of occurrence"""
    overall_prob = 0
    loss_rate = 1 - win_rate
    for num in range(wins_req, total_chances+1, 1):
        numerator = comb(total_chances, num)
        denominator = (win_rate ** num) * (loss_rate ** (total_chances - num))
        overall_prob += numerator * denominator
    return overall_prob


if __name__ == "__main__":
    res = greater_than_n_wins(wins_req=3, total_chances=4, win_rate=0.5)
    print(res)
