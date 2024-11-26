from flask import Flask
from flask import request, render_template, redirect, send_file
app = Flask(__name__)

app.config['SECRET_KEY'] = b'1236!$1254dfnjndfgj'


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/dados', methods=['POST'])
def dados():
    if request.method == 'POST':
        data = request.form
        data = data.to_dict()
        print("Dados Recebidos: \n Nome: %s \n Email: %s \n Idade: %s", data['Nome'],data['Email'], data['Idade'])
        return redirect('/')
    
@app.route('/download', methods=['GET', 'POST'])
def download():
    path_download = "./files/teste.xlsx"
    return send_file(path_download,as_attachment=True,download_name='teste.xlsx')


if __name__ =="__main__":
    app.run(debug=True, port=3000)