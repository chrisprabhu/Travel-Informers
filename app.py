from flask import Flask, render_template, jsonify, redirect
import pandas as pd

from sqls import city_data
from dfs import timeseries_data, scatter_data, donut_data
import json
import random 
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/crimedata.html")
def crimedata():
    return render_template("crimedata.html")

@app.route("/hotels.html")
def hotels():
    return render_template("hotels.html")

@app.route("/weather.html")
def weather():
    return render_template("weather.html")


@app.route("/map.html")
def map():
    return render_template("map.html")

@app.route("/chart.html")
def chart():
    return render_template("chart.html")

@app.route("/city")
def city():
    data = city_data()
    return jsonify(data)

@app.route("/<city_name>/<month>/<x>/<y>")
def give_them_graphs(city_name, month, x, y):
    traces = []
    traces.append(timeseries_data(city_name, month, x))
    traces.append(scatter_data(city_name, month, x, y))
    traces.append(donut_data(city_name, month, x))
    return jsonify(traces)

'''
@app.route("/scrape")
def scrape():
    # Get the stuff we need to get
    return redirect("//", code=302)

@app.route("/city")
def city():
    # Return weather information for city 

@app.route("/something")
def something():
    # Return something

@app.route("/render")
'''

@app.route("/city_attributes")
def city_attributes():
    df = pd.read_csv("historical-hourly-weather-data/city_attributes.csv", index_col='City')
    print(df.to_dict(orient='records'))
    return jsonify(df.to_dict(orient='records'))

@app.route("/city_pics/<city>")
def get_pic_urls(city):
    """
    queries the pic urls json file and returns a random sampling of them
    
    No guarenttees for trying to get more than 6 pics
    """
    with open('city_pics_urls.json', 'r') as f:
        data = json.loads(f.read())
        city_urls = data[city]
        return jsonify(random.sample(list(city_urls),6))


if __name__ == "__main__":
    app.run(debug=True)