####connecting to a database####
import sqlite3 

def get_db_connection(database):
	conn=None
	try:
		conn=sqlite3.connect(database)
	except Exception as e:
		print(e)
	return conn 

########inserting filehash into database########
def insertHashFile(database,hash,status):
	conn=get_db_connection(database)
	conn.execute('INSERT INTO fileHash (hash,status) Values (?,?)',(hash,status))
	conn.commit()
	conn.close()

#check if filehash exist in database and return status
def ifAlreadyFileHash(conn,fileHash):
	cur=conn.cursor()
	cur.execute("SELECT * FROM fileHash")
	rows=cur.fetchall()
	for row in rows:
		if fileHash==row[0] :
			return row[1]
	
	return None

	

	
	



	
