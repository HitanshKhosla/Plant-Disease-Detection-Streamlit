

# 🌿 Plant Disease Detection

This project uses a Convolutional Neural Network (CNN) model to detect plant diseases from images. The model is built using **TensorFlow** and deployed using **Streamlit** for a user-friendly interface. The system allows users to upload images of plants and predict the presence of diseases based on a trained model.



## 🚀 Features

- **Disease Detection**: Detects plant diseases from images.
- **Streamlit Interface**: A simple web application to upload images and see predictions.
- **Model Training**: The model is trained using a dataset of plant disease images.
- **User-Friendly**: Upload images, get instant predictions with a click of a button.



## 📦 Requirements

Before running the project, ensure you have the following dependencies:

- Python 3.7 or higher
- TensorFlow
- Streamlit
- Pillow (PIL)
- Numpy
- Other dependencies listed in `requirements.txt`



## 🛠️ Installation

Follow these steps to get the project running locally:

### 1. Clone the repository:

```bash
git clone https://github.com/HitanshKhosla/plant-disease-detection.git
cd plant-disease-detection
```

### 2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:

```bash
.\venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt


## 🚀 Running the Application

To run the Streamlit app and test the plant disease detection, follow these steps:

### 1. Start Streamlit:

```bash
streamlit run app/main.py
```

This will launch the web application, and you can access it by opening `http://localhost:8501` in your web browser.

---

## 📂 Project Structure

```
plant-disease-detection/
│
├── app/                          # Contains application files
│   ├── main.py                   # Streamlit app file
│   ├── class_names.json          # JSON file with class labels
│   └── trained model/            # Directory with the trained model (e.g., .h5 file)
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```



## 📈 Model Details

The model used for disease detection is based on **Convolutional Neural Networks (CNNs)** and was trained on a dataset of plant disease images from the [PlantVillage Dataset](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset/data). It has been fine-tuned to classify the input images into various categories based on the disease.

---

## 👩‍💻 How to Contribute

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a pull request.

---

## 📑 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 Contact

For any questions or suggestions, feel free to reach out to:

- **Email**: hitanshkhosla200@gmail.com
- **GitHub**: [HitanshKhosla](https://github.com/HitanshKhosla)

