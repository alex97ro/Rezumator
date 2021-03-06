import string

import nltk

nltk.download('punkt')


# Functie care deschide fisierul si adauga toate prepozitiile / conjuctiile intr-o lista

def adauga_cuvinte(path):
    with open(path, "r", encoding='utf8') as f:
        cuvinte = f.read()
        lista_cuvinte = cuvinte.split("\n")
    return lista_cuvinte[:-1]


# Functie care returneaza un dictionar avand ca cheie cuvintele si ca valoare numarul.
# De aparitii in text a acestora

def word_counter(text):
    dictionar_couter = {}
    words = [word.strip(string.punctuation).lower() for word in text.split()]
    for word in words:
        if word not in dictionar_couter:
            dictionar_couter[word] = 1
        else:
            dictionar_couter[word] = dictionar_couter[word] + 1

    if '' in dictionar_couter:
        del dictionar_couter['']

    return dictionar_couter


# Functie care imparte in propozitii un text.
def text_sentences(text):
    sentences = nltk.tokenize.sent_tokenize(text)
    return sentences


# Functie eliminare dialog
def process_text(text):
    split_text = text.split("\n")
    new_text = ""
    for counter in range(0, len(split_text)):
        if split_text[counter][-2] == ':' and split_text[counter + 1][0] == '-':
            pass
        elif split_text[counter][0] == '-':
            pass
        else:
            new_text = new_text + split_text[counter] + "\n"

    return new_text


# Functie care imparte un text in paragrafe.
def paragraphs_text(text):
    new_text = text.split("\n")
    if new_text[-1] == '':
        return new_text[:-1]
    else:
        return new_text


# Functie pentru distributia frecventei cuvintelor.
# Functia elimina din dictionarul frecventei cuvintele de legatura, prepozitii, conjunctii
def word_freq_distribution(dictionar_counter):
    freq_dictionar = {}
    cuv_neimportante = adauga_cuvinte(r"C:\Users\FuNNNk\Desktop\Fac\Sem5\AI\RezumatorOk\Cuv-neimportante.txt")
    max_freq = max(dictionar_counter.values())
    for word in dictionar_counter.keys():
        if len(word) == 2 or len(word) == 1 or word in cuv_neimportante:
            pass
        else:
            freq_dictionar[word] = (dictionar_counter[word] / max_freq)
    list_freq = sorted(freq_dictionar.items(), key=lambda x: x[1], reverse=True)
    return list_freq


# Functie prin care determina cele mai importante cuvinte din text
def extrage_cuvinte_imp(list_freq):
    cuvinte_importante = []
    for counter in range(0, len(list_freq)):
        if counter <= len(list_freq) / 10:  # Luam primele 10% cuvintele aparute cel mai frecvent in list_freq
            cuvinte_importante.append(list_freq[counter][0])
    return cuvinte_importante


####################################
# Transformare numere litere in cifre
####################################
def litere_in_cifre(textnum, numwords={}):
    textnum = procesare_numere(textnum)
    if not numwords:
        units = [
            "zero", "unu", "doi", "trei", "patru", "cinci", "sase", "sapte", "opt",
            "noua", "zece", "unsprezece", "doisprezece", "treisprezece", "paisprezece", "cincisprezece",
            "saisprezece", "saptesprezece", "optisprezece", "nouasprezece",
        ]

        tens = ["", "", "douazeci", "treizeci", "patruzeci", "cincizeci", "saizeci", "saptezeci", "optzeci", "nouazeci"]

        scales = ["suta", "mie", "milion"]

        numwords["si"] = (1, 0)
        for idx, word in enumerate(units):    numwords[word] = (1, idx)
        for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Numar incorect: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current


def procesare_numere(text):
    numere = text.split(" ")
    numar_nou = ''
    for counter in range(0, len(numere)):
        if numere[counter] == 'o' or numere[counter] == 'un':
            numar_nou = numar_nou + 'unu' + ' '
        elif numere[counter] == 'doua' and numere[counter + 1] != '':
            numar_nou = numar_nou + 'doi' + ' '
        elif numere[counter] == 'sute':
            numar_nou = numar_nou + 'suta' + ' '
        elif numere[counter] == 'mii':
            numar_nou = numar_nou + 'mie' + ' '
        elif numere[counter] == 'milioane':
            numar_nou = numar_nou + 'milion' + ' '
        elif numere[counter] == 'de':
            pass
        else:
            numar_nou = numar_nou + numere[counter] + ' '
    return numar_nou


# def remove_enum(text):
#     text = re.sub("(\w+)( \w+)*, (\w+)( \w+)*(, (\w+)( \w+)*)*", "", text)
#     return text
#
#
# def remove_rep(text):
#     new_text = ""
#     sentences = nltk.tokenize.sent_tokenize(text)
#     print(sentences)
#     for sentence in sentences:
#         words = re.findall(r'[a-zA-Z-*]+', sentence)
#         words_dict = list(dict.fromkeys(words))
#         print(words_dict)
#         for word in words_dict:
#             print(word)
#             print(words.count(word))
#             if words.count(word) > 1:
#                 sentence = sentence.replace(word, "", words.count(word) - 1)
#                 print(sentence)
#         new_text += sentence
#         new_text = re.sub(r'si', '', new_text)
#         new_text = re.sub(r' +', ' ', new_text)
#
#     return new_text
#
# print(remove_rep("el s-a uitat si s-a uitat si s-a uitat"))
# print(remove_rep("el manca si zi si noapte si zi si noapte"))

