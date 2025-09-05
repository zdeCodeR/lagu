import time
import re
import sys

HIJAU = "\033[92m"
KUNING = "\033[93m"
RESET = "\033[0m"

def load_lrc(filename):
    pattern = re.compile(r"\[(\d+):(\d+\.\d+)\](.*)")
    lirik = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            match = pattern.match(line.strip())
            if match:
                menit = int(match.group(1))
                detik = float(match.group(2))
                teks = match.group(3).strip()
                waktu = menit * 60 + detik
                lirik.append((waktu, teks))
    return sorted(lirik, key=lambda x: x[0])

def tampilkan_per_huruf(teks, durasi):
    if not teks:
        print()
        return
    panjang = len(teks)
    jeda = durasi / panjang if panjang > 0 else 0.1

    for i in range(panjang):
        sudah = teks[:i+1]
        sisa = teks[i+1:]
        sys.stdout.write("\r" + HIJAU + sudah + RESET + sisa)
        sys.stdout.flush()
        if teks[i] == " ":
            time.sleep(jeda * 0.4)
        elif teks[i].lower() in "aiueo":
            time.sleep(jeda * 1.2)
        else:
            time.sleep(jeda)
    print() 

def main():
    lirik = load_lrc("otuan.lrc")

    print("=== Karaoke O'Tuan (smooth huruf demi huruf) ===\n")
    start = time.time()
    for i in range(len(lirik)):
        waktu, teks = lirik[i]
        if i < len(lirik) - 1:
            durasi = lirik[i+1][0] - waktu
        else:
            durasi = 3  
        while time.time() - start < waktu:
            time.sleep(0.01)
        tampilkan_per_huruf(teks, durasi)

    print("\n=== Tamat ===")

if __name__ == "__main__":
    main()