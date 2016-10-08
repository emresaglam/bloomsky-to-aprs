# What is this?

This little script grabs environment data from [BloomSky](https://www.bloomsky.com/) weather systems and creates a json file to be read by [pymultimonaprs](https://github.com/asdil12/pymultimonaprs) project.

# Configuration

You need to create a config.json file. An example is provided [here](../master/config.json.example)

Also the script supports two switches:

--config : config.json location (The default is config.json in the same directory as the script)

--output : Where to spit out the pymultimonaprs weather.json file. (The default is the same directory as the script)

# Example

python ./getWeather.py --config /etc/bloomsky.config --output /tmp/weather.json

# See Also

- [pymultimonaprs](https://github.com/asdil12/pymultimonaprs) project. Especially the weather config section in the README.
- [BloomSky API](http://weatherlution.com/bloomsky-api/)
