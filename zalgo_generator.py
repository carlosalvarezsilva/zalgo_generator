import random

combining_half_marks = [chr(i) for i in range(0xFE20, 0xFE2F + 1)]
combining_basic = [chr(i) for i in range(0x0300, 0x036F + 1)]
combining_extended = [chr(i) for i in range(0x1AB0, 0x1ABF + 1)]
combining_supplement = [chr(i) for i in range(0x1DC0, 0x1DFF + 1) if i not in [0x1DFA]]
combining_symbols = [
    chr(i) for i in range(0x20D0, 0x20F0 + 1)
    if i not in range(0x20F1, 0x2100)  # remove U+20F1 to U+20FF
]

superscript_digits = [chr(i) for i in range(0x2070, 0x2079 + 1)]
subscript_digits = [chr(i) for i in range(0x2080, 0x2089 + 1)]
superscripts_and_subscripts = superscript_digits + subscript_digits

zalgo_normal = (
    combining_half_marks +
    combining_basic +
    combining_supplement
)

zalgo_full = (
    combining_half_marks +
    combining_basic +
    combining_extended +
    combining_supplement +
    combining_symbols
)

def zalgo_char(c, intensity, isCorrupted=False):
    if not c.isalpha():
        return c
    all_marks = zalgo_full if isCorrupted else zalgo_normal
    intensity = min(max(0, intensity), 20)
    zalgofied_char = c + ''.join(random.choices(all_marks, k=intensity))
    if random.random() < 0.15:
        zalgofied_char += random.choice(superscripts_and_subscripts)
    return zalgofied_char

def zalgo_text(text, intensity, isCorrupted=False):
    return ''.join(zalgo_char(c, intensity, isCorrupted) for c in text)

def gradual_zalgo(text, start_intensity=0, end_intensity=10, isCorrupted=False):
    out = []
    steps = (len(text) - 1) if (len(text) > 1) else 1
    for i, c in enumerate(text):
        level = start_intensity + int((end_intensity - start_intensity) * (i / steps))
        out.append(zalgo_char(c, level, isCorrupted))
    return ''.join(out)

# User interface
def main():
    while True:
        print("Zalgo Text Generator")
        print("====================")
        print("1. Regular Zalgo")
        print("2. Gradual Zalgo")
        print("3. Zalgo (Powerfull Version)")
        print("4. Gradual Zalgo (Powerfull Version)")
        print("Other to Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            text = input("Enter text to Zalgo-fy: ")
            if not text.strip():
                print("No text provided.")
                continue
            try:
                intensity = int(input("Enter intensity (recommended 1-20): "))
            except ValueError:
                print("Invalid number. Try again.")
                continue
            print("\nZalgo Text:")
            print(zalgo_text(text, intensity))
        elif choice == '2':
            text = input("Enter text to gradually Zalgo-fy: ")
            if not text.strip():
                print("No text provided.")
                continue
            try:
                start_int = int(input("Enter intensity from first letter (0-20): "))
                end_int = int(input("Enter intensity from last letter (0-20): "))
            except ValueError:
                print("Invalid number. Try again.")
                continue
            print("\nGradual Zalgo Text:")
            print(gradual_zalgo(text, start_int, end_int))
        elif choice == '3':
            text = input("Enter text to Zalgo-fy on steroids: ")
            if not text.strip():
                print("No text provided.")
                continue
            try:
                intensity = int(input("Enter intensity (1-20): "))
            except ValueError:
                print("Invalid number. Try again.")
                continue
            print("\nBig Zalgo Text:")
            print(zalgo_text(text, intensity, True))

        elif choice == '4':
            text = input("Enter text to gradually Zalgo-fy on steroids: ")
            if not text.strip():
                print("No text provided.")
                continue
            try:
                start_int = int(input("Enter intensity from first letter (0-20): "))
                end_int = int(input("Enter intensity from last letter (0-20): "))
            except ValueError:
                print("Invalid number. Try again.")
                continue
            print("\nBig Gradual Zalgo Text:")
            print(gradual_zalgo(text, start_int, end_int, True))

        else:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
