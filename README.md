# Email Aniversariantes

>It's an automation to send an email to people of the birthdays in the day, week and month.

## Description

---

Is created a connection in our Oracle database with cx_Oracle and SQLAlchemy, after that
we search for that data we need and return a DataFrame using the packge of pandas.

With the data in hands is created a image with PIL so we can send a email to a group of people 
with thr birthdays of day, week and month.
