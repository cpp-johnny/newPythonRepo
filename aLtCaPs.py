def alt_caps(s: str) -> str:
    temp: list[str] = []
    for i, c in enumerate(s):
        if i % 2 == 0:
            temp.append(c.upper())
        else:
            temp.append(c.lower())
            
    return ''.join(temp)

if __name__ == '__main__':
    text: str = 'I will kill myself right now'
    print(alt_caps(text))   # output: I WiLl kIlL MySeLf rIgHt nOw
