from . import modul_1  # Modulul (Robert Darabana - Grigorovschi Teodor)
import string


# Afisarea textului rezumat in functie de procentul dat de utilizator
def afisare_text_procent(lista_scor_prop, procent):
    lista_scor_prop = lista_scor_prop[0:round(len(lista_scor_prop) * procent / 100)]
    return lista_scor_prop


#####################################################################
############################EURISTICI################################
#####################################################################

def calculeaza_scor(propozitie, text):
    list_freq = modul_1.word_freq_distribution(modul_1.word_counter(text))
    cuvinte_importante = modul_1.extrage_cuvinte_imp(list_freq)  # 10% cele mai importante cuvinte din text
    words = [word.strip(string.punctuation).lower() for word in propozitie.split()]
    begin, end, total_words, cuv_imp = 0, 0, 0, 0
    for word in words:
        if word in cuvinte_importante:
            cuv_imp = cuv_imp + 1
            if cuv_imp == 1:
                begin = total_words
            end = total_words
        total_words = total_words + 1

    if end - begin + 1 == 0:
        return 0.0

    return float(cuv_imp ** 2) / float(end - begin + 1)


def scorul_propozitiilor(text):
    text = modul_1.process_text(text)  # Functie prin care eliminam dialogul inainte sa calculam scorurile
    dictionar_scor = {}
    propozitii_text = modul_1.text_sentences(text)
    for prop in propozitii_text:
        if prop not in dictionar_scor:
            dictionar_scor[prop] = calculeaza_scor(prop, text)
        else:
            pass

    lista_scor_prop = sorted(dictionar_scor.items(), key=lambda x: x[1], reverse=True)
    return lista_scor_prop


def reconstruire_text(text, procent):
    text_reconstruit = ""
    lista_scor_prop = scorul_propozitiilor(text)
    prop_alese = afisare_text_procent(lista_scor_prop,
                                      int(procent))  # Prop-alese = lista de tuple de forma ( propozitie , procent)
    lista_prop_alese = []  # Doar propozitiile din tupla de forma (propozitie, procent)
    for prop in prop_alese:
        s = prop[0].replace('\r', "").replace('\n', "")
        lista_prop_alese.append(s)
    text = modul_1.process_text(text)
    paragrafe_text = modul_1.paragraphs_text(text)
    for paragraf in paragrafe_text:
        ok = 0
        prop_paragraf = modul_1.text_sentences(paragraf)
        for prop in prop_paragraf:
            if prop in lista_prop_alese:
                text_reconstruit = text_reconstruit + prop + ' '
                ok = 1
            else:
                print(prop)
        if ok == 1:
            text_reconstruit =text_reconstruit + "\n" + "   "

    return text_reconstruit
