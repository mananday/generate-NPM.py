'''
(BACA)
halo saia chandra yallo :v,kalo ngoni mau bljar btul2 soal ini,ta kse tau dpe pnjelasan
ato dpe cara kta bkin ini no 2,sebelum itu pstikan ngo lia dpe soal la tra bingung...

sbenarnya no 2 ini tra rumit,yang rumit itu di bagian tong tentukan "YY" dimana YY itu 
untuk tahun lahir,sedangkan yang tong dpa minta input itu umur,jadi tong tentukan tahun
lahirnya pake rumus,lia da di baris 63-67...selain itu yang rumit tu pas dibagian "XX",
"XX" kan dpa sruh input 2 digit terakhir tahun masuk,misal tong masuk 2020,tong musti
bking sampe dpe output tu cuman 2 digit terakhir saja,angka 20 yang terakhir.
jadi pake rumus lagi...lia di baris 58-60...cuman itu saja sih yang bikin susah,brang
makan wktu buat bpikir...dpe sisa tu sama suda dg pa pe materi,if elif bla bla bla,sekian
....
JANG LUPA GANTI DPE DEKLARASI VARIABEL LA PAK TRA KNTARA,MISAL GANTI "JK" DG "Jenis_K"
ATAU "jenis_kelamin","nama" jadi "N" dan sebagainya


btw ini bukan versi yang pastinya sih,msih kurang,ta msih mo bking ulang ato tambah
besok,jadi untuk ngoni tes2 improv da,bereksperimen,gnti sytax ka,dll



'''
print('Program generate NPM')
nama=str(input('Silahkan masukkan nama anda : '))
JK=str(input('Jenis kelamin anda(L/P) : '))
umur=int(input('Umur anda : '))
TM=int(input('Tahun masuk anda : '))
DA=str(input('Daerah asal anda(DIB,DIT,DITA) : '))
F=str(input('Fakultas anda(FE,FH,FKIP,FSB,FP,FAPET,FT,FK) : '))

if(F=='FE'):
    VV="01"
elif(F=='FH'):
    VV='02'
elif(F=='FKIP'):
    VV='03'
elif(F=='FSB'):
    VV='04'
elif(F=='FP'):
    VV='05'
elif(F=='FAPET'):
    VV='06'    
elif(F=='FT'):
    VV='07'
elif(F=='FK'):
    VV='08'

    
if(DA=='DIB'):
    WW='25'
elif(DA=='DIT'):
    WW='35'
elif(DA=='DITA'):
    WW='45'

    
tahun_masuk=TM-2000
if(tahun_masuk<=2000):
    XX=tahun_masuk
    

tahun_lahir=2021-umur
if(tahun_lahir%2==0):
    YY='00'
elif(tahun_lahir%2!=0):
    YY='01'



if(JK=='L'):
    ZZZ='001'
elif(JK=='P'):
    ZZZ='002'

    
print('Proses selesai')
print(nama,'NPM anda adalah : ')
print(VV,WW,XX,YY,ZZZ)

    
