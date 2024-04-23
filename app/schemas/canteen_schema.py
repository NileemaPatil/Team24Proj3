from .. import ma

class CanteenSchema(ma.Schema):
    class Meta:
        fields = ('canteenid', 'location', 'canteenname', 'canteenowner', 'canteenstatus', 'createddate','updateddate')
