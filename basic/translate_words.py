def translate(b_dict, words):
    result = []

    for word in words:
        result.append(b_dict.get(word, word))  

    return result

dct = {"merry":"god", "christmas":"jul", "aand":"och",
       "happy":"gott", "new":"nytt", "year":"ar"}
wish = ["merry","christmas","aand","happy","new","year"]
print(translate(dct, wish))
