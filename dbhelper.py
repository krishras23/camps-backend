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


# admin permissions

def add_camp(name, description, MIN_AGE, MAX_AGE, price_per_week):
    add_camp_query = "INSERT INTO SummerCamps.Camps (name, description, MIN_AGE, MAX_AGE, price_per_week) values (\"{" \
                     "}\", \"{}\", {}, {}, {})".format(name, description, MIN_AGE, MAX_AGE, price_per_week)
    print(add_camp_query)
    write_to_db(add_camp_query)


def delete_camp(name):
    delete_camp_query = "DELETE FROM SummerCamps.Camps WHERE name like \"{}\"".format(name)
    print(delete_camp_query)
    write_to_db(delete_camp_query)


def update_camp_price(CampID, new_price):
    update_camp_price_query = "UPDATE SummerCamps.Camps SET price_per_week = {} WHERE CampID = {}".format(new_price,
                                                                                                          CampID)
    print(update_camp_price_query)
    write_to_db(update_camp_price_query)


def update_camp_ages(CampID, new_MIN_AGE, new_MAX_AGE, ):
    update_camp_ages_query = "UPDATE SummerCamps.Camps SET MIN_AGE = {}, MAX_AGE = {} WHERE CampID = {}".format(
        new_MIN_AGE, new_MAX_AGE, CampID)
    print(update_camp_ages_query)
    write_to_db(update_camp_ages_query)


update_camp_ages(1, 80000, 90000)
