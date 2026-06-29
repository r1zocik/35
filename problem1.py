def count_vowels_and_consonants(text: str) -> dict:
    unli = 0
    undosh = 0
    for u in text.lower():
        if u in "a, e, i, o, u": 
            unli += 1
        elif u.isalpha():     
            undosh += 1

    return {"unli": unli, "undosh": undosh}



print(count_vowels_and_consonants("Salom Dunyo!"))
# Kutilgan natija: {"unli": 4, "undosh": 5}