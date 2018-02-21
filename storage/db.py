import sqlite3

DB_PATH = "storage/moustache.sqlite"

GET_TAP = "SELECT * FROM tapliters WHERE tapId = {0}"
UPDATE_TAP_LITERS = """UPDATE "TapLiters" SET literAmount = {0}  WHERE tapId={1}"""
UPDATE_TAP_LABEL = "UPDATE tapliters SET tapName = {0} WHERE tapId = {1}"


class Database(object):
	def __init__(self):
		self.connection = sqlite3.connect(DB_PATH)
		self.cursor = self.connection.cursor()
		#self.createTable()

	def getTapInfo(self, tapNumber):
		qry = GET_TAP.format(tapNumber)
		self.cursor.execute(qry)
		results = self.cursor.fetchone()
		liters, label = results[1], results[2]
		return liters, label

	def updateTapLiters(self,tapNumber, liters):
		qry = UPDATE_TAP_LITERS.format(liters, tapNumber)
		self.cursor.execute(qry)
		self.connection.commit()

	def updateTapLabel(self,tapNumber, label):
		qry = UPDATE_TAP_LABEL.format(tapNumber, label)
		self.cursor.execute(qry)
		self.connection.commit()

	def createTable(self):
		qry = 'CREATE TABLE IF NOT EXISTS "TapLiters" ("tapId" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"literAmount" INTEGER,"tapName" TEXT)'
		self.cursor.execute(qry)

		for tapId in range(1,6):
			qry = """INSERT INTO "TapLiters" (tapId, literAmount, tapName) VALUES ({0},0,"-")""".format(tapId)
			self.connection.execute(qry)

		self.connection.commit()

	def __enter__(self):
		return self

	def __exit__(self, ext_type, exc_value, traceback):
		self.cursor.close()
		if isinstance(exc_value, Exception):
			self.connection.rollback()
		else:
			self.connection.commit()
		self.connection.close()
