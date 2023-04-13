from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db_via_ID

app = Flask(__name__)


@app.route("/")
def hello_jovian():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name="Jovian")


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db_via_ID(id)
  if not job:
    return "Not Found", 404
  else:
    return render_template('jobpage.html', job=job, company_name="Jovian")


@app.route("/api/job/<id>")
def show_job_json(id):
  job = load_job_from_db_via_ID(id)
  return jsonify(job)


@app.route("/login")
def login():
  return render_template('login.html')


@app.route("/signup")
def signup():
  return render_template('signup.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
