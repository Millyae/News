from django import template

register = template.Library()

@register.filter
def censor(value):
    unwanted_words = ['удар', 'убийство', 'наркотики', 'насилие', 'смерть', 'жертвы']  # список нежелательных слов
    censored_value = value
    for word in unwanted_words:
        censored_value = censored_value.replace(word, '*' * len(word))  # заменяем слово на звездочки
    return censored_value