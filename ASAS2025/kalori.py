import ttkbootstrap as tb
from tkinter import messagebox

def hitung_kalori():
    try:
        umur = int(input_umur.get())
        berat = float(input_berat.get())
        tinggi = float(input_tinggi.get())
        kelamin = dropdown_kelamin.get().lower()
        tingkat_aktivitas = dropdown_aktivitas.current()

        if kelamin == "pria":
            bmr = 66.5 + (13.7 * berat) + (5 * tinggi) - (6.8 * umur)
        elif kelamin == "wanita":
            bmr = 655 + (9.6 * berat) + (1.8 * tinggi) - (4.7 * umur)
        else:
            messagebox.showerror("Error", "Silakan pilih jenis kelamin.")
            return

        faktor_aktivitas = [1.2, 1.3, 1.4]
        if tingkat_aktivitas not in [0, 1, 2]:
            messagebox.showerror("Error", "Silakan pilih tingkat aktivitas.")
            return

        total_kalori = bmr * faktor_aktivitas[tingkat_aktivitas]
        messagebox.showinfo("Hasil Kalori", f"Kebutuhan kalori harian Anda: {total_kalori:.2f} kalori")

    except:
        messagebox.showerror("Error", "Masukkan data dengan benar!")

root = tb.Window(themename="superhero")
root.title("Penghitung Kalori Harian")
root.geometry("400x320")

tb.Label(root, text="Umur (tahun)").pack(pady=4)
input_umur = tb.Entry(root)
input_umur.pack()

tb.Label(root, text="Berat (kg)").pack(pady=4)
input_berat = tb.Entry(root)
input_berat.pack()

tb.Label(root, text="Tinggi (cm)").pack(pady=4)
input_tinggi = tb.Entry(root)
input_tinggi.pack()

tb.Label(root, text="Jenis Kelamin").pack(pady=4)
dropdown_kelamin = tb.Combobox(root, values=["Pria", "Wanita"], state="readonly")
dropdown_kelamin.pack()

tb.Label(root, text="Tingkat Aktivitas").pack(pady=4)
dropdown_aktivitas = tb.Combobox(root, values=[
    "Tidak Aktif",
    "Jarang Aktif",
    "Sering Aktif"
], state="readonly")
dropdown_aktivitas.pack()

tb.Button(root, text="Hitung Kalori", bootstyle="success", command=hitung_kalori).pack(pady=5)

root.mainloop()
