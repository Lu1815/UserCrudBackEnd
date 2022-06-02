from utils.DateFormat import DateFormat

class User():
    def __init__(self, userId, userName = None, userPwd = None, userCreation = None) -> None:
        self.userId = userId
        self.userName = userName
        self.userPwd = userPwd
        self.userCreation = userCreation

    def to_JSON(self):
        return {
            'userId': self.userId,
            'userName': self.userName,
            'userPwd': self.userPwd,
            'userCreation': DateFormat.convert_date(self.userCreation)
        }