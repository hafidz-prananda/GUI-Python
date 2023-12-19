from tkinter import *
from tkinter import ttk

global key

def quicksort(arr):
  if len(arr) <= 1:
    return arr

  pivot = arr[-1]

  lebih_kecil = [x for x in arr[:-1] if key(x) <= key(pivot)]
  lebih_besar = [x for x in arr[:-1] if key(x) > key(pivot)]

  lebih_kecil_sorted = quicksort(lebih_kecil)
  lebih_besar_sorted = quicksort(lebih_besar)

  sorted_data = lebih_kecil_sorted + [pivot] + lebih_besar_sorted

  return sorted_data

def sort_nama():
    global key
    for item in table.get_children():
      table.delete(item)

    key=lambda x: x[0]

    sorted_data = quicksort(data)

    for dt in sorted_data:
      table.insert("", "end", values=dt)

def sort_nip():
    global key

    for item in table.get_children():
      table.delete(item)

    key=lambda x: x[1]

    sorted_data = quicksort(data)

    for dt in sorted_data:
      table.insert("", "end", values=dt)

def sort_tgl():
    global key

    for item in table.get_children():
      table.delete(item)

    key=lambda x: x[2]

    sorted_data = quicksort(data)

    for dt in sorted_data:
      table.insert("", "end", values=dt)

def sort_alamat():
    global key

    for item in table.get_children():
      table.delete(item)

    key=lambda x: x[3]

    sorted_data = quicksort(data)

    for dt in sorted_data:
      table.insert("", "end", values=dt)

def search():
    for item in table.get_children():
      table.delete(item)

    cari = text.get().lower()

    for i in range(len(data)):
      if data[i][0].lower() == cari:
        return table.insert("", "end", values=(data[i]))
      elif data[i][1].lower() == cari:
        return table.insert("", "end", values=(data[i]))
      elif data[i][2].lower() == cari:
        return table.insert("", "end", values=(data[i]))
      elif data[i][3].lower() == cari:
        return table.insert("", "end", values=(data[i]))
    return -1

def dataIn():
  global text1
  for item in table.get_children():
      table.delete(item)
      
  for rec in data:
    table.insert("", "end", values=(rec[0], rec[1], rec[2], rec[3]))
  
  text.delete(0, END)

window = Tk()
window.title("Aplikasi Sorting Pegawai")
window.geometry("450x300")
window.resizable(False, False)
frame = Frame(window).pack()

data = [('Budi Santoso', '012345678', '1990-01-01', 'Jl. Contoh No. 123'),
        ('Dewi Indah', '987654310', '1985-05-15', 'Jl. Uji Coba No. 456'),
        ('Citra Putri', '111223345', '1992-08-20', 'Jl. Percobaan No. 789'),
        ('Agus Wijaya', '555667789', '1988-03-10', 'Jl. Test No. 1011'),
        ('Rina Setiawan', '222333445', '1995-11-25', 'Jl. Dummy No. 1213'),
        ('Putra Pratama', '777888899', '1998-04-30', 'Jl. Sample No. 1415'),
        ('Sari Wulandari', '123789457', '1986-07-12', 'Jl. Example No. 1617'),
        ('Adi Nugroho', '987654210', '1994-02-05', 'Jl. Illustration No. 1819'),
        ('Dian Cahyani', '555666788', '1993-09-15', 'Jl. Model No. 2021'),
        ('Ani Rahayu', '333444566', '1991-06-28', 'Jl. Prototype No. 2223'),
        ('Faisal Rahman', '888999900', '1987-12-03', 'Jl. Draft No. 2425'),
        ('Linda Susanto', '444555677', '1996-10-18', 'Jl. Template No. 2627'),
        ('Dodi Kurniawan', '666777899', '1989-04-22', 'Jl. Blueprint No. 2829'),
        ('Merry Julianti', '555444331', '1997-01-08', 'Jl. Scheme No. 3031'),
        ('Eko Prasetyo', '111222344', '1994-08-14', 'Jl. Framework No. 3233'),
        ('Ratna Widiastuti', '999887765', '1992-03-19', 'Jl. Algorithm No. 3435'),
        ('Andi Firmansyah', '333222210', '1986-05-06', 'Jl. Protocol No. 3637'),
        ('Rina Kusuma', '777666541', '1990-02-11', 'Jl. Design No. 3839'),
        ('Dito Setiawan', '444333210', '1988-09-26', 'Jl. Pattern No. 4041'),
        ('Dini Rahmawati', '222111110', '1995-06-01', 'Jl. Style No. 4243'),
        ('Rizky Wardhana', '666555432', '1993-11-16', 'Jl. Method No. 4445'),
        ('Santi Hidayati', '111000987', '1987-04-30', 'Jl. Syntax No. 4647'),
        ('Anto Pratama', '888777654', '1999-01-15', 'Jl. Code No. 4849'),
        ('Rahmat Hayat', '555444320', '1985-08-20', 'Jl. Function No. 5051'),
        ('Putri Amelia', '999888764', '1996-03-06', 'Jl. Variable No. 5253'),
        ('Yoga Utomo', '333221100', '1991-10-11', 'Jl. Class No. 5455'),
        ('Evi Julianti', '777665543', '1988-05-26', 'Jl. Object No. 5657'),
        ('Iqbal Putra', '444332210', '1994-02-10', 'Jl. Interface No. 5859'),
        ('Ratih Asmara', '222110000', '1992-09-24', 'Jl. Module No. 6061'),
        ('Taufik Rahman', '666555442', '1986-06-09', 'Jl. Package No. 6263'),
        ('Rina Anggraini', '111009987', '1993-01-24', 'Jl. Library No. 6465'),
        ('Anita Kusuma', '888777644', '1990-08-09', 'Jl. Namespace No. 6667'),
        ('Arif Hidayat', '555444311', '1984-11-04', 'Jl. Repository No. 6869'),
        ('Dini Ayu', '999888763', '1996-06-19', 'Jl. Framework No. 7071'),
        ('Galih Wijaya', '333221110', '1991-01-03', 'Jl. Algorithm No. 7273'),
        ('Elsa Rahmawati', '777665544', '1988-08-18', 'Jl. Template No. 7475'),
        ('Adi Prasetyo', '444333220', '1995-03-05', 'Jl. Blueprint No. 7677'),
        ('Ayu Handayani', '222221110', '1993-10-20', 'Jl. Pattern No. 7879'),
        ('Reza Santoso', '666554432', '1987-05-07', 'Jl. Style No. 8081'),
        ('Aulia Turner', '111009986', '1994-12-22', 'Jl. Protocol No. 8283'),
        ('Riska Davis', '888776665', '1992-07-08', 'Jl. Method No. 8485'),
        ('Bobby Hill', '555444330', '1986-02-03', 'Jl. Syntax No. 8687'),
        ('Dewi Bennett', '999888762', '1990-09-18', 'Jl. Code No. 8889'),
        ('Andi Foster', '333221111', '1988-04-03', 'Jl. Function No. 9091'),
        ('Rini Coleman', '777666542', '1995-11-16', 'Jl. Variable No. 9293')]

table = ttk.Treeview(frame)
table["columns"] = ("1", "2", "3", "4")
table.column("#0", width=0, stretch=NO)
table.column("1", anchor=CENTER, width=100)
table.column("2", anchor=CENTER, width=80)
table.column("3", anchor=CENTER, width=80)
table.column("4", anchor=CENTER, width=135)

table.heading("#0", text="", anchor=CENTER)
table.heading(1, text="Nama", anchor=CENTER, command=sort_nama)
table.heading(2, text="NIP", anchor=CENTER, command=sort_nip)
table.heading(3, text="Tanggal Lahir", anchor=CENTER, command=sort_tgl)
table.heading(4, text="Alamat", anchor=CENTER, command=sort_alamat)

for rec in data:
  table.insert("", "end", values=(rec[0], rec[1], rec[2], rec[3]))

label = Label(text="Aplikasi sorting pegawai")
text = Entry(window, width=20)
button1 = Button(window, text="Search", command=search)
button2 = Button(window, text="Refresh", command=dataIn)

table.pack()
text.place(x=160, y=235)
button1.place(x=200, y=260)
button2.place(x=25, y=260)

window.mainloop()