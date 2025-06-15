def main():
    # while
    # satat kita tau syarat tapi masih ragu dengan jalan menuju syaratnya
    # sifat utamanya
    # check terlebih dahulu baru di jalankan
    index = 10001
    print("=======while=======")
    while index <= 1000:
        print(f"{index}. Sorry Beb !!!!!!")
        index += 1
    # do while
    # sifat di kerjakan dulu baru di check
    # tidak ada di python tapi ada di java,javascript,atau keluarga C,C++dan,C#
    print("======for=====")
    # for
    # for di pakai saat kamu tau syarat dan cara menujunya
    for value in range(1,10+1):
        print(f"Index of {value}")
        
    makanan = ['daging', 'ayam', 'sayur', 'semangka', 'Melon']
    for value in makanan:
        print(f"{value}")
        
        
#format dasar untuk memberitahukan kalau program yang di jalankan pertama kali    
if __name__ == "__main__": 
    main()