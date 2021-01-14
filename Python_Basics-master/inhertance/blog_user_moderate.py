class User:
    active_user = 0
    @classmethod
    def display_method(cls):
        return f"şu anda aktif {cls.active_user} user var "
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
        User.active_user +=1

    def fullname(self):
        return "{} {}".format(self.firstname,self.lastname)

class Modarator(User):

    active_moderators = 0

    @classmethod
    def display_methods(cls):
        return f"şu anda aktif {cls.active_moderators} moderator var var "
    def __init__(self,firstname,lastname,company):
        User.__init__(self,firstname,lastname)

        self.company=company
        Modarator.active_moderators +=1
    

u1 = User("Ali","Korkmaz")
m1=Modarator("Yağmur","Korkmaz","Yazılım")


#print(isinstance(u1,User)) if function refers to class of User thats True. else false.
#print(isinstance(u1, Modarator))""
print(m1.fullname())
print(User.display_method())
print(Modarator.display_methods())