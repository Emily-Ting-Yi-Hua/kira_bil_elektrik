guna_elektrik=float(input("Masukkan penggunaan elektrik(kWj):"))
kadartarif1=0.128
kadartarif2=0.334
kadartarif3=0.516
kadartarif4=0.546
unitgunaelektrik1=200
unitgunaelektrik2=100
unitgunaelektrik3=300
unitgunaelektrik4=300
if guna_elektrik<=200:
    bilelektrik1=kadartarif1*unitgunaelektrik1
    print("Jumlah bil elektrik setiap bulan ialah RM",bilelektrik1)
elif guna_elektrik <=300:
    bilelektrik2=kadartarif2*unitgunaelektrik2
    print("Jumlah bil elektrik setiap bulan ialah RM",bilelektrik2)
elif guna_elektrik <=600:
    bilelektrik3=kadartarif3*unitgunaelektrik3
    print("Jumlah bil elektrik setiap bulan ialah RM",bilelektrik3)
else:
    bilelektrik4=kadartarif4*unitgunaelektrik4
    print("Jumlah bil elektrik setiap bulan ialah RM",bilelektrik4)
