import mysql.connector
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "Python")
print(myconn)
cur = myconn.cursor()
def update_rec():
  sql = ""
  try:
    cursor.execute(sql)
    db.commit()
  except:
    db.rollback()
def insert_rec():
  sql = "INSERT INTO DBS(trans_key,acc_key \
       trans_am,trans_type,trans_origin,trans_date) \
       VALUES ('%s', '%s', '%d', '%s', '%s' )"
  try:
    cursor.execute(sql)
    db.commit()
  except:
    db.rollback()
def delete_rec():
  sql = ""
  try:
    cursor.execute(sql)
    db.commit()
  except:
    db.rollback()
def h1_class():
  h1=[]
  sql ="SELECT count(*) from transaction t, account_info a where t.account_key==a.account_key and a.customer_key==query.customer_key  in  (SELECT  CAST(EXTRACT MONTH FROM [transfer_date] AS MONTH) ,
     account_key,COUNT(transaction_amt) AS counter
FROM transaction where counter>10 and trnasaction_type="INN" or transaction_type="OUT"
GROUP BY CAST([trnasfer_date] AS MONTH),account_key;
"
  try:
    h=cursor.execute(sql)
    h1=list(h)
    db.commit()
  except:
    db.rollback()
def h2_class():
  h2=[]
  sql = "SELECT count(*) from transaction t, account_info a where t.account_key==a.account_key and a.customer_key==query.customer_key  in  (SELECT  CAST(EXTRACT MONTH FROM [transfer_date] AS MONTH) ,
         account_key ,
         COUNT(transaction_amt) AS counter
         FROM     transaction where counter>1000 and transaction_type="INN"
         GROUP BY CAST([transfer_date] AS MONTH) ,account_key;"
  try:
    h=cursor.execute(sql)
    h2=list(h)
    db.commit()
  except:
    db.rollback()
def h3_class():
  h3=[]
  sql = "SELECT count(*) from transaction t, account_info a where t.account_key==a.account_key and a.customer_key==query.customer_key  in  (SELECT  CAST(EXTRACT MONTH FROM [transfer_date] AS MONTH) ,
         account_key ,COUNT(transaction_amt) AS counter
        FROM   transaction where counter>800 and transaction_type="OUT" GROUP BY CAST([transfer_date] AS MONTH) ,
         account_key;"
  try:
    h=cursor.execute(sql)
    h3=list(h)
    db.commit()
  except:
    db.rollback()
def h4_class():
  h4=[]
  sql = "SELECT count(*) from transaction t, account_info a where t.account_key==a.account_key and a.customer_key==query.customer_key  in  (SELECT  CAST([transfer_date] AS DATE) ,
     account_key,COUNT(account_key) AS counter
FROM  transaction where counter>20
GROUP BY CAST([transfer_date] AS DATE),account_key;"
  try:
    h=cursor.execute(sql)
    h4=list(h)
    db.commit()
  except:
    db.rollback()
def h4_class():
  h4=[]
  sql = "SELECT count(*) from transaction t, account_info a where t.account_key==a.account_key and a.customer_key==query.customer_key  in  (SELECT  CAST([transfer_date] AS DATE) ,
     account_key,COUNT(account_key) AS counter
FROM  transaction where counter>20
GROUP BY CAST([transfer_date] AS DATE),account_key;"
  try:
    h=cursor.execute(sql)
    h4=list(h)
    db.commit()
  except:
    db.rollback()
def m2_class():
  m2=[]
  sql = "SELECT count(*) from transaction t, account_info a where t.account_key==a.account_key and a.customer_key==query.customer_key in (SELECT CAST(EXTRACT MONTH FROM [transfer_date] AS MONTH),account_key,
          sum (transaction_amt)AS counter
          FROM  transaction where counter>600 and counter<1000 and transaction_type="INN"
          GROUP BY CAST([transfer_date] AS MONTH),account_key;"
  try:
    m=cursor.execute(sql)
    m2=list(m)
    db.commit()
  except:
    db.rollback()
def m3_class():
  m3=[]
  sql = "SELECT count(*) from transaction t, account_info a where t.account_key==a.account_key and a.customer_key==query.customer_key  in
         (SELECT  CAST(EXTRACT MONTH FROM [transfer_date] AS MONTH) ,
         account_key ,
         sum(transaction_amt) AS counter
         FROM transaction where counter>500 and counter<800 and transaction_type="OUT"
         GROUP BY CAST([transfer_date] AS MONTH) ,
         account_key;"
  try:
    m=cursor.execute(sql)
    m3=list(m)
    db.commit()
  except:
    db.rollback()
def m4_class():
  m4=[]
  sql = "SELECT count(*) from transaction t, account_info a where t.account_key==a.account_key and a.customer_key==query.customer_key  in  (SELECT  CAST([transfer_date] AS DATE) ,
      account_key,COUNT(account_key) AS counter
FROM  transaction where counter>10 and counter<20
GROUP BY CAST([transfer_date] AS DATE),account_key;"
  try:
    m=cursor.execute(sql)
    m4=list(m)
    db.commit()
  except:
    db.rollback()
def l1_class():
  l1=[]
  sql =" SELECT count(*) from transaction t, account_info a where t.account_key==a.account_key and a.customer_key==query.customer_key  in  (SELECT  CAST(EXTRACT MONTH FROM [transfer_date] AS MONTH) ,
         account_key,COUNT(transaction_amt) AS counter
FROM transaction where counter<10 and transaction_type="INN" or transaction_type="OUT"
GROUP BY CAST([transfer_date] AS MONTH),account_key;"
  try:
    l=cursor.execute(sql)
    l1=list(l)
    db.commit()
  except:
    db.rollback()
def l2_class():
  l2=[]
  sql ="SELECT count(*) from transaction t, account_info a where t.account_key==a.account_key and a.customer_key==query.
        customer_key in (SELECT CAST(EXTRAXT MONTH FROM [transfer_data] AS MONTH),account_key,
        COUNT(transaction_amt)AS counter
        FROM transaction where counter<600 and transaction_type="INN"
        GROUP BY CAST([transfer_date] AS MONTH),account_key;"
  try:
    l=cursor.execute(sql)
    l2=list(l)
    db.commit()
  except:
    db.rollback()
def l3_class():
  l3=[]
  sql =" SELECT count(*) from transaction t, account_info a where t.account_key==a.account_key and a.customer_key==query.customer_key  in
         (SELECT  CAST(EXTRACT MONTH FROM [transfer_date] AS MONTH) ,
         account_key ,
         COUNT(transaction_amt) AS counter
         FROM  transaction where counter<500 and transaction_type="OUT"
         GROUP BY CAST([transfer_date] AS MONTH) ,
         account_key;"
  try:
    l=cursor.execute(sql)
    l3=list(l)
    db.commit()
  except:
    db.rollback()
def l4_class():
  l4=[]
  sql = "SELECT count(*) from transaction t, account_info a where t.account_key==a.account_key and a.customer_key==query.customer_key  in  (SELECT  CAST([transfer_date] AS DATE) ,
    account_key,COUNT(account_key) AS counter
FROM  transaction where counter<10
GROUP BY CAST([transfer_date] AS DATE),account_key;"
  try:
    l=cursor.execute(sql)
    l4=list(l)
    db.commit()
  except:
    db.rollback()
