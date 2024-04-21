from .. import ma

class WeatherSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'weather_main', 'weather_description','windspeed','temperature', 'humidity', 'location')

weather_schema = WeatherSchema()
weathers_schema = WeatherSchema(many=True)
