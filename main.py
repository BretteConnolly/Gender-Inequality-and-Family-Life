import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv("GII Data.csv")
df = pd.DataFrame(data)
print(df, "\n")

x = data.fertility_rate
y = data.GII

xmean = np.mean(x)
ymean = np.mean(y)

print(f'xmean = {xmean}')
print(f'ymean = {ymean}\n')

# Calculate the terms needed for the numator and denominator of beta
covariance = np.cov(x, y)
print(f'covariance = {covariance}\n')

variance = np.var(x)
print(f'variance = {variance}\n')  

# Calculate beta and alpha
beta = covariance[0][1] / variance
alpha = ymean - beta * xmean
print(f'alpha = {alpha}')
print(f'beta = {beta}\n')
correlation = np.corrcoef(x, y)
print(f'correlation coefficient = {correlation}\n')

#for x in x:
  #print(f'GII = {x}')
ypred = alpha + beta * x 
  #print(f'predicted fertility rate = {ypred}')

plt.figure(figsize=(6, 7))
plt.subplot(3, 1, 1)
plt.plot(x, y, 'ro')   # scatter plot showing actual data
plt.title('Children per Woman and Gender Inequality: r = 0.78')
plt.xlabel('Fertility Rate')
plt.ylabel('Gender Inequality')
plt.plot(x, ypred)     # regression line
#plt.show()

x2 = data.age_at_first_marriage
y = data.GII

xmean = np.mean(x2)
ymean = np.mean(y)

print(f'xmean = {xmean}')
print(f'ymean = {ymean}\n')

# Calculate the terms needed for the numator and denominator of beta
covariance = np.cov(x2, y)
print(f'covariance = {covariance}\n')

variance = np.var(x2)
print(f'variance = {variance}\n')  

# Calculate beta and alpha
beta = covariance[0][1] / variance
alpha = ymean - beta * xmean
print(f'alpha = {alpha}')
print(f'beta = {beta}\n')
correlation = np.corrcoef(x2, y)
print(f'correlation coefficient = {correlation}\n')

#for x in x:
  #print(f'GII = {x}')
ypred = alpha + beta * x2 
  #print(f'predicted fertility rate = {ypred}')

#plt.figure(figsize=(8, 4))
plt.subplot(3, 1, 3)
plt.plot(x2, y, 'ro')   # scatter plot showing actual data
plt.title('Age at First Marriage and Gender Inequality: r = -0.72')
plt.xlabel('Age at First Marriage')
plt.ylabel('Gender Inequality')
plt.plot(x2, ypred)     # regression line

plt.show()


# sources: 
# -- https://hdr.undp.org/data-center/thematic-composite-indices/gender-inequality-index#/indicies/GII 
# -- https://www.unfpa.org/data/world-population-dashboard