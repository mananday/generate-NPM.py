
print('Program generate NPM')
print('-----------------------')
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

    
