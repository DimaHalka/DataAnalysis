import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('../datasets/AmesHousing.csv')

df = df[['SalePrice', 'Gr Liv Area']].dropna()

# Create bins for the living area
df['AreaBin'] = pd.cut(df['Gr Liv Area'], 
                       bins=[0, 1000, 1500, 2000, 2500, 3000, 4000, 5000], 
                       labels=['<1000', '1000-1500', '1500-2000', '2000-2500', '2500-3000', '3000-4000', '4000+'])

# Plot
plt.figure(figsize=(12, 6))
sns.boxplot(x='AreaBin', y='SalePrice', data=df)
plt.title('House Price vs Living Area (Grouped)')
plt.xlabel('Living Area (sq ft)')
plt.ylabel('Sale Price ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

