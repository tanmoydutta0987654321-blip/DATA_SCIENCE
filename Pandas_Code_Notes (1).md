# Pandas — Code Notes

All code snippets from the Pandas notes, grouped by section for quick reference.

## Installation & Setup

```bash
# Standard install
pip install pandas

# Install with optional extras (Excel, Parquet, etc.)
pip install 'pandas[all]'

# Via conda
conda install pandas

# Verify installation
python -c "import pandas as pd; print(pd.__version__)"
# Output: 2.2.1
```

## Importing Pandas

```python
# Standard import — always use this alias
import pandas as pd
import numpy as np   # almost always used alongside pandas

print('Pandas version:', pd.__version__)
print('NumPy version: ', np.__version__)
# Output:
# Pandas version: 2.2.1
# NumPy version:  1.26.4
```

## Key Features — Quick Reference

```python
pd.read_csv('file.csv')        # Data Loading
df.dropna()                    # Data Cleaning — drop missing values
df.fillna(0)                   # Data Cleaning — fill missing values
df['Salary'].mean()            # Data Analysis
df[df['Age'] > 25]             # Data Selection
df.groupby('Department')       # Data Transformation
df.isnull()                    # Handling Missing Data
```

## Creating a Series

```python
import pandas as pd

# Method 1: From a list (default numeric index)
s = pd.Series([10, 20, 30])
print(s)
```

```python
import pandas as pd

# From a list with a custom index
ages = pd.Series([25, 30, 28], index=['Alice', 'Bob', 'Charlie'])
print(ages)
```

```python
import pandas as pd

# From a dictionary (keys become the index)
ages_dict = {'Alice': 25, 'Bob': 30, 'Charlie': 28}
s = pd.Series(ages_dict)
print(s)
```

```python
import pandas as pd

# From a scalar (broadcast across the given index)
s = pd.Series(10, index=['a', 'b', 'c', 'd', 'e'])
print(s)
```

## Indexing and Slicing

```python
import pandas as pd

ages = pd.Series([25, 30, 28], index=['Alice', 'Bob', 'Charlie'])

# Access by label (recommended)
print(ages['Bob'])              # Output: 30

# Slicing by label — inclusive of both endpoints
print(ages['Alice':'Bob'])
```

```python
import pandas as pd

ages = pd.Series([25, 30, 28], index=['Alice', 'Bob', 'Charlie'])

# Access by position — use .iloc, not ages[0]
print(ages.iloc[0])             # Output: 25

# First two elements by position
print(ages.iloc[0:2])
```

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40, 50])

# Slicing by position (like Python lists) — stop index is exclusive
print(s.iloc[1:4])              # positions 1, 2, 3 (not 4)
```

```python
import pandas as pd

ages = pd.Series([25, 30, 28, 35], index=['Alice', 'Bob', 'Charlie', 'Diana'])

# Conditional indexing / filtering
old_people = ages[ages > 28]
print(old_people)
```
