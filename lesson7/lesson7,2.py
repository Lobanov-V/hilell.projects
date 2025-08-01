def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'

    return text



print(correct_sentence("greetings, friends"))
print(correct_sentence("hello"))
print(correct_sentence("Greetings, Friends"))
print(correct_sentence("greetings, friends."))
print(correct_sentence("ОК"))

