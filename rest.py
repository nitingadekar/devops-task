import flask
from datetime import datetime
from pytz import reference


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
 now = datetime.now()
 localtime = reference.LocalTimezone()
 tz = localtime.tzname(now)
 vardt = now.strftime("%m/%d/%Y, %H:%M:%S")
 return (tz + "  " + vardt)
app.run(port=8080, debug=True)
