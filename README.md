# Preprocessing Web App

## About the Project

This project is a web application that visualize on how the text proprocessing work.

## Screenshots

![image](https://raw.githubusercontent.com/mfakhrulam/preprocessing-web-app/main/assets/ss.png)

## How to Use Locally


1. First, clone this repository with:

```
git clone https://github.com/mfakhrulam/preprocessing-web-app.git

```

2. Now, create a virtual environment to run the project

```
python -m venv .venv

```

3. Then, activate the virtual environment

Windows:  
```
.venv\Scripts\activate
```
Linux and Mac:
```
source .venv/bin/activate

```

4. Install the requirements
```
pip install -r requirements.txt

```

5. Download nltk puntk, wordnet, and stopwords
```
python nltk_download.py

```

6. Make .flaskenv file and specify the appropriate file to run:
```
FLASK_APP=app
FLASK_DEBUG=True
```

7. Install the dependencies
```
npm install

```

8. Run the following command to compile and watch for changes for the Tailwind CSS file:
```
npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch

```

9. Run the flask app using different console:
```
flask run

```


credit: mfakhrulam


