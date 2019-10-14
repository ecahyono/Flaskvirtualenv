from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello_world():
    
    orang = {'nama': 'mia', 'umur':'21thn' , 'status':'pelajar'}

    return render_template('index.html', title='Beranda', orang=orang)
    
if __name__ =="__main__":
    app.run(debug=True)



 


