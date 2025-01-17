class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.p = panjang
        self.l = lebar
    
    def keliling(self):
        return 2 * (self.p + self.l)
    
    def luas(self):
        return self.p * self.l
    
    def __str__(self):
        return f"Persegi Panjang, panjang {self.p} cm, dan lebar {self.l} cm"
    
def main():
    try:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))

        persegipanjang = PersegiPanjang(panjang, lebar)

        print(persegipanjang)
        print("Keliling:", persegipanjang.keliling())
        print("Luas:", persegipanjang.luas())

    except ValueError:
        print("Maaf, input tidak valid")

# Memanggil fungsi main
if __name__ == "__main__":
    main()
