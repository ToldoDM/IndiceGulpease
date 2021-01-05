# Calcolare l'indice di Leggibilita' di un PDF

import textract
import re

def indiceGulpease(testo, path):
    parole = len(re.findall(r'\w+', testo))
    lettere = len(re.findall(r'\w', testo))

    ps = len(re.findall('[.]+\s', testo)) #prende tutti i punti seguiti da spazi o a capo
    pv = len(re.findall('[;]+\s', testo)) #prende tutti i ';' seguiti da uno spazio o a capo
    pp = len(re.findall('[.]+\s+[.]', testo)) #prende tutti i '. .': è molto utile se usate LaTeX, dove nella tableOfContents ci sono tutti i punti per ogni sezione
    dp = len(re.findall('[:]+\n', testo))  #prende tutti i ':' seguito da un a capo
    vc = len(re.findall('[,]+\n', testo)) #prende tutte le virgole seguite da un a capo (ho preso come riferimento l'inizio delle lettere dove si scrive 'Caro Rossi Mario,(\n)')
    vp = len(re.findall('[v]+[.]+\s', testo)) #Utile se avete diciture nel vostro documento (se per esempio sono presenti diciture di versioni 'v. ', USATELA SOLO SE AVETE UNO SPAZIO DOPO IL PUNTO, DATO CHE È CONTATO IN ps)

    #come si può vedere, pp è contato due volte, questo perchè una volta che conta '. .' passa alla dicitura seguente.
    # ad esempio se ci sono '. . . . .'  conta 2 occorrenze '[. .] [. .] .', quando in realtà ne sono presenti 4
    punti = ps + pv + dp + vc - (pp)*2 - vp

    #da come potete intuire nell'esempio sopra descritto, il conteggio dei punti (aka frasi)
    #non è del tutto corretto: sono riuscito a stimare uno scarto del 15% in base a dei documenti esempio (corti) in mio possesso
    #che riuscissero a rappresentare degli scenari tipo, in modo tale che potessi calcolare l'indice a mano: il conteggio delle frasi e parole
    #è abbastanza corretto (anche qui ovviamente ci sarà un piccolo errore), il problema stava maggiormente nel riconoscimento delle frasi.
    puntiUP = punti + (punti / 100 * 15)
    puntiDOWN = punti - (punti / 100 * 15)

    indiceG = 89 + ((300 * punti) - (10 * lettere)) / parole
    indiceGUP = 89 + ((300 * puntiUP) - (10 * lettere)) / parole
    indiceGDOWN = 89 + ((300 * puntiDOWN) - (10 * lettere)) / parole
    print("Documento " + path)
    print("numero di parole presenti nei doc :   " + str(parole))
    print("numero di lettere presenti nei doc :  " + str(lettere))
    print("numero di frasi presenti nei doc :    " + str(punti))
    print("")
    if parole != 0:
        if indiceG > 100:
            indiceG = 100

        print("indice di Gulpease restrittivo : " + str(indiceG))
        print("indice di Gulpease scarto + 15% : " + str(indiceGUP))
        print("indice di Gulpease scarto - 15% : " + str(indiceGDOWN))
    else:
        print("Errore nel calcolo dell'indice Gulpease")


    print("")
    print("")


if __name__ == "__main__":
    doc = "/<PATH ASSOLUTO O RELATIVO>/doc.pdf"
    indiceGulpease(textract.process(doc, method='pdftotext').decode("UTF8"), doc)

