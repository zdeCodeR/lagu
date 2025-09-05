import time
import re
import sys

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
    jeda = durasi / len(teks)  
    for h in teks:
        sys.stdout.write(h)
        sys.stdout.flush()
        time.sleep(jeda)
    print()  

def main():
    lirik = load_lrc("otuan.lrc")

    print("=== O'Tuan ===\n")
    start = time.time()
    for i in range(len(lirik)):
        waktu, teks = lirik[i]
        # durasi = waktu baris berikutnya - waktu baris sekarang
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