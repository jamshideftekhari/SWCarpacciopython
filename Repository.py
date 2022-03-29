import mysql.connector

class Repository(object):
    DBobject = object
    DBCursor = object
    RowsList = []
    def __init__(self):
        pass

    # can be made by parameter
    def Connect2DB(self):
        self.DBobject = mysql.connector.connect(
                  host = "localhost",
                  user = "jamshid",
                  password = "JAM2003eft",
                  database = "taxDiscount"
                )
        self.DBCursor = self.DBobject.cursor()

    def GetTableElements(self, tableName):
        self.DBCursor.execute("SELECT * FROM %s" %tableName)
        self.RowsList = self.DBCursor.fetchall()
        for row in self.RowsList:
            print(row)

    def InsertDiscount(self, disBase, disValue):
        discount=[(disBase,disValue), (disBase,disValue)]
        self.DBCursor.execute("insert into discountTable (discountBase, discountValue) values (%s,%s)", (disBase, disValue))
        self.DBobject.commit()
         


re=Repository()
re.Connect2DB()
print("************state values***********")
re.GetTableElements("taxtable")
print ("**************discount table**************")
re.GetTableElements("discounttable")
re.InsertDiscount(3000,5)
print ("**************discount table one row added**************")
re.GetTableElements("discounttable")

