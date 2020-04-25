import pandas as pd
import numpy as np
import itertools

from scipy.stats import chi2_contingency

import seaborn as sns; 
sns.set()
import matplotlib.pyplot as plt

disciplines = ["Medicine","Literature","Peace","Physics","Chemistry","Economy"]

subContinents = ["South America","Western Africa","Central America","Eastern Africa","Northern Africa","Southern Africa","Northern America","Caribbean","Eastern Asia","Southern Asia","South-Eastern Asia","Southern Europe","Australia and New Zealand","Western Asia","Eastern Europe","Northern Europe","Western Europe"]

#read data from csv
nobelDataDf = pd.read_csv("Nobel_N2")

#turn to numpy array
nobelData = nobelDataDf.to_numpy()

#total of all nobel prizes
grandTotal = np.sum(nobelData)

#we will work with proportions 
correspondenceMatrix = np.divide(nobelData,grandTotal)


#row and column marginal totals
# axis=0 veut dire somme en itérant sur l'axe 0
rowTotals = np.sum(correspondenceMatrix, axis=1)
columnTotals = np.sum(correspondenceMatrix, axis=0)

#Independence matrix
independenceModel = np.outer(rowTotals, columnTotals)


#use chi squared to verify the dependence of qualitative variable 
'''
chiSquaredStatistic = grandTotal*np.sum(np.square(correspondenceMatrix-independenceModel)/independenceModel)
#print("Chi-2 statistique calcul manuel")
#print(chiSquaredStatistic)


# Quick check - compare to scipy Chi-Squared test
statistic, prob, dof, ex = chi2_contingency(nobelData)
#print("\n Vérification")
#print(statistic)
'''

#Residuals by subtracting the expected proportions from the observed proportions
standardizedResiduals = np.divide((correspondenceMatrix-independenceModel),np.sqrt(independenceModel))

#singular value decomposition(SVD)
u,s,vh = np.linalg.svd(standardizedResiduals, full_matrices=False)

# u contains the left singular vectors.
# vh contains the right singular vectors.
# s contains the singular values.

#unweight the SVD's outputs
#unweight for rows
stdRows = np.zeros((u.shape[0],u.shape[1]))
for i in range(u.shape[0]):
    stdRows[i] = np.divide(u[i],np.sqrt(rowTotals[i]))

#unweight for colomns
stdCols = np.zeros((vh.shape[0],vh.shape[1]))
for i in range(vh.shape[0]):
    stdCols[i] = np.divide(vh[i],np.sqrt(columnTotals[i]))

#compute rows and colomns coordinates
rowCoordinates = np.dot(stdRows,np.diag(s))
colCoordinates = np.dot(stdCols,np.diag(s))

#turn to dataframe, that woult be easy to plot the result 
dfFirstTwoComponentsR = pd.DataFrame(data=[l[0:2] for l in rowCoordinates], columns=['Factorial_axis_1', 'Factorial_axis_2'], index=subContinents)
dfFirstTwoComponentsC = pd.DataFrame(data=[l[0:2] for l in colCoordinates], columns=['Factorial_axis_1', 'Factorial_axis_2'], index=disciplines)
dfFirstTwoComponents =  dfFirstTwoComponentsR.append(dfFirstTwoComponentsC)

#see what our final data looks like 
print(dfFirstTwoComponents) 

points = subContinents + disciplines


#plot the points 
fig, ax_kwargs = plt.subplots()
plt.scatter(dfFirstTwoComponentsR['Factorial_axis_1'], dfFirstTwoComponentsR['Factorial_axis_2'], s = 40, c = 'red')
plt.scatter(dfFirstTwoComponentsC['Factorial_axis_1'], dfFirstTwoComponentsC['Factorial_axis_2'], s = 40, c = 'blue')
plt.title('scatter plot')
ax_kwargs.axvline(c='grey', lw=1)
ax_kwargs.axhline(c='grey', lw=1)

#ax_kwargs.scatter(dfFirstTwoComponents['Factorial_axis_1'], dfFirstTwoComponents['Factorial_axis_2'])

for i, txt in enumerate(points):
    ax_kwargs.annotate(txt, (dfFirstTwoComponents['Factorial_axis_1'][i], dfFirstTwoComponents['Factorial_axis_2'][i]),horizontalalignment='center', verticalalignment='center',size=7)
plt.show()


#autre affichage disponile 
'''
ax = sns.scatterplot(data=dfFirstTwoComponentsR,x='Factorial_axis_1', y='Factorial_axis_2', hue=subContinents, color='.2')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.get_legend().set_visible(False)

for label in points:
    plt.annotate(label, 
                 (dfFirstTwoComponents.loc[label,:]['Factorial_axis_1'],
                  dfFirstTwoComponents.loc[label,:]['Factorial_axis_2']),
                 horizontalalignment='center', verticalalignment='center',size=11)
#plt.scatter(subContinents,disciplines)   
plt.show()
'''





