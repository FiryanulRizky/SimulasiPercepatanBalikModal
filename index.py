import numpy
from prettytable import PrettyTable
def set_title():
    print("SIMULASI JASA FOTOCOPY")

def simulasi():
    a=2420000*30#kertas
    b=284000*30#tinta
    gaji_karyawan = 3400000
    c= a+b+gaji_karyawan
    awal = 1
    batas = 31

    range_kertas = [0,
                    list(range(0, 21)),
                    list(range(22, 32)),
                    list(range(33, 65)),
                    list(range(66, 99))]
    jml_kertas = [list(range(1, 5501)),
                  list(range(5501, 11002)),
                  list(range(11003, 16503)),
                  list(range(16504, 22004)),
                  list(range(22005, 27501))]
    bilrand1 = numpy.random.randint(0, 100)
    list_pendapatan = []
    for i in range(awal, batas):
        for x in range(0, len(jml_kertas)):
            if range_kertas[x]:
                if bilrand1 in range_kertas[x]:
                    var_rand_kertas = numpy.random.choice(jml_kertas[x])
                    newvarrand = var_rand_kertas
                    var_rand_kertas *= 150
        table_output(i, newvarrand, var_rand_kertas,c)
        list_pendapatan.append(var_rand_kertas)

    addition_pendapatan = sum(list_pendapatan)
    print("Pendapatan 1 Bulan:",addition_pendapatan)
    print("Investasi:",c)
    newadd = addition_pendapatan/30
    print("rata - rata keuntungan:",addition_pendapatan/30)
    w = open('./hasil/file_simulasi40.txt','w')
    w.writelines("\nPendapatan:"+str(addition_pendapatan))
    w.writelines("\nInvestasi:"+str(c))
    w.writelines("\nRata - rata Keuntungan:"+str(newadd))
    if addition_pendapatan > c:
        print("Status: Untung")
        w.writelines("\nStatus: Untung" )
    else:
        print("Status: Rugi")
        w.writelines("\nStatus: Rugi" )
    w.close()

def table_output(var1, var2, var3,var4):
    t = PrettyTable(['Hari', 'Jumlah Kertas','Pendapatan','Investasi'])
    t.add_row([var1, var2, var3,var4])
    print(t)

if __name__ == '__main__':
    set_title()
    simulasi()