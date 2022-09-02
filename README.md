## Running the project

To run the project locally make follow the next steps :
- make sure you have python installed
- Pull the project from git provider.
- run the comman `Scripts\activate`, if the activation was successful, then you’ll see the name of your virtual environment, (env), at the beginning of your command prompt.
- install the used libraries, mentioned in the `usedlib.txt` file, using the following command `python -m pip install -r usedlib.txt`
- cd into the source file using `cd src`
- finally, run the application using the command `pyhton manage.py runserver`
- Open `http://127.0.0.1:8000/` on your browser, or you can login as an admin on the `http://127.0.0.1:8000/admin`
- the admin credentials are as follows: Email : `salahek25@gmail.com`      , Password `luffy1234`
- the parts requiring an email to be sent won't be functionnal, as you're gonna have to manually enter your email credentials on the `settings.py` file in the `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` fields as shown in the following image :

![image](https://user-images.githubusercontent.com/99540220/188193597-2ad73eaa-01b1-4022-a168-a1e78e844405.png)
