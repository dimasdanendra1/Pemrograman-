from db import DBConnection as mydb


class Apkresto:
    def __init__(self):
        self.__nama = None
        self.__nohp = None
        self.__makanan = None
        self.__minuman = None
        self.__alamat = None
        self.__ongkir = None
        self.__total = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def nohp(self):
        return self.__nohp

    @nohp.setter
    def nohp(self, value):
        self.__nohp = value

    @property
    def makanan(self):
        return self.__makanan

    @makanan.setter
    def makanan(self, value):
        self.__makanan = value

    @property
    def minuman(self):
        return self.__minuman

    @minuman.setter
    def minuman(self, value):
        self.__minuman = value

    @property
    def alamat(self):
        return self.__alamat

    @alamat.setter
    def alamat(self, value):
        self.__alamat = value

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value

    @property
    def ongkir(self):
        return self.__ongkir

    @ongkir.setter
    def ongkir(self, value):
        self.__ongkir = value

    def simpan(self, total, ongkir):
        self.conn = mydb()
        val = (self.__nama, self.__nohp, self.__alamat, ongkir,
               self.__makanan, self.__minuman, total)
        print(val)
        sql = "INSERT INTO orderan (nama, no_hp, alamat, ongkir, makanan, minuman, total) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nama, self.__nohp, self.__makanan, self.__Harga_makanan, self.__minuman,
               self.__Harga_Minuman, self.__alamat, self.__Harga_Ongkirself.__Total_Harga, id)
        sql = "UPDATE orderan SET Nama pemesan = %s,Nomor telpon = %s,Makanan = %s,Harga makanan = %s,Minuman = %s,Harga Minuman = %s,Alamat Pengiriman = %s,Harga Ongkir = %sTotal Harga = %s WHERE =%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM orderan WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM orderan WHERE id ='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nama = self.result[0]
        self.__nohp = self.result[1]
        self.__makanan = self.result[2]
        self.__Harga_makanan = self.result[3]
        self.__minuman = self.result[4]
        self.__Harga_Minuman = self.result[5]
        self.__alamat = self.result[6]
        self.__Harga_Ongkir = self.result[7]
        self.__Total_Harga = self.result[8]
        self.conn.disconnect
        return self.result

    def getBy(self, ):
        a = str()
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM orderan WHERE ='" + b + "'"
        self.result = self.conn.findOne(sql)
        if (self.result != None):
            self.__nama = self.result[1]
            self.__nohp = self.result[2]
            self.__alamat = self.result[3]
            self.__ongkir = self.result[4]
            self.__makanan = self.result[5]
            self.__minuman = self.result[6]
            self.__total = self.result[7]

            self.affected = self.conn.cursor.rowcount
        else:
            self.__nama = ''
            self.__nohp = ''
            self.__alamat = ''
            self.__ongkir = ''
            self.__makanan = ''
            self.__minuman = ''
            self.__total = ''

            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM orderan"
        self.result = self.conn.findAll(sql)
        return self.result
