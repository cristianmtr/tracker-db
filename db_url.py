import os
# do export VARIABLE="value_here"
# one = "mysql+mysqlconnector://{}:{}@localhost:3306/taskfreak".format(os.environ['MYSQLUSER'],
                                                                     # os.environ['MYSQLPASSWORD'])
two = "postgresql://{}:{}@localhost:5432/tracker".format(os.environ['PSQLUSER'],
                                                                 os.environ['PSQLPASSWORD'])

