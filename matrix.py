import random
from itertools import combinations
from collections import Counter
from more_itertools import windowed

SIZE = 9
HOMEROW = "crstnaeui"
# HOMEROW = ""

REPLACEMENTS = {
    "qu": "¹",
    "you": "²",
}

# REPLACEMENTS = {x * 2: f"{x}¹" for x in "aeiou"}
# REPLACEMENTS = {x * 2: f"{x}²" for x in "bcdfghjklmnpqrstvwxyz"}

LETTERS = (
    "abcdefghijklmnopqrstuvwxyz"
    ",.'"
    "?-\"!;:()"
    "`/@#"
    "¹²"
    # ";/[]-=1234567890"
)


def get_text(corpus = "monkeyracer.txt"):
    with open(corpus, "r") as f:
        text = f.read()

    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    
    return text

def get_pairs(corpus = "monkeyracer.txt"):
    text = get_text(corpus)

    res = Counter()
    for gram in windowed(text, 2):
        if not all(x in LETTERS for x in gram):
            continue
        
        res.update([gram[::-1]])
        res.update([gram]) 

    return res


def get_skips(corpus = "monkeyracer.txt"):
    text = get_text(corpus)

    res = Counter()
    for gram in windowed(text, 3):
        gram = (gram[0], gram[-1])
        if not all(x in LETTERS for x in gram):
            continue
        
        res.update([gram[::-1]])
        res.update([gram]) 

    return res

def get_monograms(corpus = "monkeyracer.txt"):
    text = get_text(corpus)
    res = Counter(text)
    # res = {k: v for k, v in res.items() if k in LETTERS}
    return res

def make_layout(letters=LETTERS, homerow="", shuffle=False):
    letters = list(letters)

    if shuffle:
        random.shuffle(letters)

    # set homerow
    string = "".join(letters)
    for char in homerow:
        string = string.replace(char, "")

    letters = list(homerow + string)

    # create layout
    buckets = [["●"] * SIZE for _ in range(SIZE + 1)]
    buckets[SIZE] = letters[:SIZE]

    for key, (a, b) in zip(letters[SIZE:], combinations(range(SIZE), 2)):
        buckets[a][b] = key
        buckets[b][a] = key

    return buckets

def show_layout(buckets):
    lines = []
    for home, bucket in zip(buckets[SIZE], buckets[:SIZE]):
        lines.append(home + " | " + " ".join(bucket))

    return "\n".join(lines)

def do_swap(a, b, buckets):
    buckets[a[0]][a[1]], buckets[b[0]][b[1]] = (
        buckets[b[0]][b[1]], buckets[a[0]][a[1]]
    )

    if a[0] < SIZE:
        buckets[a[1]][a[0]] = buckets[a[0]][a[1]]

    if b[0] < SIZE:
        buckets[b[1]][b[0]] = buckets[b[0]][b[1]]

def get_score(buckets, pairs):
    score = 0
    for i in range(SIZE):
        bucket = [buckets[SIZE][i]] + buckets[i][:i] + buckets[i][i + 1:]
        
        for combo in combinations(bucket, 2):
            score += pairs.get(combo, 0)

    return score

def get_fingers(buckets, monograms):
    res = [0] * SIZE
    for i in range(SIZE):
        bucket = [buckets[SIZE][i]] + buckets[i][:i] + buckets[i][i + 1:]
        
        for char in bucket:
            res[i] += monograms.get(char, 0)

    return res

def get_top(buckets, pairs):
    res = {}
    for i in range(SIZE):
        bucket = [buckets[SIZE][i]] + buckets[i][:i] + buckets[i][i + 1:]
        
        for combo in combinations(bucket, 2):
            res["".join(combo)] = pairs.get(combo, 0)

    res = dict(sorted(res.items(), key=lambda x: x[1], reverse=True))
    return res

def main():
    combos = list(combinations(range(SIZE), 2))
    if not HOMEROW:
        combos += [(SIZE, x) for x in range(SIZE)]
    
    swaps = list(combinations(combos, 2))

    buckets = make_layout(homerow=HOMEROW, shuffle=True)
    pairs = get_pairs()

    best = get_score(buckets, pairs)
    optimum = best

    while True:
        random.shuffle(swaps)

        for a, b in swaps:
            do_swap(a, b, buckets)
            score = get_score(buckets, pairs)

            if score < best:
                best = score
                break

            do_swap(a, b, buckets)
        else:
            if best < optimum:
                optimum = best

                print(f"score = {optimum / sum(pairs.values()):.3%}")
                print(show_layout(buckets))

            buckets = make_layout(homerow=HOMEROW, shuffle=True)
            best = get_score(buckets, pairs)

if __name__ == "__main__":
    main()