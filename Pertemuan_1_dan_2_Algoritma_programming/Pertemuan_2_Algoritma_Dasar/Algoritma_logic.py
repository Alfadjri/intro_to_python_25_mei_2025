#study kasus
nilai_raport = 100

# if 
# format dasar
# if kondisi :
#    apa yang akan kamu lakukan jika kondisi terpenuhi
# kalau tidak terpenuhi program akan tetap berjalan
print("==========if=========")
nilai_raport = 100
if nilai_raport >= 100:
    print("Selamat kamu lulus dalam test ini !!!")
print("Program akan terus berlanjut")

print("==========if-else=========")
#di gunakan untuk memaksa seseorang untuk mengikut perintah jika gagal
nilai_raport = 50
if nilai_raport >= 100:
    print("Selamat kamu lulus dalam test ini !!!")
else :
    print("Kamu tidak lulus!!!")

print("=========Tenery===========")
nilai_raport = 50
pesan = "Lulus" if nilai_raport >= 100 else "Tidak lulus"
print(f"{pesan}")

print("=========if elif else=========")
nilai_raport = 60
if nilai_raport >= 100:
    print("Selamat kamu lulus dalam test ini !!!")
elif nilai_raport >= 50 and nilai_raport < 100:
    print("Kamu lulus dengan nilai passpasan")
else:
    print("Kamu tidak lulus")

print("======if nesterd(bersarang)=======")
nilai_raport = 60
if nilai_raport >= 100:
    print("Selamat kamu lulus dalam test ini !!!")
elif nilai_raport >= 50 and nilai_raport < 100:
    # tips nya cari syarta yang paling sedikit
    if nilai_raport > 70: #ini di sebut if nesteted bersarang
        print("Kamu lulus")
    else:
        print("Kamu lulus dengan nilai passpasan")
else:
    print("Kamu tidak lulus")
    
    
# switch case
# di pakai saat kamu tau spesifik apa yang akan di lakukan user

print("=============Switch case ============")
print("======Menu=======")
print("1.Start")
print("2.End")
select = input("Select => ")
match select:
    case "1":
        print("Start")
    case "2":
        print("End")
    case _ :
        print("Invalid input type !!!!!!")
