from flask import Flask

app=Flask(__name__)
app.secret_key="success"
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='1234'
app.config['MYSQL_DB']='aerele'


@app.route('/')
def index():
    return '<h1> hello </h1>'

if __name__=='__main__':
    app.run(debug=True)