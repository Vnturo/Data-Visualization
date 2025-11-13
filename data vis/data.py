import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from CSV file
data = pd.read_csv('data.csv')

sns.set(style="whitegrid")

cols = data.columns.tolist()

# Helper to create a bar chart for a column
def plot_bar_for_column(col_name, out_filename):
    if pd.api.types.is_numeric_dtype(data[col_name]):
        plt.figure(figsize=(10,6))
        sns.barplot(x=data.index, y=data[col_name], ci=None)
        plt.xlabel('Index')
        plt.ylabel(col_name)
        plt.title(f'Bar chart of {col_name} (values by row index)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(out_filename, dpi=300)
    else:
        vc = data[col_name].value_counts()
        plt.figure(figsize=(10,6))
        ax = vc.plot(kind='bar')
        ax.set_xlabel(col_name)
        ax.set_ylabel('Count')
        ax.set_title(f'Bar chart of {col_name} (value counts)')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(out_filename, dpi=300)

# Bar chart for first column (index 0)
if len(cols) >= 1:
    plot_bar_for_column(cols[0], 'bar_col1.png')
else:
    print("No first column found in data.csv")

# Pie chart for third column (index 2)
if len(cols) >= 3:
    col3 = cols[2]
    vc3 = data[col3].value_counts()
    plt.figure(figsize=(7,7))
    vc3.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.ylabel('')
    plt.title(f'Pie chart of {col3} (value distribution)')
    plt.tight_layout()
    plt.savefig('pie_col3.png', dpi=300)
else:
    print("No third column found in data.csv")

# Bar chart for fourth column (index 3)
if len(cols) >= 4:
    plot_bar_for_column(cols[3], 'bar_col4.png')
else:
    print("No fourth column found in data.csv")

plt.show()
