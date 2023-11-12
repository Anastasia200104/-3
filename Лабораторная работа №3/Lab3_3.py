main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
def count_letters(text):
    letter_low = text.lower()
    letter_number = {}
    for letter in letter_low:
        if letter.isalpha():
            if letter in letter_number:
                letter_number[letter] = letter_number[letter] + 1
            else:
                letter_number[letter] = 1
    return letter_number
def calculate_frequency(letter_number):
    value_of_frequency = {}
    sum_letters = sum(letter_number.values())
    for letter, count in letter_number.items():
        frequency = count / sum_letters
        value_of_frequency[letter] = round(frequency, 2)
    return value_of_frequency

dict_ = count_letters(main_str)
dict_frequency = calculate_frequency(dict_)

for letter, frequency in dict_frequency.items():
    print(f"{letter}: {frequency:.2f}")