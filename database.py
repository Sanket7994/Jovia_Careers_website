import os
from sqlalchemy import create_engine, text

db_string = os.environ["DB_CONNECTION_STRING"]

engine = create_engine(db_string,
                       echo=True,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result.all():
      dict_row = row._asdict()
      jobs.append(dict_row)
    return jobs


def load_job_from_db_via_ID(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),
                          {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
