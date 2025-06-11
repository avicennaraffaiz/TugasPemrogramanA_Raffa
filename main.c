#include <stdio.h>

// Data populasi contoh untuk regresi sederhana (orde 2)
int years[] = {2010, 2020, 2023};
double population[] = {242968342, 273523615, 277534122};

double lagrange(double x, int n, int x_vals[], double y_vals[]) {
    double result = 0.0;
    for (int i = 0; i < n; i++) {
        double term = y_vals[i];
        for (int j = 0; j < n; j++) {
            if (i != j) {
                term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j]);
            }
        }
        result += term;
    }
    return result;
}

int main() {
    int n = sizeof(years) / sizeof(years[0]);

    double year_2030 = 2030;
    double pred_pop_2030 = lagrange(year_2030, n, years, population);

    printf("Prediksi Populasi Indonesia 2030 (Lagrange, orde 2): %.0f\n", pred_pop_2030);

    // Prediksi jumlah pengguna internet tahun 2035
    int years_pct[] = {2010, 2020, 2023};
    double pct[] = {10.92, 53.72, 71.71};
    double pop_2035 = lagrange(2035, n, years, population);
    double pct_2035 = lagrange(2035, n, years_pct, pct);
    double user_2035 = pop_2035 * pct_2035 / 100.0;

    printf("Persentase pengguna internet 2035: %.2f%%\n", pct_2035);
    printf("Estimasi jumlah pengguna internet 2035: %.0f\n", user_2035);

    return 0;
}
