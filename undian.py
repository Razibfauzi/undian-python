import random
import time

peserta = input("Masukkan nama peserta (pisahkan dengan koma): ").split(',')
peserta = [nama.strip() for nama in peserta]

print("Mengundi pemenang", end="")
for _ in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)


pemenang = random.choice(peserta)


time.sleep(1)
print(f"\n🎉 Selamat! Pemenangnya adalah: {pemenang} 🎊")
