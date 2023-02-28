import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

project_df = pd.read_excel('Project_File.xlsx')
print(project_df)

project_df.dropna()

project_df.columns = ['Year', 'United Kingdom', 'Germany', 'France', 'Italy', 'Netherlands', 'Greece', 'Belgium & Luxembourg', 'Switzerland', 'Austria', 'Scandinavia', 'CIS & Eastern Europe']
print(project_df)

#sns.histplot(data=project_df, x="Germany", bins=10)
#plt.show()

#sns.histplot(data=project_df, x="France", bins=10)
#plt.show()

#sns.histplot(data=project_df, x="United Kingdom", bins=10)
#plt.show()

#sns.histplot(data=project_df, x="Italy", bins=10)
#plt.show()

#sns.histplot(data=project_df, x="Netherlands", bins=10)
#plt.show()

#sns.histplot(data=project_df, x="Greece", bins=10)
#plt.show()

#sns.histplot(data=project_df, x="Belgium & Luxembourg", bins=10)
#plt.show()

#sns.histplot(data=project_df, x="Switzerland", bins=10)
#plt.show()

#sns.histplot(data=project_df, x="Austria", bins=10)
#plt.show()

#sns.histplot(data=project_df, x="Scandinavia", bins=10)
#plt.show()

#sns.histplot(data=project_df, x="CIS & Eastern Europe", bins=10)
#plt.show()

#CHARTS WE CHOOSING : highest (CIS & EE , UK , GER) lowest (AUSTRIA , GREECE)
