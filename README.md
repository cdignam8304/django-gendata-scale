# django-gendata-scale
Scale out the generic data application

## Generic data upload script

NB: for date fields have to ensure in YYYY-MM-DD format, and use following function to handle missing dates:

def test_value(x): 
    ...:     if x == "": 
    ...:         return None 
    ...:     return x 

e.g. date1 = test_value(row[1]]


with open(vendors) as f: 
    ...:     reader = csv.reader(f, delimiter="|") 
    ...:     for row in reader: 
    ...:         _, created = Generic.objects.get_or_create( 
    ...:             schema_name_id = row[0], 
    ...:             string1 = row[1], 
    ...:             string2 = row[2], 
    ...:             string3 = row[3], 
    ...:             string4 = row[4], 
    ...:             string5 = row[5], 
    ...:             int1 = row[11], 
    ...:             int2 = row[12], 
    ...:             string10 = row[6], 
    ...:             string6 = row[7], 
    ...:             string7 = row[8], 
    ...:             string8 = row[9], 
    ...:             string9 = row[10], 
    ...:             status = row[13] 
    ...:         ) 

