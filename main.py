<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Data Cleaning & Visualization</title>

<style>
*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial,sans-serif;
}

body{
background:linear-gradient(135deg,#4facfe,#00f2fe);
display:flex;
justify-content:center;
align-items:center;
min-height:100vh;
}

.container{
width:90%;
max-width:1000px;
background:white;
padding:30px;
border-radius:15px;
box-shadow:0 10px 25px rgba(0,0,0,0.2);
}

h1{
text-align:center;
color:#0d6efd;
margin-bottom:10px;
}

.subtitle{
text-align:center;
color:#666;
margin-bottom:30px;
}

.upload-box{
border:2px dashed #0d6efd;
padding:30px;
text-align:center;
border-radius:10px;
background:#f8fbff;
}

input[type=file]{
margin:20px;
padding:10px;
}

button{
background:#0d6efd;
color:white;
border:none;
padding:12px 25px;
border-radius:8px;
font-size:16px;
cursor:pointer;
transition:0.3s;
}

button:hover{
background:#084db3;
}

.features{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-top:35px;
}

.card{
background:#f8fbff;
padding:20px;
border-radius:12px;
text-align:center;
box-shadow:0 3px 8px rgba(0,0,0,.1);
transition:0.3s;
}

.card:hover{
transform:translateY(-5px);
}

.card h3{
color:#0d6efd;
margin-bottom:10px;
}

.table-container{
margin-top:30px;
overflow-x:auto;
}

table{
width:100%;
border-collapse:collapse;
}

table th{
background:#0d6efd;
color:white;
padding:12px;
}

table td{
padding:10px;
border:1px solid #ddd;
text-align:center;
}

.download{
margin-top:25px;
text-align:center;
}

.download a{
text-decoration:none;
}

footer{
margin-top:30px;
text-align:center;
color:#777;
}
</style>

</head>

<body>

<div class="container">

<h1>Data Cleaning & Visualization</h1>

<p class="subtitle">
Upload a CSV dataset, clean the data, visualize insights, and download the cleaned dataset.
</p>

<div class="upload-box">

<form action="/upload" method="POST" enctype="multipart/form-data">

<input type="file" name="file" accept=".csv" required>

<br>

<button type="submit">Upload Dataset</button>

</form>

</div>

<div class="features">

<div class="card">
<h3>🧹 Remove Duplicates</h3>
<p>Automatically removes duplicate records.</p>
</div>

<div class="card">
<h3>📊 Fill Missing Values</h3>
<p>Handles missing values using mean and mode.</p>
</div>

<div class="card">
<h3>📈 Visualization</h3>
<p>Generate charts from cleaned data.</p>
</div>

<div class="card">
<h3>⬇ Download</h3>
<p>Download the cleaned CSV dataset.</p>
</div>

</div>

<div class="table-container">
{{ table|safe }}
</div>

<div class="download">
{% if chart %}
<img src="/chart" width="600">

<br><br>

<a href="/download">
<button>Download Cleaned CSV</button>
</a>
{% endif %}
</div>

<footer>
© 2026 Data Cleaning & Visualization Project
</footer>

</div>

</body>
</html>