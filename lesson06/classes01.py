dict_eng_to_rus = {"apple": "яблоко", "house": "дом"}

dict_rus_to_eng = {
    value: key
    for key, value in dict_eng_to_rus.items()
}

def from_eng_to_rus(eng):
    rus = dict_eng_to_rus[eng]
    return rus

from_eng_to_rus("apple")

def from_rus_to_eng(rus):
    eng = dict_eng_to_rus[rus]
    return eng

from_rus_to_eng("яблоко")