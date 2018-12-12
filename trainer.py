import pandas as pd

excel = pd.read_excel('jd_list_tagged.xlsx')

# update column names
excel.columns = ['doc_id','description','label']

# review the data - this function displays top 5 rows
excel.head()
