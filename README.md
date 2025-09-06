# Facial Emotion Recognition (AiLab 2022/23)

A simple project for recognizing facial emotions from images and live video. Built around a VGG16 backbone, trained on FER-2013, and topped off with a real-time webcam demo.

---

## Team

* [Francesco Fazzari](https://github.com/CiZ01)
* [Gabriele Fabro](https://github.com/gabrielefabro)
* [Diego Spaziani](https://github.com/Spazio-D)
* [Elisa Locchi](https://github.com/Lokky99)

---

## Highlights

* **Dataset:** FER-2013 (Kaggle) — \~35.9k grayscale 48×48 face images across **7 classes**: *Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral*.
* **Model:** **VGG16** chosen for strong results with a simple, well-understood architecture.
* **Preprocessing:** Resize 48×48→224×224 and convert 1-channel grayscale → 3-channel RGB for VGG input.
* **Validation split:** Created our own **10%** validation set from training data (FER-2013 ships with train/test only).
* **Augmentation:** `RandomHorizontalFlip` to mitigate overfitting.
* **Training recipe:** Explored SGD/Adam; **final choice: AdamW** with CrossEntropyLoss, **lr=1e-4**, **weight\_decay=5e-4**, **epochs=50**, **early-stopping=20**. (Batch size **64** used in experiments.)
* **Live demo:** OpenCV webcam pipeline with Haar Cascade face detection; on user trigger, run classification and overlay the predicted emotion.

---

## Dataset

We use **FER-2013**, a widely-used facial expression dataset containing **35,887** grayscale **48×48** face images labeled into seven emotion categories (*anger, disgust, fear, happiness, sadness, surprise, neutral*). The official split provides training and test sets, so we set aside **10% of training** for validation. 

---

## Method

The model is based on **VGG16**. Images flow through stacked convolution + activation + pooling blocks; the final layers map extracted features to the seven emotion classes. VGG16 was selected for its strong performance and architectural simplicity for this task.

**Input adaptation.** Since FER-2013 images are 48×48×1 while VGG16 expects 224×224×3, we: (1) **resize** to 224×224, (2) **convert** grayscale to 3-channel RGB (PIL), and (3) apply standard **torchvision transforms**.

**Regularization.** To combat overfitting, we use **RandomHorizontalFlip** during training.

---

## Training

We tried several optimizer/parameter combos (e.g., **Adam** and **SGD** with **batch size 64** and **lr=1e-4**) and settled on the following final configuration for stability and weight-decay handling:

* **Optimizer:** **AdamW**
* **Loss:** **CrossEntropyLoss**
* **Learning rate:** `1e-4`
* **Weight decay:** `5e-4`
* **Epochs:** `50` (with **early stopping** after `20` epochs of no improvement)

---

## Real-Time Demo (Webcam)

A simple demo showcases the model in action:

1. Capture frames with **OpenCV VideoCapture**.
2. Detect faces via **Haar Cascades** to obtain bounding boxes and a cropped face image.
3. On user interrupt, run classification for the cropped face and **overlay** the predicted emotion above the bounding box in real time.

---

## Setup

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   > For **PyTorch**, follow the official selector for your OS/CUDA setup.

2. **Prepare the data**
   Download FER-2013 from Kaggle and place it where your training script/notebook expects it (see your local paths/scripts).

3. **Train / Evaluate**
   Use the provided training code or notebook in this repository to train on the FER-2013 training split, validate on the held-out 10%, and evaluate on the test set. (Hyperparameters above.)

4. **Run the demo**
   Ensure OpenCV is installed and that a Haar Cascade XML file is available; launch the webcam demo to see real-time predictions as described earlier.

---

## Notes & Tips

* FER-2013 images are low-resolution; consider mild blur/contrast normalization and careful augmentation to avoid degrading facial cues. (We used horizontal flips only.)
* Track validation early stopping to prevent overfitting and reduce unnecessary epochs.

---

## Acknowledgments

* **Dataset:** FER-2013 (Kaggle).
* **Architecture:** VGG16 (used as the backbone in this work).