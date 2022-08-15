from flask_app.config.mysqlconnection import connectToMySQL


class User:
    db = "2rtfeedback"

    def __init__(self, data):
        self.idfeeback = data['id']
        self.CustEmail = data['CustEmail']
        self.CustId = data['CustId']
        self.CustName = data['CustName']
        self.Invoice = data['Invoice']
        self.Date = data['Date']
        self.SalesRep = data['SalesRep']
        self.Rating = data['Rating']
        self.EmailSent = data['Email_Sent']
        self.compid = data['compid']
        self.SqlRecn = data['SqlRecn']
        self.SalesMn = data['SalesMn']

##################################MYSQL QUERIES####################################################
    @classmethod
    def setinvoice(cls, data):
        query = "query to db"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def getUsers(cls):
        query = "SELECT a.*,b.refinfo,b.MailServer,b.MailPort,b.MailUser,b.MailPass,b.MailTsl,b.MailSsl,b.SqlRecn FROM feedback a, feedset b where a.compid = b.compid and a.EmailSent = 0"
        results = connectToMySQL(cls.db).query_db(query)

        print(results)
        return results

    @classmethod
    def updateFeedback(cls, data):
        query = " Update feedback SET Rating=%(Rating)s WHERE idfeeback = %(idfeeback)s ;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def getOneUser(cls, data):
        query = "SELECT a.*,b.refinfo FROM feedback a, feedset b where a.compid = b.compid and a.idfeeback= %(idfeeback)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results(results[0])

    @classmethod
    def updateEmailSent(cls, data):
        query = "Update feedback SET EmailSent=1 WHERE idfeeback = %(idfeeback)s ;"
        return connectToMySQL(cls.db).query_db(query, data)
# Email_Sent =%(Email_Sent)s
