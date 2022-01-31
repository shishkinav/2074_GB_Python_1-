def get_jokes(count: int, flag: int) -> list:

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    from random import randint

    joke_list = []

    if flag == 0:
        for i in range(count):
            noun = nouns[randint(0, len(nouns) - 1)]
            adverb = adverbs[randint(0, len(adverbs) - 1)]
            adjective = adjectives[randint(0, len(adjectives) - 1)]
            joke_list.append(' '.join([noun, adverb, adjective]))
            i += 1
    else:
        # для flag == 1 используется метод .pop()
        for i in range(0, len(nouns), 1):
            noun = nouns.pop(randint(0, len(nouns) - 1))
            adverb = adverbs.pop(randint(0, len(adverbs) - 1))
            adjective = adjectives.pop(randint(0, len(adjectives) - 1))
            joke_list.append(' '.join([noun, adverb, adjective]))
            i += 1

    return joke_list


print(get_jokes(6, 1))