# Seaborn 

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")


sns.regplot(x="total_bill", y="tip", data=tips);
plt.show()