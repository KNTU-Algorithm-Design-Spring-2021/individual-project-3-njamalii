words = set()
with open("words.txt") as file:
    for word in file:
        word = word.strip()
        if word:
            words.add(word)
print(f"{len(words)} words detected")


def decoder(string, result=''):
    string = string.lower()
    prefix = ''
    all_results = []
    for index, c in enumerate(string):
        prefix += c
        if prefix in words:
            all_results += decoder(string[index + 1:], result=f'{result}{prefix} ')
    if prefix in words:
        result += prefix
        all_results.append(result)
    return all_results


if __name__ == '__main__':
    decoded_sents = decoder("CALLSECURITYATMIAMIAIRPORTBECAUSEITHINKABOMBISABOUTTOGOOFF")
    print("\n".join(f"{index+1}) {sent}" for index,sent in enumerate(decoded_sents)))


