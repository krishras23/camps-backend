from mysql.connector import connect, Error


# read path
def get_enrollments():
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            enrollments = []
            get_enrollments_query = "select * from SummerCamps.child_information"
            with connection.cursor() as cursor:
                cursor.execute(get_enrollments_query)
                for record in cursor:
                    enrollments.append(record)
                return enrollments
    except Error as e:
        print(e)

get_enrollments()

# create connection to update the database
def write_to_db(camp_query):
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(camp_query)
                connection.commit()
                return ""
    except Error as e:
        print(e)


# write path for child_information

def create_child(student_id, name, allergies, age):
    create_child_query = "insert into SummerCamps.child_information (student_id, name, allergies, age) " \
                         "values ({}, \"{}\", \"{}\", {})".format(student_id, name, allergies, age)
    write_to_db(create_child_query)
    print(create_child_query)


def update_child(name, new_age):
    update_child_query = "UPDATE SummerCamps.child_information SET age = {} WHERE name like \"{}\"".format(new_age,
                                                                                                           name)
    write_to_db(update_child_query)
    print(update_child_query)


def delete_child(name):
    delete_child_query = "delete from SummerCamps.child_information where name = \"{}\"".format(name)
    write_to_db(delete_child_query)
    print(delete_child_query)
