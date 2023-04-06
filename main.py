from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id':1,
  'title':"Data Sci",
  'location':'usa',
  'salary': 'rs100'
},
       {
  'id':2,
  'title':"Data Sci",
  'location':'usa',
  'salary': "Rs.10"
},{
  'id':3,
  'title':"Data Sci",
  'location':'usa',
  'salary': "Rs.10"
},{
  'id':4,
  'title':"Data Sci",
  'location':'usa',
  'salary': "Rs.10"
}]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs = JOBS)
@app.route('/api/jobs')
def job_list():
  return jsonify(JOBS)
if __name__ == "__main__":
  app.run('0.0.0.0', debug = True)
  
