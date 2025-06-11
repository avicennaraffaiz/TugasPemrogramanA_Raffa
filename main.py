import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from numpy.polynomial.polynomial import polyfit, Polynomial

# Load dataset
df = pd.read_csv("Data Tugas Pemrograman A.csv")

# Missing years
target_years = [2005, 2006, 2015, 2016]

# Interpolation
interp_pop = interp1d(df['Year'], df['Population'], kind='cubic')
interp_pct = interp1d(df['Year'], df['Percentage_Internet_User'], kind='cubic')

# Estimasi nilai hilang
missing_pop = interp_pop(target_years)
missing_pct = interp_pct(target_years)

print("Interpolasi Data Hilang:")
for y, p, pct in zip(target_years, missing_pop, missing_pct):
    print(f"{y}: Populasi = {int(p):,}, Internet = {pct:.2f}%")

# Polynomial regression orde 3
x = df['Year']
y_pop = df['Population']
y_pct = df['Percentage_Internet_User']

coefs_pop = polyfit(x, y_pop, 3)
coefs_pct = polyfit(x, y_pct, 3)

poly_pop = Polynomial(coefs_pop)
poly_pct = Polynomial(coefs_pct)

print("\nPersamaan Polinomial:")
def format_poly(p, label):
    terms = [f"{coef:.6f}x^{i}" if i > 1 else f"{coef:.6f}x" if i == 1 else f"{coef:.6f}" for i, coef in enumerate(p.coef)]
    terms.reverse()
    return label + " = " + " + ".join(terms)

print(format_poly(poly_pop, "Populasi"))
print(format_poly(poly_pct, "Internet"))

# Prediksi
pop_2030 = poly_pop(2030)
pct_2035 = poly_pct(2035)

# Estimasi pengguna internet 2035 = % * populasi
pop_2035 = poly_pop(2035)
user_2035 = pop_2035 * pct_2035 / 100

print("\nPrediksi:")
print(f"Populasi 2030: {int(pop_2030):,}")
print(f"Persentase pengguna internet 2035: {pct_2035:.2f}%")
print(f"Estimasi pengguna internet 2035: {int(user_2035):,}")

# Plot
years = np.arange(1960, 2036)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(x, y_pop, 'bo', label='Data Asli')
plt.plot(years, poly_pop(years), 'r-', label='Regresi')
plt.title('Regresi Populasi')
plt.xlabel('Tahun')
plt.ylabel('Populasi')
plt.legend()

plt.subplot(1,2,2)
plt.plot(x, y_pct, 'go', label='Data Asli')
plt.plot(years, poly_pct(years), 'm-', label='Regresi')
plt.title('Regresi % Pengguna Internet')
plt.xlabel('Tahun')
plt.ylabel('% Pengguna Internet')
plt.legend()

plt.tight_layout()
plt.savefig("grafik_regresi.png")
plt.show()
