from interact_with_DB import interact_db

class DBcomplains:

    def insert(self,id, username, order_number, subject, problem, file_url):
        query = "insert into web_project_g16.complains \
                        values ('%s', '%s', '%s', '%s', '%s', '%s');" % (id, username, order_number, subject, problem, file_url)
        interact_db(query=query, query_type='commit')

    def get_last_complain_id(self,username):
        query = "SELECT *" \
                " FROM web_project_g16.complains " \
                "where username = '%s';" % (username)
        answer = interact_db(query=query, query_type='fetch')
        return len(answer)

# Creates an instance for the DBproducts class for export.
dbComplains = DBcomplains()