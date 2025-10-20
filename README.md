# 🧹 Data Analyst Internship – Task 1
### **Task: Data Cleaning and Preprocessing**

---

## 📊 Dataset Information
**Dataset Used:** Medical Appointment No Shows (Kaggle)  
**File Name:** KaggleV2-May-2016.csv  
**Records:** 110,527  
**Columns:** 14  

This dataset contains information about patient medical appointments in Brazil and whether or not patients showed up for their appointment.

---

## 🧩 Objective
The main goal of this task was to clean and preprocess the raw dataset by:
- Handling missing values and duplicates
- Standardizing inconsistent data formats
- Fixing invalid entries
- Preparing a clean version ready for analysis

---

## 🧠 Tools Used
- **Python 3 (Jupyter Notebook)**
- **Pandas** for data cleaning
- **Excel** (for file format verification)

---

## ⚙️ Data Cleaning Steps Performed
1. **Loaded the dataset** using Pandas.  
2. **Checked for missing values** using `df.isnull().sum()` — no missing values found.  
3. **Removed duplicate rows** using `df.drop_duplicates()`.  
4. **Renamed columns** to lowercase with underscores for consistency.  
   Example: `AppointmentDay` → `appointmentday`
5. **Fixed invalid ages** by removing negative age values.  
6. **Converted datetime columns** (`ScheduledDay`, `AppointmentDay`) into standard datetime format.  
7. **Removed timezone info** using `.dt.tz_localize(None)` to make Excel-compatible.  
8. **Standardized text formats**:  
   - Converted all genders to uppercase (`M`, `F`)  
   - Capitalized "No-show" column values (`Yes`, `No`)  
9. **Verified data types** and ensured consistency across columns.  
10. **Exported cleaned dataset** into two formats:
    - `cleaned_data.csv`
    - `cleaned_data.xlsx`

---

## 📁 Files Included
| File Name | Description |
|------------|-------------|
| `KaggleV2-May-2016.csv` | Original raw dataset |
| `task1.ipynb` | Jupyter Notebook with complete cleaning code |
| `cleaned_data.csv` | Final cleaned dataset (CSV format) |
| `cleaned_data.xlsx` | Final cleaned dataset (Excel format) |
| `README.md` | Documentation of the task |

---



## 🧑‍💻 Author
**Monika Sharma**  
B.Tech CSE | Data Science Enthusiast  
GitHub: [yourusername](https://github.com/Monika808)  
