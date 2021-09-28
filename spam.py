from flask import Flask,render_template,request
import pickle


app = Flask(__name__)



@app.route("/",methods=['GET','POST'])
def func():
    
    with open('NB_model_pickle','rb') as f:
        model = pickle.load(f)

    if request.method == 'POST':

        email = request.form
        check_email = email['email']

        check = model.predict([check_email])

        if check == 1:
            return render_template('email.html',show = "This email is SPAM.")
              
        else:
             return render_template('email.html',show = "This email is not a SPAM.")

    return render_template('email.html')
        
if __name__ == "__main__":
    app.run(debug = True)