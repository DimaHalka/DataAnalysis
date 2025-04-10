import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("../datasets/AmesHousing.csv")

plt.figure(figsize=(8, 4))
# sns.boxplot(y=df['SalePrice'])  # Vertically
sns.boxplot(x=df['SalePrice'])    # Horizontally
plt.title('Distribution of House Sale Prices')
plt.ylabel('Sale Price ($)')
plt.show()
