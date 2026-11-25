from model.connectiondb import mydb

mycursor = mydb.cursor()

class Transaksi:
    def __init__(self):
        self

    def select_data_trxbeli(self):
        try:
            sql = """
                SELECT t.id_transaksi,
                       t.tanggal,
                       p.supplier,
                       p.no_faktur,
                       p.metode_pembayaran,
                       p.status_pembayaran
                FROM trx t
                JOIN trx_pembelian p
                ON t.id_transaksi = p.id_transaksi
                WHERE t.jenis = 'pembelian'
            """
            mycursor.execute(sql)
            return mycursor.fetchall()
        except Exception as e:
            print(e)

    def select_data_trxjual(self):
        try:
            sql = """
                SELECT t.id_transaksi,
                       t.tanggal,
                       p.pelanggan,
                       p.diskon,
                       p.metode_pembayaran,
                       p.bayar,
                       p.kembalian
                FROM trx t
                JOIN trx_penjualan p
                ON t.id_transaksi = p.id_transaksi
                WHERE t.jenis = 'penjualan'
            """
            mycursor.execute(sql)
            return mycursor.fetchall()
        except Exception as e:
            print(e)

    def insert_data(self, tanggal, jenis):
        try:
            sql = "INSERT INTO trx (tanggal, jenis) VALUES (%s, %s)"
            val = (tanggal, jenis)
            mycursor.execute(sql, val)
            mydb.commit()
            return mycursor.lastrowid
        except Exception as e:
            print(e)

class DetailTransaksi:
    def __init__(self):
        self

    def insert_data(self, id_trx, id_barang, qty, harga, subtotal):
        try:
            sql = """INSERT INTO detail_trx
                        (id_transaksi, id_barang, qty, harga, subtotal)
                        VALUES (%s, %s, %s, %s, %s)"""
            val = (id_trx, id_barang, qty, harga, subtotal)
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print(e)

class TransaksiPembelian(Transaksi):
    def __init__(self):
        super().__init__()

    def insert_data(self, id_trx, supplier, no_faktur, metode, tempo, status):
        try:
            sql = """INSERT INTO trx_pembelian
                        (id_transaksi,
                        supplier,
                        no_faktur,
                        metode_pembayaran,
                        jatuh_tempo,
                        status_pembayaran)
                        VALUES (%s, %s, %s, %s, %s, %s)"""
            val = (id_trx, supplier, no_faktur, metode, tempo, status)
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print(e)

class TransaksiPenjualan(Transaksi):
    def __init__(self):
        super().__init__()

    def insert_data(self, id_trx, pelanggan, diskon, metode, bayar, kembalian):
        try:
            sql = """INSERT INTO trx_penjualan
                        (id_transaksi,
                        pelanggan,
                        diskon,
                        metode_pembayaran,
                        bayar,
                        kembalian)
                        VALUES (%s, %s, %s, %s, %s, %s)"""
            val = (id_trx, pelanggan, diskon, metode, bayar, kembalian)
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print(e)
