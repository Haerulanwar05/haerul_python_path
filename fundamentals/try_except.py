'''
try dan except merupakan sebuah syntax dimana dalam try itu sendiri merupakan sebuah input dalam kondisi yang terpenuhi apabila kita mengetahui error dalam inputan tersebut kita akan memperingati nya dengan except.
tidak hanya itu terdapat beberapa syntax dalam try dan except yaitu else dan finally, else dalam hal ini merupakan sebuah syntax dimana apabila inputan dalam try atau try terpenuhi maka akan melanjutkan ke else sebagaimana isi dari program dalam inputan tersebut dan apabila try tidak terpenuhi maka akan menuju ke except dan tidak melanjutkan else nya, finally  itu sendiri merupakan sebuah syntax akhir dimana ia tidak memperdulikan mana yang salah dan benar dan hanya menjalankan apa yang di perintahkan saja.
contoh nya seperti dibawah ini:
'''
try:
    print("Selamat datang dipengecekan Umur!")
    umur = int(input("Masukan Umur Anda: ")) # inputan ini kita meminta user menginput sebuah data int
except:
    print("yang anda masukan bukan sebuah angka!") # ini merupakan antisipasi apabila user mengisi data selain int

# setelah kita membuat try and except selanjutnya kita masuk dalam tahap program dari input ini

else:
    if umur > 20:
        print("Anda boleh Masuk!")
    else:                                                  # ini merupakan sebuah program yang dibentuk bedasarkan sebuah input dari user
        print("Maaf Anda masih dibawah umur!")
finally:
    print("Terimakasih sudah mengecek umur anda!")         # finally ini merupakan sebuah program yang dibilang independen karena tidak terkait 