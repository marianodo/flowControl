import sqlite3

DB_PATH = "moustache.db"

GET_TAP = "SELECT * FROM tapliters WHERE tapId = {0}"
UPDATE_TAP_LITERS = "UPDATE tapliters SET literAmount = {0} WHERE tapId = {1}"
UPDATE_TAP_LABEL = "UPDATE tapliters SET tapName = {0} WHERE tapId = {1}"


class Database(object):
	def __init__(self):
		self.connetion = sqlite3.connect(DB_PATH)
		self.cursor = self.connetion.cursor()


	def getTapInfo(self, tapNumber):
		qry = GET_TAP.format(tapNumber)
		self.cursor.execute(qry)
		liters, label = self.cursor.fetchone()
		return liters, label

	def updateTapLiters(self,tapNumber, liters)
		qry = UPDATE_TAP.format(tapNumber, liters)
		self.cursor.execute(qry)
		self.connetion.commit()

	def updateTapLabel(self,tapNumber, label)
		qry = UPDATE_TAP_LABEL.format(tapNumber, label)
		self.cursor.execute(qry)
		self.connetion.commit()
