import tkinter as tk
from tkinter import messagebox
import time
import threading
import platform

# Ses çalma fonksiyonu (platforma göre)
def play_sound():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(100, 2000)  # 1000 Hz, 0.5 second
    else:
        print("\a")  # Unix-like sistemlerde terminal bip sesi

# Zamanlayıcı fonksiyonu
def start_timer():
    def countdown():
        try:
            minute = int(entry_minute.get())
            second = int(entry_second.get())
            total_second = minute * 60 + second
            taskname = entry_taskname.get() or "Görev"

            while total_second > 0:
                minute, second = divmod(total_second, 60)
                label_sure.config(text=f"Kalan süre: {minute:02}:{second:02}")
                time.sleep(1)
                total_second -= 1

            label_sure.config(text="Süre doldu!")
            play_sound()
            messagebox.showinfo("Zamanlayıcı", f"{taskname} süresi doldu!")
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli sayı girin!")

    threading.Thread(target=countdown).start()

# Arayüz
pencere = tk.Tk()
pencere.title("Görev Zamanlayıcı")
pencere.geometry("300x300")

# Görev adı
tk.Label(pencere, text="Görev Adı:").pack()
entry_taskname = tk.Entry(pencere)
entry_taskname.pack()

# dakika ve second
tk.Label(pencere, text="Dakika:").pack()
entry_minute = tk.Entry(pencere)
entry_minute.pack()

tk.Label(pencere, text="Saniye:").pack()
entry_second = tk.Entry(pencere)
entry_second.pack()

# Başlat butonu
tk.Button(pencere, text="Zamanlayıcıyı Başlat", command=start_timer).pack(pady=10)

# Kalan süre
label_sure = tk.Label(pencere, text="")
label_sure.pack()

# Başlat
pencere.mainloop()
