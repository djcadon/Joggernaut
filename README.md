# Joggernaut
Fitness workout DBMS for CS4092

Keeping track of progress in the gym is hard. Joggernaut is here to help with that!

Joggernaut is a fitness tracking application that helps you keep track of your fitness journey. By utilizing a Postgres database, you can keep track of your workouts, exercises and progress all in one place. You can also keep yourself and your friends accountable by adding them as your Joggernaut Friend!

### Setup Instructions

1. Clone the repository
2. Create a `.env` file by performing this command at the root folder
    ```
    cp .env.template .env
    ```
3. Enter the database connection keys inside the `.env` file
4. Navigate to source directory using
    ```
    cd src
    ```
5. Install all python requirements by running
    ```
    pip install -r requirements.txt
    ```
6. Run the streamlit app by running
    ```
    streamlit run ./login.py
    ```
    or
    ```
    python -m streamlit run ./login.py
    ```

### How to Use Joggernaut?
1. You begin by logging in, if you do not have an existing account, please make one by clicking 'Sign Up'
2. Once you have an account, you will be redirected to the home page. At the home page, you can see how many exercises you've done this week as well how your friends are doing on their progress.
3. Using the side navigation bar, you can access all your pages.
4. Exercises page is to keep track of each of your exercises
5. The workouts page is to keep track of workouts. You can create workouts by adding exercises to them.
6. The Find Friends page is for you to find your friend using their username and add them as a friend!
7. The User Profile page shows you all your critical information
8. The Progress page is for you to keep track of your progress on all exercises, and based on workouts too.