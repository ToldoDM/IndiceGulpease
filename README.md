# IndiceGulpease
Script python per il calcolo dell'indice di Gulpease di un documento PDF.

Questo script si basa sul lavoro eseguito da [imriccardop](https://github.com/imriccardop/Indice-Gulpease).


## Come usarlo
Lo script è stato creato per essere eseguito su **python3.6**, attualmente è stato testato solo su linux (18.04 LTS) da cmd.

Ps: funziona anche su python2 ma non è stato creato per questa versione (inoltre restituisce numeri diversi).


Per eseguire lo script è necessario il package *textract*, se non lo avete potete installarlo con il comando
```
 pip3 install textract
```
Prima di eseguirlo bisogna inserire il path del file pdf all'interno del main del file *IndiceGulpease.py*:
```
 if __name__ == "__main__":
    doc = "/<PATH ASSOLUTO O RELATIVO>/doc.pdf"
```
Per eseguire lo script è necessario usare il comando
```
 python3.6 IndiceGulpease.py
```
Dovrebbe risultarvi un output simile a questo:
```
  Documento /<PATH ASSOLUTO O RELATIVO>/doc.pdf
  numero di parole presenti nei doc :   3805
  numero di lettere presenti nei doc :  19248
  numero di frasi presenti nei doc :    262

  indice di Gulpease restrittivo : 59.070959264126145
  indice di Gulpease scarto + 15% : 62.16951379763469
  indice di Gulpease scarto - 15% : 55.97240473061761

```
------------------
Non è garantita una precisione del 100%, ne tantomento di uno scarto del 15%. Ho strutturato il seguente script secondo le mie esigenze e basato i calcoli su i miei tipi di documenti.
