from flask import Flask,render_template,request
import sqlite3
app =Flask(__name__)
@app.route('/')
def home():
    return render_template("firstpage.html")

@app.route('/first',methods = ["POST"])
def first():
    name=(request.form.get('name'))
    address=(request.form.get('address'))
    mobile=(request.form.get('mobile'))
    alternate=(request.form.get('alternate'))
    ip=(request.remote_addr)
    #Databese connection
    Conn= sqlite3.connect('mocktest.db')
    c=Conn.cursor()
    
       
    candidate = c.execute("INSERT INTO Candidates(Name,Address,Mobile,Alternate,IP) VALUES('"+name+"','"+address+"','"+mobile+"','"+alternate+"','"+ip+"')")
    
    Conn.commit()
    Conn.close()
    return render_template('index.html')
    
    
@app.route('/get-questions')
def getQuestions():
    conn = sqlite3.connect('mocktest.db')
    c= conn.cursor()
    data = c.execute("SELECT QuestionId, QuestionText, A, B, C, D FROM Questions WHERE IsActive = 1").fetchall()
    conn.commit()
    conn.close()
    return data

@app.route('/submit',methods = ['GET','POST'])
def submit1():
    
    mobile=(request.form.get('mobile'))
    # data=[]
    # item={}
    # item.id
    conn = sqlite3.connect('mocktest.db')
    c= conn.cursor()
    dataCount = c.execute('SELECT COUNT(*) FROM Questions WHERE IsActive = 1')
    num_rows = c.fetchone()[0]
    print(num_rows)
    
    for i in range(1,num_rows+1):
        radio = request.form.get(f"{i}")
        print(radio)
        conn = sqlite3.connect('mocktest.db')
        c= conn.cursor()
        
        answers = c.execute("""INSERT INTO Answers  
                            VALUES  ('"""+mobile+"""','"""+radio.split('-')[0]+"""','"""+radio.split('-')[1]+"""')
                        """)
        conn.commit()
        conn.close()
    
    
    
   
    
    
    return render_template("thankyou.html")

app.run(debug =True,port=8000 )
