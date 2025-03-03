def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isupper():
            # Обработка заглавных букв
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        elif char.islower():
            # Обработка строчных букв
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            # Не-алфавитные символы остаются без изменений
            result.append(char)
    return ''.join(result)

def main():
    action = input("Выберите действие (1 - шифровать, 2 - дешифровать): ")
    text = input("Введите текст: ")
    shift = int(input("Введите сдвиг: "))
    
    if action == '2':
        shift = -shift  # Инвертируем сдвиг для дешифрования
    
    processed_text = caesar_cipher(text, shift)
    print("\nРезультат:", processed_text)

if __name__ == "__main__":
    main()
