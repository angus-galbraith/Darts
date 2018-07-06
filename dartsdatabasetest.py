import dartsdb

conn = dartsdb.connect()

cursor = conn.cursor()
playername = "Angus"
playerscore = 150

#cursor.execute("INSERT INTO rtb_highscores (name, score) VALUES ( 'Caitlin', 20)")
query = ("INSERT INTO rtb_highscores" "(name, score)" "VALUES ( %s, %s)")
values = (playername, playerscore)
cursor.execute(query, values)
conn.commit()


cursor.execute("SELECT name, score FROM rtb_highscores ORDER BY score DESC")
nameList = []
scoreList = []
highscoreList = [nameList, scoreList]
full_list = []
while True:
    row =cursor.fetchone()
    if row is None:
        print("Row is None")
        break
    print("Name: %s, Score: %s" % (row[0], row[1]))
    name = row[0]
    score = row[1]
    full_list.append(row[0])
    full_list.append(row[1])
    full_list.append( '/n' )
    #nameList.append(name)
    #scoreList.append(score)
    
print("Number of rows returned: %d" % cursor.rowcount)
print(full_list)
print(highscoreList[0], [1])

cursor.close()
