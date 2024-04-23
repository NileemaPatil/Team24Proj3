from .. import ma

class AddressSchema(ma.Schema):
    class Meta:
        fields = ('addressid', 'userid', 'typeofaddress', 'address_desc','createddate','updateddate')

address_schema = AddressSchema()
addresss_schema = AddressSchema(many=True)
