def verifie_age(age: int) -> bool:
    age_list = map(int, str(age))
    if (sum(age_list % 2 == 0)):
        return True
    age_set = set(age_list)
    if(len(age_set) == 1):
        return True
    return False