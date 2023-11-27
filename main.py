import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/manga', methods = ['POST'])
def create_manga():
    try:
        __json = request.json
        __manga_Name = __json['manga_Name']
        __manga_Detail = __json['manga_Detail']
        __manga_Img = __json['manga_Img']
        __student_Fio = __json['student_Fio']
        __student_Score = __json['student_Score']
        if __manga_Name and __manga_Detail and __manga_Img and __student_Fio and __student_Score and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO Manga(manga_Name, manga_Detail, manga_Img, student_Fio, student_Score) VALUES(%s, %s, %s, %s, %s)"
            binData = (__manga_Name, __manga_Detail, __manga_Img, __student_Fio, __student_Score)
            cursor.execute(sqlQuery, binData)
            conn.commit()
            respone = jsonify('Manga added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()

@app.route('/manga')
def get_manga():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM Manga")
        mangaRows = cursor.fetchall()
        response = jsonify(mangaRows)
        response.status_code = 200
        return response
    except Exception as ex:
        print(ex, response.status_code)
    finally:
        cursor.close()
        conn.close()

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

if __name__ == "__main__":
    app.run()