import pandas as pd
import json

# Read encasher data
encasher_df = pd.read_csv('encasher.csv')
# Read purchaser data
purchaser_df = pd.read_csv('purchaser.csv')

# Sum of amount of all bonds
total_bonds_amount = purchaser_df['Denomination'].sum()

# Group by party and calculate total amount and percentage
party_summary = encasher_df.groupby('Name of the Political Party')['Denomination'].agg(['sum'])
party_summary['percentage'] = party_summary['sum'] / total_bonds_amount * 100

# Group by purchaser and calculate total amount and percentage
purchaser_summary = purchaser_df.groupby('Purchaser Name')['Denomination'].agg(['sum'])
purchaser_summary['percentage'] = purchaser_summary['sum'] / total_bonds_amount * 100

# Write to CSV file
party_summary.to_csv('party_summary.csv', header=['Total Amount', 'Percentage'])
purchaser_summary.to_csv('purchaser_summary.csv', header=['Total Amount', 'Percentage'])

# Print total sum of bonds
print("Total sum of bonds: {:,.2f}".format(total_bonds_amount))

# Create JSON objects for encashers
encasher_json = {}
for index, row in encasher_df.iterrows():
    if row['Name of the Political Party'] not in encasher_json:
        encasher_json[row['Name of the Political Party']] = []
    encasher_json[row['Name of the Political Party']].append({'Date of Encashment': row['Date of Encashment'],
                                                             'Denomination': row['Denomination']})

# Write encasher JSON to file
with open('encasher.json', 'w') as f:
    json.dump(encasher_json, f, indent=4)

# Create JSON objects for purchasers
purchaser_json = {}
for index, row in purchaser_df.iterrows():
    if row['Purchaser Name'] not in purchaser_json:
        purchaser_json[row['Purchaser Name']] = []
    purchaser_json[row['Purchaser Name']].append({'Date of Purchase': row['Date of Purchase'],
                                                   'Denomination': row['Denomination']})

# Write purchaser JSON to file
with open('purchaser.json', 'w') as f:
    json.dump(purchaser_json, f, indent=4)

print("CSV files 'party_summary.csv' and 'purchaser_summary.csv' have been generated.")
print("JSON files 'encasher.json' and 'purchaser.json' have been generated.")
