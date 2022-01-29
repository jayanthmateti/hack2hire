import csv
customer_risk_rating = []
with open('customer_info.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        if (line[0] != ""):
            customer_risk_rating.append({
                "customer_name": line[0],
                "Residential_Country": line[1],
                "Risk_rating": 0,
                "Risk_Rating_Reason": "",
                "Account_No": [],
                "transaction_in_month": {},
                "sum_in_month": {},
                "sum_out_month": {},
                "transaction_in_day": {}
            })
risk_countries = []
with open('countries_info.csv') as rc:
    risk_country = csv.reader(rc)
    for line in risk_country:
        if (line[1] != ""):
            risk_countries.append(line[1])
all_transactions = []
with open('customer_transactions.csv') as ct:
    cus_tran = csv.reader(ct)
    for line in cus_tran:
        if (line[0] != ""):
            all_transactions.append(line)

with open('customer_account_info.csv') as cai:
    cus_cai = csv.reader(cai)
    for line in cus_cai:
        for cus in customer_risk_rating:
            if (line[1] == cus['customer_name']):
                cus['Account_No'].append(line[0])


for customer in customer_risk_rating:
    for transaction in all_transactions:
        for account in customer['Account_No']:

            if (transaction[1] == account):

                date = "-".join(transaction[5].split('/')[1:])

                if (transaction[4] in risk_countries):
                    customer['transaction_in_month'].update(
                        {date: customer['transaction_in_month'].get(date, 0)+1})
                if (transaction[3] == "INN"):
                    customer['sum_in_month'].update(
                        {date: customer['sum_in_month'].get(date, 0)+int(transaction[2])})
                else:
                    customer['sum_out_month'].update(
                        {date: customer['sum_out_month'].get(date, 0)+int(transaction[2])})
                customer['transaction_in_day'].update(
                    {transaction[5]: customer['transaction_in_day'].get(transaction[5], 0)+1})

for customer in customer_risk_rating:
    for tm in customer['transaction_in_month'].values():
        if tm > 10:
            customer['Risk_rating'] = 3
            customer["Risk_Rating_Reason"] = "H1"
        elif (tm > 6):
            customer['Risk_rating'] = 2
            customer["Risk_Rating_Reason"] = "M1"

    for si in customer['sum_in_month'].values():
        if si > 1000:
            customer['Risk_rating'] = 3
            customer["Risk_Rating_Reason"] = "H2"
        if si < 1000 and si > 600:
            customer['Risk_rating'] = 2
            customer["Risk_Rating_Reason"] = "M2"
        if si < 600:
            customer['Risk_rating'] = 1
            customer["Risk_Rating_Reason"] = "L2"
    for so in customer['sum_out_month'].values():
        if so > 800:
            customer['Risk_rating'] = 3
            customer["Risk_Rating_Reason"] = "H3"
        if so < 800 and so > 500:
            customer['Risk_rating'] = 2
            customer["Risk_Rating_Reason"] = "M3"
        if so < 500:
            customer['Risk_rating'] = 1
            customer["Risk_Rating_Reason"] = "L3"
    for so in customer['transaction_in_day'].values():
        if so > 20:
            customer['Risk_rating'] = 3
            customer["Risk_Rating_Reason"] = "H4"
        if so > 10 and so < 20:
            customer['Risk_rating'] = 2
            customer["Risk_Rating_Reason"] = "M4"
        if so < 10:
            customer['Risk_rating'] = 1
            customer["Risk_Rating_Reason"] = "L4"

for cus in customer_risk_rating:
    if cus["Risk_rating"] > 0:
        print(cus["customer_name"])
        print(cus['Risk_rating'])
        print(cus["Risk_Rating_Reason"])
