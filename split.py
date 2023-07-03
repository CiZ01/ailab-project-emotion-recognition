import os
import random
import shutil

# Percorsi dei dataset di addestramento, convalida e destinazione
train_path = './dataset/train'
val_path = './dataset/val'
test_path = './dataset/test'

# Frazione del dataset di addestramento da assegnare alla convalida
val_fraction = 0.1

# Creazione della cartella di convalida (val)
os.makedirs(val_path, exist_ok=True)

# Ottieni la lista di file nel dataset di addestramento
dir_list = os.listdir(train_path)

for dir in dir_list:
    val_class_path = os.path.join(val_path, dir)
    os.makedirs(val_class_path, exist_ok=True)
    
    train_class_path = os.path.join(train_path, dir)
    # Ottieni la lista di file nella sottocartella
    file_list = os.listdir(train_class_path)
    
    # Calcola il numero di file da assegnare alla convalida
    num_val_files = int(len(file_list) * val_fraction)

    # Genera un elenco casuale di file da spostare nella convalida
    random.seed(42)
    val_files = random.sample(file_list, num_val_files)

    # Sposta i file dalla cartella di addestramento alla cartella di convalida
    for file in val_files:
        src = os.path.join(train_class_path, file)
        dst = os.path.join(val_class_path, file)
        shutil.move(src, dst)

print(f"{num_val_files} files moved from train to val.")

# Ora il dataset di addestramento contiene solo i file rimanenti
remaining_files = os.listdir(train_path)
num_train_files = len(remaining_files)

print(f"Remaining train files: {num_train_files}.")
