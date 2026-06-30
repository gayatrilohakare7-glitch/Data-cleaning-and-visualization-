from flask import Flask, request, render_template_string, send_file
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Data Cleaning & Visualization</title>
<style>
body{
font-family:Arial;
background:#f4f4f4;
padding:30px;
}
.container{
background:white;
padding:30px;
border-radius:10px;
max-width:900px;
margin:auto;
box-shadow:0 0 10px gray;
}
h1{
text-align:center;
color:#0d6efd;
}
input{
padding:10px;
margin:15px 0;
}
button{
padding:10px 20px;
background:#0d6efd;
color:white;
border:none;
border-radius:5px;
cursor:pointer;
}
table{
border-collapse:collapse;
width:100%;
margin-top:20px;
}
table,th,td{
border:1px solid black;
padding:8px;
}
img{
margin-top:20px;
width:100%;
}
</style>
</head>

<body>

<div class="container">

<h1>Data Cleaning & Visualization</h1>

<form action="/upload" method="POST" enctype="multipart/form-data">

<input type="file" name="file" required>

<button type="submit">Upload</button>

</form>

{{table|safe}}

{% if chart %}
<h2>Visualization</h2>

<img src="/chart">

<br><br>

<a href="/download">
<button>Download Cleaned CSV</button>
</a>

{% endif %}

</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/upload", methods=["POST"])
def upload():

    file=request.files["file"]

    filepath=os.path.join(UPLOAD_FOLDER,file.filename)

    file.save(filepath)

    df=pd.read_csv(filepath)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing values
    for col in df.columns:
        if df[col].dtype=="object":
            df[col].fillna(df[col].mode()[0], inplace=True)
        else:
            df[col].fillna(df[col].mean(), inplace=True)

    cleaned=os.path.join(OUTPUT_FOLDER,"cleaned.csv")

    df.to_csv(cleaned,index=False)

    # Visualization
    numeric=df.select_dtypes(include="number")

    if len(numeric.columns)>=2:

        plt.figure(figsize=(6,4))

        plt.bar(numeric.iloc[:,0],numeric.iloc[:,1])

        plt.title("Bar Chart")

        plt.xlabel(numeric.columns[0])

        plt.ylabel(numeric.columns[1])

        plt.tight_layout()

        plt.savefig(os.path.join(OUTPUT_FOLDER,"chart.png"))

        plt.close()

    table=df.head(10).to_html(index=False)

    return render_template_string(HTML,table=table,chart=True)

@app.route("/chart")
def chart():
    return send_file(os.path.join(OUTPUT_FOLDER,"chart.png"),mimetype="image/png")

@app.route("/download")
def download():
    return send_file(os.path.join(OUTPUT_FOLDER,"cleaned.csv"),as_attachment=True)

if __name__=="__main__":
    app.run(debug=True)