

# 🛒 E-Commerce Image Intelligence

### Modular Web Scraping & Image Analytics Pipeline

A professional, modular Python system that automatically **scrapes product data, downloads images, performs computer vision processing, and generates visual insights** from an e-commerce platform.

This project demonstrates a production-ready data pipeline combining **web scraping, image engineering, and data science**.

---

# 📌 Project Overview

This project implements a **decoupled data pipeline** that separates the "heavy lifting" from the "analysis":

1. **Extraction**: Scrapes product metadata from a demo e-commerce site.
2. **Ingestion**: Downloads raw product images systematically.
3. **Processing**: Uses OpenCV and PIL to resize, grayscale, and perform Canny Edge Detection.
4. **Intelligence**: Extracts visual features (brightness, file size) into a structured metadata file.
5. **Analytics**: Provides a clean Jupyter Dashboard for visualization.

---
---
Architecture:

<img width="513" height="2409" alt="image" src="https://github.com/user-attachments/assets/ef91bfdb-4349-4538-bdcb-d6dac6972b94" />




# 📂 Project Structure


```text
ecommerce-image-intelligence/
├── .gitignore              # Excludes venv/ and large data/ files from Git
├── README.md               # Project documentation (this file)
├── requirements.txt        # Project dependencies (pandas, opencv, etc.)
├── notebooks/
│   └── analysis.ipynb      # Visualization Dashboard & Final Reports
├── src/                    # Logic Layer (The Engine)
│   ├── scraper.py          # Web scraping & Raw image downloading
│   ├── processor.py        # Image transformations & Feature extraction
│   └── utils.py            # Shared helpers (Path management & Folder setup)
├── data/                   # Data Layer (Storage)
│   ├── metadata.csv        # Central "Database" of all product intelligence
│   ├── raw/                # Original downloaded images
│   └── processed/          # Transformed images (Edge Detection/Grayscale)
└── venv/                   # Local Python Virtual Environment
```

---

# ⚙️ Installation & Setup

### 1. Clone and Navigate
```bash
cd ecommerce-image-intelligence
```

### 2. Setup Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
pip install -r requirements.txt
```

---

# ▶️ Running the Pipeline

To see the system in action, follow these steps in order:

### Step 1: Run the Scraper
This collects metadata and downloads original images to `data/raw/`.
```bash
python src/scraper.py
```

### Step 2: Run the Image Processor
This applies OpenCV transformations and saves "Intelligence" (brightness/stats) to `data/metadata.csv`.
```bash
python src/processor.py
```

### Step 3: View the Analysis
Open the notebook to view the charts, histograms, and image comparisons.
```bash
jupyter notebook notebooks/analysis.ipynb
```

---

# 🧩 Functional Modules

### 1️⃣ Web Scraping (`src/scraper.py`)
* **Technology**: BeautifulSoup4 & Requests.
* **Logic**: Extracts Title, Price, and Image URLs; handles relative pathing.

### 2️⃣ Image Engineering (`src/processor.py`)
* **Transformations**: Resizing (200x300), Grayscale conversion.
* **Computer Vision**: OpenCV Canny Edge Detection to highlight product contours.
* **Feature Extraction**: Calculates average brightness and storage footprint.

### 3️⃣ Analytics Dashboard (`notebooks/analysis.ipynb`)
* **Visuals**: Pixel intensity histograms, Brightness distribution.
* **Comparison**: Side-by-side display of Raw vs. Edge-Detected products.

---# 📊 Web Scraping Performance Comparison

To evaluate scraping performance, three Python libraries were tested:

* **BeautifulSoup**
* **lxml**
* **Selenium**

### Performance Results

| Library       | Pages | Products Scraped | Execution Time (s) | Memory Used (MB) | Errors | Duplicates | Missing Values |
| ------------- | ----- | ---------------- | ------------------ | ---------------- | ------ | ---------- | -------------- |
| BeautifulSoup | 3     | 60               | 4.61               | 1.52             | 0      | 0          | 0              |
| lxml          | 3     | 60               | **4.33**           | **0.00**         | 0      | 0          | 0              |
| Selenium      | 3     | 15               | 10.59              | 0.00             | 0      | 0          | 0              |
| **Average**   | **3** | **45**           | **6.51**           | **0.51**         | **0**  | **0**      | **0**          |


---

# 🛠 Technologies Used

* **Python 3.9+**
* **OpenCV**: Computer Vision / Edge Detection.
* **Pillow (PIL)**: Image resizing and handling.
* **Pandas**: Data structuring and CSV management.
* **Matplotlib**: Data visualization.
* **BeautifulSoup4**: HTML Parsing.

---

# 📌 Key Learning Outcomes

* **Modular Programming**: Separating scraping logic from processing logic.
* **Data Persistence**: Managing a `metadata.csv` as a local database.
* **Computer Vision Basics**: Understanding how edge detection extracts product features.
* **Pipeline Automation**: Building a system where data flows from the web to a chart automatically.

---
