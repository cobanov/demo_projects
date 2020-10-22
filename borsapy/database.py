import sqlite3
import pandas as pd

DB_PATH = "test.db"


def create_connection():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(""" CREATE TABLE BORSA
                        (ISIM TEXT NOT NULL,
                        FIYAT REAL NOT NULL,
                        ADET INT NOT NULL,
                        ISLEM CHAR(10),
                        TARIH CHAR(10))
                        """)


def insert_value(values):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO BORSA (ISIM, FIYAT, ADET, ISLEM, TARIH) VALUES (?, ?, ?, ?, ?)", values)

    conn.commit()

# # create_connection("test.db")
# insert_value(("NATEN", 40.74, 50, "alis", "09.10.2020"))
# insert_value(("KAREL", 19.07, 10, "alis", "09.10.2020"))
# insert_value(("KAREL", .23, 10, "satis", "12.10.2020"))
# insert_value(("HLGYO", 2.56, 50, "alis", "12.10.2020"))
# insert_value(("ODAS", 3.49, 50, "alis", "12.10.2020"))
# insert_value(("USAK", 2.20, 50, "alis", "12.10.2020"))


def names():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT distinct(ISIM) FROM BORSA")
        unique_names = [i[0] for i in cur.fetchall()]
        # print(unique_names)
    return unique_names


def get_data(unique_names):
    values = dict()
    with sqlite3.connect(DB_PATH) as conn:

        query = "SELECT * FROM BORSA"
        data = pd.read_sql_query(query, conn)
        islem_kodlari = {"alis": -1, "satis": 1}
        data["ISLEM"].replace(islem_kodlari, inplace=True)
        data["TOPLAM"] = data["FIYAT"] * data["ADET"] * data["ISLEM"]

        print(data)

        return data


def overall_table(data):
    getiri = data.groupby(by="ISIM").sum()["TOPLAM"]

    data["ADET"] = data["ADET"] * data["ISLEM"]
    toplam_adet = data.groupby(by="ISIM").sum()["ADET"] * -1

    ortalama = data.groupby(by="ISIM").sum(
    )["TOPLAM"] / data.groupby(by="ISIM").sum()["ADET"]

    overall_df = pd.DataFrame(
        pd.concat([toplam_adet, ortalama, getiri], axis=1))
    overall_df.columns = ["Toplam Adet", "Ortalama", "Getiri"]
    return overall_df


def write_to_sql(dataframe):
    with sqlite3.connect(DB_PATH) as conn:
        dataframe.to_sql("asd", con=conn)


def main():
    unique_names = names()
    data = get_data(unique_names)
    overall_df = overall_table(data)
    write_to_sql(overall_df)


main()
