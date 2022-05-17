import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Josh Gabriel\PycharmProjects\pythonProject\5.17.22 Database\Database2.accdb')
    print("Connected to a Database")

    Fullname = "Josh Gabriel E. Sese"
    Assignment = 90
    Laboratory = 995
    Quiz = 90
    Exam = 94
    user_id = 10

    record = connect.cursor()
    record.execute('UPDATE Table1 SET Fullname = ?, Assignment = ?, Laboratory = ?, Quiz = ?, Exam = ? WHERE id = ?', (Fullname, Assignment, Laboratory, Quiz, Exam, user_id))
    record.commit()
    print("Data is updated")

except pyodbc.Error as e:
    print("Error in Connection")