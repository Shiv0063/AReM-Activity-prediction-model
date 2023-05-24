# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
from sklearn.model_selection import GridSearchCV
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            time=float(request.form['time'])
            avg_rss12=float(request.form['avg_rss12'])
            var_rss12=float(request.form['var_rss12'])
            avg_rss13=float(request.form['avg_rss13'])
            var_rss13=float(request.form['var_rss13'])
            avg_rss23=float(request.form['avg_rss23'])
            var_rss23=float(request.form['var_rss23'])
            filename = 'ARem_gcv.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[time,avg_rss12, var_rss12, avg_rss13, var_rss13, avg_rss23, var_rss23]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=prediction)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run() # running the app