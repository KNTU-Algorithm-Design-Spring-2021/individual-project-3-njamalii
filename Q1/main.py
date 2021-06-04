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
    for index, c in enumerate(string):
        prefix += c
        if prefix in words:
            decoder(string[index+1:], result=f'{result}{prefix} ')
    if prefix in words:
        result += prefix
        print(result)


if __name__ == '__main__':
     decoder("CALLSECURITYATMIAMIAIRPORTBECAUSEITHINKTHEREBOMBINAIRPORT")

(decoder(input()))
