from .. import ma

class AddressSchema(ma.Schema):
    class Meta:
        fields = ('addressid', 'userid', 'typeofaddress', 'address_desc','createddate','updateddate','remarks')

address_schema = AddressSchema()
address_schema = AddressSchema(many=True)
