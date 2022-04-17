text = 'Тест тест привіт "??? повтор, повтор. Повтор повторити @123 repeat 1 не 123 1"№!№'
def wordscount(text):
    dict = {}
    text = text.lower()
    symbol_line = '!@#$%^&*()_+-=/\|.,`1234567890<>"«»—№;:?'
    #Перевіряємо кожний символ тексту і видаляємо числа, пунктуацію та інші символи
    for symbol in text:
        if symbol in symbol_line:
            text = text.replace(symbol, '')
    #Розбиваємо текст на список слів
    words_list = text.split()
    #Перевіряємо кожне слово списку на присутність у словнику, якщо так значення збільшується на 1, якщо ні, добавляємо новий ключ(слово) і значення для нього
    for word in words_list:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    return dict

print(wordscount(text))