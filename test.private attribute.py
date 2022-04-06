class Product():
 __items = 6 # private

def __init__(self, nama_barang):
    self.nama = nama_barang

def harga_barang(self,harga_barang):
    hasil = self.__items * harga_barang
    return hasil

sepatu = Product("sepatu")
print(sepatu.harga_barang(100))

# Aldeni marga putra,Aldeni
#hasil :
# 600
