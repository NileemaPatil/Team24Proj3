from .. import ma
from marshmallow import fields, post_load
from ..models.user_model import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        # Specify fields to be included in the serialization
        fields = ('id', 'name', 'email', 'language', 'registered_on', 'role')
        load_instance = True  # Optional: if you want deserialization to create User instances

    # Explicitly declare the password field to only load it when deserializing,
    # and to exclude it from all serializations (dumping)
    password = ma.String(load_only=True, required=True)

    # Optional: If you're creating user instances upon loading data, customize further here
    @post_load
    def hash_password(self, data, **kwargs):
        if 'password' in data:
            data['password'] = ma.bcrypt.generate_password_hash(data['password']).decode('utf-8')
        return data

user_schema = UserSchema()
users_schema = UserSchema(many=True)
