import pandas as pd 
data = [10, 20, 30, 40] 
v = pd.Series(data) 
# print(v) 
data = { 
    'Name': ['Alice', 'Bob', 'Charlie'], 
    'Age': [25, 30, 35], 
    'City': ['New York', 'Los Angeles', 'Chicago'] 
} 
df = pd.DataFrame(data) 
print(df) 