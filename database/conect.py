import sqlalchemy
import pandas
from secret import secret_keys

ENGINE = sqlalchemy.create_engine(f"oracle+cx_oracle://{secret_keys.DATABASE_USER}:{secret_keys.DATABASE_PASSWORD}@"
                                  f"{secret_keys.DATABASE_HOST}/?service_name={secret_keys.DATABASE}",
                                  arraysize=1000)


def consults_manager(sql) -> pandas.DataFrame:

    return pandas.read_sql(sql, ENGINE)
