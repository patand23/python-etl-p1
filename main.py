import sql
from pgsql import query
import insert

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

     query(sql.create_schema)
     query(sql.create_table)
     insert.all()


    #select data
    #results = query(sql.test_select);
    #print("results: ", results)


 #See PyCharm help at https://www.jetbrains.com/help/pycharm/
