# 📊 ISPP Performance Analysis Scripts

Scripts to generate performance analysis graphs for group and individual analysis of the ISPP subject.

Developed by [@JuaniniGC](https://github.com/JuaniniGC)

---
## 📁 Project Structure

This repository contains Python scripts designed to analyze performance data from the ISPP subject. It supports both individual and group-level analytics through visualizations.

### 📂 `example_reports`

This folder contains example CSV reports that match the input format expected by the graphing and analysis scripts. These files serve as reference templates and test data to understand how the tools work. The structure of the data in these reports reflects real use cases, making it easy to verify script behavior and output accuracy. Use these examples to format your own data correctly before running the scripts.

### 📄 `requirements.txt`

This file lists all the Python dependencies required to run the scripts in the project. You can install them using:


```bash
pip install -r requirements.txt
```

## ⚙️ Requirements

- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)

---

## 🧪 Setting Up a Virtual Environment

To avoid dependency conflicts, it's recommended to use a virtual environment.

### Windows

```bash
python -m venv venv
.env\Scripts\activate
```

### macOS / Linux


```bash
python3 -m venv venv
source venv/bin/activate
```

You should see the environment name (`venv`) in your terminal prompt after activation.

---

## 📦 Installing Dependencies

Make sure you are in the root directory of the project (where `requirements.txt` is located), then run:


```bash
pip install -r requirements.txt
```

This will install all required Python packages for the scripts to work properly.

---

## 🚀 Running the Scripts

After setting up the environment and installing dependencies, you can run the scripts using:


```bash
python <script_name>.py
```

Example:


```bash
python group_analysis.py
```

Replace `<script_name>.py` with the actual name of the script you want to run.

---

## 🔄 Updating Dependencies

If you add or update packages, you can regenerate the `requirements.txt` file with:


```bash
pip freeze > requirements.txt
```

---

## ❌ Deactivating the Environment

To deactivate the virtual environment at any time:


```bash
deactivate
```

---

## 🧑‍💻 Author

Developed by [@JuaniniGC](https://github.com/JuaniniGC)