def rabin_karp(haystack: str, needle: str, base: int = 256, divisor: int = 101):
    if not needle or not haystack:
        return []

    pattern_mask = 0  # числове представлення needle
    first_letter_power = pow(base, len(needle) - 1, divisor)
    haystack_substring_mask = 0

    # перетворюємо шаблон в число
    for char in needle:
        pattern_mask = (base * pattern_mask + ord(char)) % divisor

    index = []

    # перетворюємо першу підстроку в число
    for i in range(len(needle)):
        haystack_substring_mask = (base * haystack_substring_mask + ord(haystack[i])) % divisor

    for i in range(len(haystack) - len(needle) + 1):
        if pattern_mask == haystack_substring_mask and haystack[i:i + len(needle)] == needle:
            index.append(i)

        if i < len(haystack) - len(needle):
            haystack_substring_mask = (base * (haystack_substring_mask - ord(haystack[i]) * first_letter_power) +
                                       ord(haystack[i + len(needle)])) % divisor

    return index

