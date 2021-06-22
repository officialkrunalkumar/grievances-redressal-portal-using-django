# Grievances Redressal Portal

Grievance Redressal Portal using Django

> ## Prerequisites

1. Download the project as zip archive and extract it to your desired location or just clone the repository by.
    for SSH clone :- 

    ```
    $ git clone git@gitlab.com:krunalkumar/grievances-redressal-portal.git
    ```
    or for HTTPS clone :- 
    ```
    $ git clone https://gitlab.com/krunalkumar/grievances-redressal-portal.git
    ```
2. Change the directory to the project folder

    ```
    $ cd grievances-redressal-portal
    ```

3. Postgres must be setted up and configured.

> ## To run the Project

1. Open the Terminal and change the path to directory with all files.
   
2. Write the following command to start the Postgres psql server.

    ```
    $ sudo -u postgres psql
    ```
3. Create the Database and User by executing the `create.sql` file

    ```
    postgres=# \i create.sql
    ```

4. Exit the psql terminal by

    ```
    postgres=# \q
    ```

5. Create a Virtual Environment by

    ```
    $ virtualenv venv
    ```

6. Activate the environment by

    ```
    $ source venv/bin/activate
    ```

7. Install the required packages by

    ```
    $ pip3 install -r requirements.txt
    ```
8. Now goto the app directory.
    ```
    $ cd grs
    ```

9.  Now Run the following command to create the and link the database to the application

    ```
    $ python3 manage.py migrate
    ```


10. Create a super user for admin functionality by.

    ```
    $ python3 manage.py createsuperuser
    ```
    Now, it will ask for `username`, `email`, `password` and `confirm password`,
    You can pass any name you want or just copy paste the below names.
    
11. Now, Run the following command to run the application
    ```
    $ python3 manage.py runserver
    ```

12. Now, To see the Application, go to the following link in any browser

    ```
    127.0.0.1:8000
    ```
13. To see the admin view goto the following link.

    ```
    127.0.0.1:8000/admin
    ```
    pass the credentials you created superuser with.

> ### After viewing all

<br>

1. Now, kill the server by `Ctrl+C`

2. Deactivate the environment by

    ```
    deactivate
    ```
3. Move one directory back by.
    ```
    $ cd ..
    ```

4. Drop the Database and User by

    ```
    sudo -u postgres psql
    ```

    ```
    postgres=# \i delete.sql
    ```
This will Drop the Database and User

5. And to exit from psql, type

    ```
    postgres=# \q
    ```