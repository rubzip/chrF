from collections import Counter

def get_all_ngrams(text: list, n: int):
    m = len(text) + 1 - n
    n_grams = [
        tuple(text[i:n+i]) for i in range(m)
    ]
    return n_grams


def split_by_char(text: str)->list:
    return tuple(text.replace(' ', '_'))


def chrP(hypothesis: str, reference: str, n: int)->float:
    hyp_n = Counter(get_all_ngrams(hypothesis.split(), n))
    ref_n = Counter(get_all_ngrams(reference.split(), n))

    return sum(min(hyp_n[key], ref_n[key]) for key in hyp_n.keys()) / len(hyp_n)

def chrR(hypothesis: str, reference: str, n: int)->float:
    hyp_n = Counter(get_all_ngrams(split_by_char(hypothesis), n))
    ref_n = Counter(get_all_ngrams(split_by_char(reference), n))

    return sum(min(hyp_n[key], ref_n[key]) for key in hyp_n.keys()) / len(hyp_n)

def chrF(hypothesis: str, reference: str, n: int, beta_: float)->float:
    p = chrP(hypothesis, reference, n)
    r = chrR(hypothesis, reference, n)

    return (1 + beta_)*(p * r) / (beta_*p + r)

print(
    get_all_ngrams(
        "hola me llamo ruben y soy de granada".split(), 4)
)

print(
    chrP(
        "hola me llamo ruben y soy de granada", 
        "hola me llamo ruben y soy de malaga", 4)
)

print(
    chrR(
        "hola me llamo ruben y soy de granada", 
        "hola me llamo ruben y soy de malaga", 4)
)

print(
    chrF(
        "hola me llamo ruben y soy de granada", 
        "hola me llamo ruben y soy de malaga", 4, 1)
)

print(
    split_by_char("This is an example.")
)