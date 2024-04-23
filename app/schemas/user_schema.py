from .. import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('userid', 'username', 'firstname','lastname', 'mobileno','email', 'aadharID','userrole','userStatus', 'password', 'registered_on', 'updatedDate', 'remarks')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
