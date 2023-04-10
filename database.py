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
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      dict_row = row._asdict()
      jobs.append(dict_row)
    return jobs
