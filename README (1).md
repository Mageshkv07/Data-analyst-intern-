# Medical Appointment No Shows - Data Cleaning

This project involves cleaning a dataset for **Medical Appointment No Shows**. The dataset contains patient information such as demographics, appointment details, and attendance status.

## 🧹 Cleaning Objectives

The script `clean_data.py` performs the following data cleaning steps:

- ✅ **Handled missing values** using median imputation for the `Income` column.
- ✅ **Removed duplicate rows** to ensure data consistency.
- ✅ **Standardized text fields** such as `Education`, `Marital_Status`, `Gender`, and `Country`.
- ✅ **Converted date fields** (`Dt_Customer`) to a consistent `dd-mm-yyyy` datetime format.
- ✅ **Renamed column headers** to lowercase and replaced spaces with underscores.
- ✅ **Fixed data types** for columns like `Year_Birth` (int), `Income` (float), and `Dt_Customer` (datetime).
- ✅ **Saved the cleaned dataset** as `cleaned_medical_appointments.csv` using **space** as the delimiter.

---

## 📁 Files Included

| File                              | Description                                      |
|-----------------------------------|--------------------------------------------------|
| `medical_appointments.csv`        | Raw input dataset (tab-separated)               |
| `clean_data.py`                   | Python script to clean the dataset              |
| `cleaned_medical_appointments.csv`| Cleaned output dataset (space-separated)        |
| `README.md`                       | This documentation                              |

---

## ▶️ How to Run

1. Place the original `medical_appointments.csv` file in the same directory.
2. Run the script:
   ```bash
   python clean_data.py
