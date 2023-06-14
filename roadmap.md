# AiLab Project Roadmap

Vogliamo costruire un modello di riconoscimento delle emozioni facciali che sia in grado di riconoscere le emozioni di una persona. Dopo aver addestrato il modello vogliamo sviluppare un sistema per il riconoscimento facciale in tempo reale e il riconoscimento di più persone contemporaneamente da un'immagine.

## Roadmap

_può essere utile [questa chat](https://chat.openai.com/share/3c45a9a6-212b-4d34-b056-fd994322ed04) con chatGPT_

_leggere anche il file [README.md](README.md) per installare le dipendenze._

### 1. Scelta del dataset
Come dataset è stato scelto [FER2013](https://www.kaggle.com/datasets/msambare/fer2013), questa versione è più piccola dell'originale e presenta problemi di bilanciamento ma è gratuita, abbiamo le immagini e il csv.

### 2. Bilanciamento

Assicurarsi che il dataset sia bilanciato, [quello scelto](#1-scelta-del-dataset) come già detto presenta problemi di bilanciamento, quindi è necessario bilanciarlo.

|![](https://i.ibb.co/ThjTVhC/dataset-graph.png)| ![](https://i.ibb.co/CPTDPhd/chart.png)|
|---|---|

Per bilanciarlo possiamo usare varie tecniche, abbiamo quella [spiegata dal prof](bindare pdf), l'oversampling e l'undersampling, pesi della classe e ecc.

### 3. Estrazioe delle caratteristiche dalle immagini
Per l'estrazione delle caratteristiche possiamo usare varie tecniche, abbiamo quella [spiegata dal prof](bindare pdf), immagino che l'idea generale sia usare openCV estrando i keypoints con gli algoritmi spiegati[8], reti neurali e/o algoritmi di machine learning[2] oppure al limite usare il csv coi dati già estratti[6].

### 4. Addestramento del modello

Per l'addestramento del modello useremo __sci-kit learn__ e __pythorch__, possiamo usare Support Vectore Machine[8] (SVM), Random Forest[?] o Artifical Neural Network[2].

### 5. Valutazione e validazione del modello

Valutiamo le prestazioni calcolando le metriche come l'accuracy, la precision, la recall e la f1-score[?].

### 6. Ottimizatione del modello

Sperimentiamo con diversi algoritmi di ML[1], parametri e techinche di estrazione come: grid search, random search per trovare parametri migliori.

### 7. Applicazione del modello
A questo punto il nostro modello funziona e abbiamo fatto il grosso del progetto.

## Side quest

Come già detto vogliamo sviluppare un sistema per il riconoscimento facciale in tempo reale e il riconoscimento di più persone contemporaneamente da un'immagine.

### 1. Riconoscimento in tempo reale

Per il riconoscimento facciale in tempo reale possiamo usare __openCV__ che ci permette di aprire una finestra con la webcam ed estrarre i frame che registra. Useremo sempre __openCV__ per il riconoscimento faccciale, quindi scontornare un rettangolo intorno al viso.


### 1.1 Riconoscimento facciale

Per il riconoscimento facciale possiamo usare __opencv__ qua troviamo come farlo molto semplicemente [Face Detection.](https://www.datacamp.com/tutorial/face-detection-python-opencv), non so se __dlib__ è più potente. [Prima implementazione della funzione.](face-detection-test.ipynb). Va solo implementata l'estrazione.

### 2. Riconoscimento multiplo da immagine

Il [metodo visto precedentemente](#11-riconoscimento-facciale) permette di riconoscere più visi contemporanemente nella stessa immagine.
