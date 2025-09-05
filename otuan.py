import time
import re

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

def main():
    lirik = load_lrc("otuan.lrc")

    print("=== Karaoke O'Tuan ===\n")
    start = time.time()
    idx = 0
    while idx < len(lirik):
        sekarang = time.time() - start
        if sekarang >= lirik[idx][0]:
            print(">>> " + lirik[idx][1]) 
            idx += 1
        else:
            time.sleep(0.05)

    print("\n=== Tamat ===")

if __name__ == "__main__":
    main()