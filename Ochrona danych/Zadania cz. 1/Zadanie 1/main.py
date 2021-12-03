from collections import Counter

text_file = open("kryptogram.txt", "r")
text = text_file.read()
text_clean = text.replace(" ", "").replace("\n", "").replace("*", "")


def count_words(text_clean):
    word_counts = Counter(text_clean.split(" "))
    return word_counts


def count_symbols(text_clean):
    symbols_counts = Counter(text_clean)
    return symbols_counts


# pl_symbols_list = ("a", "e", "o", "i", "z", "n", "s", "r", "w", "c", "t", "l", "y", "k", "d", "p", "m", "u", "j", "b", "g", "h", "f", "q", "v", "x")
pl_symbols_str = ("aeoiznsrwctlykdpmujbghfqvx")

# Analiza znaków
print("---------------------------------------------------------------------------")
print("Analiza częstości występowania liter alfabetu łac. w zaszyfrowanym tekście:")
print(count_symbols(text_clean).most_common(35))

# Ilość unikalnych znaków w analizowanym tekście bez spacji, gwiazdki i \n
print("-----------------------------------------------")
print("Ilość unikalnych znaków w analizowanym tekście:")
print(len(count_symbols(text_clean)))
print("-------------------------------------------")
print("Laczna ilość znaków w analizowanym tekście:")
text_total_symbols = count_symbols(text_clean).total()
print(text_total_symbols)

print("--------------------------------------------------------")
print("Procentowy wskaźnik występowania danych liter w tekście:")
for key, value in sorted(count_symbols(text_clean).items(), key=lambda item: item[1], reverse=True):
    print(key, "->", round(value / text_total_symbols * 100, 3), " %")

sorted_items = sorted(count_symbols(text_clean).items(), key=lambda item: item[1], reverse=True)

print("-----------------------------------------------------------------------------------------------------------")
print("Zestawienie najczęściej występujących symboli w tekscie do najczęściej występujących liter w alfabecie łac.")
decrypted = [item[0] for item in sorted_items]
encrypted = [item[0] for item in pl_symbols_str]
for a, b in zip(decrypted, encrypted):
    print(a + " = " + b)

# Analiza spójników
print("------------------------------------------------")
print("Analiza częstości występowania spójników(top30):")
spojniki = count_words(text).most_common(30)
print(spojniki)
