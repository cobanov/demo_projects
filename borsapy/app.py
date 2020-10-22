from flask import Flask, render_template, request
import sqlite3

DATABASE = "test.db"

app = Flask(__name__)


@app.route('/')
def table():
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("select * from BORSA")
        rows = cur.fetchall()

    return render_template("main.html", rows=rows)


@app.route('/add')
def add():
    return render_template("add.html")


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            isim = request.form["isim"]
            fiyat = request.form["fiyat"]
            adet = request.form["adet"]
            islem = request.form["islem"]
            tarih = request.form["tarih"]

            with sqlite3.connect("test.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into BORSA (isim, fiyat, adet, islem, tarih) values (?, ?, ?, ?, ?)",
                            (isim, fiyat, adet, islem, tarih))
                con.commit()
                msg = (isim, fiyat, adet, islem, tarih)

        except:
            con.rollback()
            msg = "We can not add the employee to the list"
        finally:
            return render_template("success.html", msg=msg)
            con.close()


if __name__ == '__main__':
    app.run(debug=True)
