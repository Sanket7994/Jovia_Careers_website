from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOB_list = [{
  'ID': 1,
  'Position': 'Data Analyst',
  'Location': 'Delhi, India',
  'Salary': 'Rs.10,00,000'
}, {
  'ID': 1,
  'Position': 'Data Scientist',
  'Location': 'Gurgao, India',
  'Salary': 'Rs.15,00,000'
}, {
  'ID': 1,
  'Position': 'Data Engineer',
  'Location': 'Gurgao, India'
}, {
  'ID': 1,
  'Position': 'BI-Developer',
  'Location': 'Remote',
  'Salary': 'Rs.8,00,000'
}]


@app.route("/")
def helloWorld():
  return render_template("home.html", jobs=JOB_list, company_name='Jovian')


@app.route("/api/jobs")
def job_listing():
  return jsonify(JOB_list)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
