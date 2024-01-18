from db import DBConnection as mydb

class data_Perawat:

    def __init__(self):
        self.__id=None
        self.__nip=None
        self.__nama=None
        self.__bagian=None
        # self.__kode_prodi=None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def id(self):
        return self.__id

    @property
    def nip(self):
        return self.__nip

    @nip.setter
    def nip(self, value):
        self.__nip = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def bagian(self):
        return self.__bagian

    @bagian.setter
    def bagian(self, value):
        self.__bagian = value

    # @property
    # def kode_prodi(self):
    #     return self.__kode_prodi

    # @kode_prodi.setter
    # def kode_prodi(self, value):
    #     self.__kode_prodi = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nip, self.__nama, self.__bagian)
        sql="INSERT INTO data_perawat (nip, nama, bagian) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nip, self.__nama, self.__bagian, id)
        sql="UPDATE data_perawat SET nip = %s, nama = %s, bagian=%s, WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIP(self, nip):
        self.conn = mydb()
        val = (self.__nama, self.__bagian, self, nip)
        sql="UPDATE data_perawat SET nama = %s, bagian=%s, WHERE nip=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM data_perawat WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteBynip(self, nip):
        self.conn = mydb()
        sql="DELETE FROM data_perawat WHERE nip='" + str(nip) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM data_perawat WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nip = self.result[1]
        self.__nama = self.result[2]
        self.__bagian = self.result[3]
        # self.__kode_prodi = self.result[4]
        self.conn.disconnect
        return self.result

    def getBynip(self, nip):
        a=str(nip)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM data_perawat WHERE nip='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nip = self.result[1]
            self.__nama = self.result[2]
            self.__bagian = self.result[3]
            # self.__kode_prodi = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nip = ''
            self.__nama = ''
            self.__bagian = ''
            # self.__kode_prodi = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM data_perawat"
        self.result = self.conn.findAll(sql)
        return self.result
    

# Tampilkan Data
A = data_Perawat()
B = A.getAllData()
print(B)

# Entry Data
# A data_perawat()
# A.nip "4478"
# A.nama = "Wahid"
# A.bagian ="L"
# A.kode_prodi="IND"
# A.simpan()
# B = A.getAllData()
# print(B)


# update Data
# A = data_perawat()
# nip "4478"
# A.nama = "Wahid Dul Hamid"
# A.bagian ="L"
# A.kode_prodi="TIF"
# A.updateBynip(nip)
# B = A.getAllData()
# print(B)


# #delete Data
# A = data_perawat()
# nip = "4478"

# A.deleteBynip(nip)
# B = A.getAllData()
# print(B)

