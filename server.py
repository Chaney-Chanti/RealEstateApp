from flask import Flask
import pandas as pd
import SourceDataObj

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to my real estate app!'

@app.route('/getZHVI')
def getZipCodeData():
    zillow = SourceDataObj.Zillow()
    print(zillow.data["ZHVI"])
    return 'Zillow Data'

if(__name__ == '__main__'):
    app.run()

#Issues: Slow Data Loading
# Zillow Home Value Index (ZHVI): 
# A measure of the typical home value and market changes across a given region and housing type.
#  It reflects the typical value for homes in the 35th to 65th percentile range.
#  Available as a smoothed, seasonally adjusted measure and as a raw measure.