# Q5

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def remove_punctuation(ss):
    s_sans_punctuation = ""
    for letter in ss:
        if letter not in punctuation:
            s_sans_punctuation += letter
    return s_sans_punctuation


def specific_word_count(string, ch):
    ss = string
    count_wds = 0
    count_chs = 0
    count_lts = 0
    words = remove_punctuation(ss).split()
    for c in words:
        if c != "+":
            count_wds += 1
    for c in string:
        if c == ch:
            count_chs += 1
    for c in string:
        if c != "+":
            count_lts += 1
    print("Your text contains", count_wds, "words, of which", count_chs, "(", (float(int((count_chs/count_lts)*100))), "%) contain an/a", "'", ch, "'", ".")


print(specific_word_count("Imagine if I was given one moment, found the safe and looked inside There was room for lots of moments; in fact, hundreds if I tried. I'm building my own little library, embedded in my heart, for all the moments spent with you before you had to part. I can open it up whenever I like, pick a moment and watch it through, My little library acts as a promise I'll never ever forget you.", "e"))



