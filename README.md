# Student Data Cleaning

Simple pandas script that loads a students.csv file, reports missing values, fills gaps in numeric columns with each column's mean, and prints the cleaned dataset. Includes a sample CSV with blanks, requirements file, and README, so beginners can practice data cleaning in minutes.

## Setup

```bash
git clone https://github.com/<your-username>/student-data-cleaning.git
cd student-data-cleaning
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

The script reads `students.csv` from the same folder, then:

1. Prints the count of missing values per column
2. Fills missing numeric values with the column mean
3. Prints the missing-value counts again (all zero)
4. Shows the first rows of the cleaned dataset

Replace the sample file with your own data (keep the filename, or edit it in `main.py`). Non-numeric columns such as `name` are left untouched.

## Sample output

```
Missing Values:
 name       0
age        1
math       1
science    1
english    1
dtype: int64

After Cleaning:
 name       0
age        0
math       0
science    0
english    0
dtype: int64

Cleaned Dataset:
     name   age  math  science  english
0  Aarav  15.0  82.0     78.0     85.0
1   Diya  16.0  74.2     88.0     94.0
2  Kiran  15.8  67.0     72.0     70.0
3  Meera  17.0  75.0     78.8     68.0
4  Rohan  16.0  88.0     92.0     77.6
```
