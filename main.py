
import interest
import display

print("=== Program Kalkulator Bunga Tabungan ===")

principal = float(input("Masukkan saldo awal: "))
rate = float(input("Masukkan bunga tahunan: "))
years = int(input("Masukkan lama menabung (tahun): "))

ci = interest.compound_interest(principal, rate, years)
si = interest.simple_interest(principal, rate, years)

display.print_result(principal, rate, years, ci, si)
