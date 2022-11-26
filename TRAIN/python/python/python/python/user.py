'''
{
    name
    age
    contactNo
    emailid
}
'''


class user:
    def __init__(self, name, age):
        #, contactNo='', emailId=''
        self.name = name
        self.age = age
        # self.contactNo = contactNo
        # self.emailId = emailId

    @classmethod
    def isNameValid(cls, name):
        name = name.split()
        if len(name) > 3 or len(name) == 0:
            return False
        for n in name:
            if not n.isalpha():
                return False
        return True

    @classmethod
    def isAgeValid(cls,age):
        if age < 3 and age> 150:
            return False
        return True

    # @classmethod
    # def isContactNumValid(cls,num):
    #     if num == '' or (len(num) == 10 and num[0] != '0'):
    #         return True
    #     return False
    #
    # @classmethod
    # def isEmailIdValid(cls,emailId):
    #     if emailId.count('@') > 1:
    #         return False
    #     emailId = emailId.split('@')
    #     if emailId[2].count('.') != 1:
    #         return False
    #     emailId = [x.split('.') for x in emailId]
    #     if all(all(lambda x: x.isalnum(),t) for t in emailId):
    #         return True
    #     return False


