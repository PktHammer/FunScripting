entry = "ab ac ad be bf bg ch ci dj dk el em fn fo gp gq lr ls rt ru"
entry = "sa mp le" # Map({('s', 'a'), ('m', 'p'), ('l', 'e')}, directed=True)

def sane_entry(pair: str) -> str:
    if len(pair) != 2:
        print(f"Error, {pair} is not a pair")
    else:
        return f"('{pair[0]}', '{pair[1]}')"


if __name__ == '__main__':
    answer = ""
    answer += "Map({"
    for item in entry.split(' '):
        answer += sane_entry(item)
        answer += ", "
    answer = answer[:-2]
    answer += "}, directed=True)"
    print(answer)
