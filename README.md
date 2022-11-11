# RestaurantAPITask

this application contains backend-api

## Project setup

python version = 3.9

1. First you have to create virtual-environment 
    - If you have install virtualenv then follow command
        - virtualenv -p python(your python version) envornment-name
    - If you don't have install virtualenv then install first

2. Activate Virtual environment
    - For Linux 
        - source environment-name/bin/activate
    - For window
        - environment-name\Scripts\activate

3. install requirements.txt
    - pip3 install -r requirements.txt

4. Run Project Using command "python manage.py runserver"

## API Documentations

https://documenter.getpostman.com/view/11889792/2s8YeoQZ9J

### Account Section
  1. Account Create
    In this api user can giving some basic information for raustraunt owner and as well as giving restraunt information as key name is "restraunt_data" in account create api.

  2. OTP Verification
    In this api user has must verify otp for account create and restraunt create. If otp verification successfull then restraunt and user both are created successfully.

  3. Login User
    In this api user can login and get access and refresh token for authentication.

  4. Employee Create
    In this api restraunt owner can create their employee account giving some basic information like email, first_name, last_name etc. and as well as giving restraunt id for linking with this restraunt.


### Restraunt section 
  1. Main Menu Create
    If restraunt owner is authenticated then he/she is create main menu list for the restraunt.

  2. Show Main Menu
    In this api getting main menu list for specific restraunt no need to be authentication.

  3. Daily Menu Create 
    If restraunt owner is authenticated then he/she is create daily menu list for restraunt.

  4. Show Daily Menu
    In this api getting daily menu list for specific restraunt for giving restraunt id there is no need to be authentication. Daily menu list showing according to date.

  5. Feedback 
    In this api visitor/customer are giving feedback for daily menu. One customer are giving feedback in one day each restraunt. 
    