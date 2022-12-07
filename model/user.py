class User:
    def __init__(self,name,ak,sk):
        self.name = name
        self.ak=ak
        self.sk=sk

class UserList:
    def __init__(self,userId):
        self.users = [
            User("扎小辫","B7PkFGeOR0etNjrVejh5GiF8QT906MV7","vc4G9SyoBo3IVmNX144Nc3OGbz4EL7rC"),
            User("万美元","DPNDXVlFHgUoafxC6nl4HZEXqtxtd2XC","mGqDXghCGcOOF71uPio046DsrlIFoKA7"),
            User("通话费","idsEGvv8C29hUTRuxYRPQeNEXGSza93C","phiTHCfkMXdWGTerbIzkRhO99cw9aCyU"),
            User("二号","SYlEDCflVXIZuyFnvmydNGyvUcZ7Gkgk","dmR52NQNaUIpQ7DZTGyRivIlnSqHCgGK"),
            User("三号","dlZSAEzRSl2Chw2NGMvlZ9AxNIkXbbuU","OM9ZFYi1SeEDu206lCZLqZ3FcdzLEdv5"),
            User("四号","GckrS7Usicn4I6bITf1YMFAoro6Z9vYf","ToWIrnIi1ZGWRIgb5i7l1GA66peNFP3L"),
            User("Test","2wKG2kUNziWzyzZ1abUXApXjR1r3xM0Q","icXKs5nrBsfRfd8aCvzPsZvm1XkRQ3G3")
            ]
        self.currentUser = self.users[userId if userId < len(self.users) else 0]
    
    def printCurrentUserInfo(self):
        print("当前用户为：" + self.currentUser.name)

    # 设置 User
    def setUser(self,userId):
        self.currentUser = self.users[userId if userId < len(self.users) else 0]
        print("已切换当前用户为：{}".format(self.currentUser.name))
    
    # 更换 User
    def updateUser(self):
        userId = self.users.index(self.currentUser) + 1 if self.users.index(self.currentUser)+1 < len(self.users) else 0
        self.currentUser = self.users[userId]
        print("已切换当前用户为：{}".format(self.currentUser.name))
