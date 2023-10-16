from flask import Flask, render_template, jsonify,Response
import time
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np
import pandas as pd
import csv

app = Flask(__name__)

var1_values = []
var2_values = []
timestamps = []

@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/api/variables")
def get_variables():
    global var1_values, var2_values, timestamps
    var1 = len(var1_values) + 1
    var2 = len(var2_values) + 5
    var1_values.append(var1)
    var2_values.append(var2)

    if len(timestamps) == 0 or len(timestamps) % 5 == 0:
        timestamps.append(time.strftime("%H:%M:%S"))
    else:
        timestamps.append("")

    return jsonify(var1=var1, var2=var2, timestamps=timestamps)

@app.route("/api/plot1")
def plot():
    plt.figure(figsize=(8, 4))
    plt.plot(timestamps, values1, label='Variable 1')
    plt.plot(timestamps, values2, label='Variable 2')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    
    # Convert the plot to an image and serve it
    img_stream = BytesIO()
    plt.savefig(img_stream, format='png')
    img_stream.seek(0)
    return Response(img_stream.read(), content_type='image/png')



@app.route("/api/plot")
def plot_average():
    input_file_path = 'C:/Users/sreel/OneDrive/Desktop/SREE/var2/dummy1.csv'
    output_csv_file_path = 'C:/Users/sreel/OneDrive/Desktop/SREE/var2/Average.csv'

    file1 = pd.read_csv(input_file_path)

    average = []
    for i in range(0, len(file1), 60):
        data_to_average = file1.iloc[i:i + 60, 2]
        avg = data_to_average.mean()
        average.append(avg)

    data_dict_list = [{'average': avg} for avg in average]

    with open(output_csv_file_path, 'w', newline='') as csv_file:
        fieldnames = ['average']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_dict_list)

    file2 = pd.read_csv(output_csv_file_path)

    x = []
    for j in range(0, len(file1), 60):
        temp = file1.iloc[j, 1]
        x.append(temp)

    plt.plot(x, file2['average'], label='Average Line', color='g')
    plt.title('Average Data Plot')
    plt.xlabel('Time')
    plt.ylabel('Average')
    plt.legend()
   
    img_stream = BytesIO()
    plt.savefig(img_stream, format='png')
    img_stream.seek(0)
    return Response(img_stream.read(), content_type='image/png')

   
app.run()
