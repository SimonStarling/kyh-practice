'''15.1 Implementera "wordcount" som jag och Christoffer byggde #
15.2 Ta in en godtycklig text (testa att copy-paste från lorumipsum.com) och skriv ut hur många vokaler som finns i strängen. Tips: "a" in "abcd" är True!
15.3 Göteborgsvarvet, vilken placering kom XYZ på? Implementera resten av detta program:
    runners_in_order = “Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus”.split()
    vem = input(“Ange löpare du söker placering för'''


# Wordcounter
def main():
    vowels = "aeiouy"
    vowels_count = 0

    def wordcount(txt):
        return len(txt.split())

    text = input("Skriv in text: ")
    count = wordcount(text)

    for c in text:
        if c in vowels:
            vowels_count += 1

    print(f'Antal ord som angivits: {count} \n Antal Vokaler{vowels_count}')


main()
