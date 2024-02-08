<h1>Open Weather API Django App</h1>

<p>This project is meant to show how ones can leverage the Open API while using Django. </p>
<p>Also, this participates to my own personal portfolio in which I show my capacity to deliver very simple projects using Django.</p>

<h2>What is this project all about?</h2>

<p>This project will provide the actual weather and a 5 days forecast. It's using the openweather API that you can find there: https://openweathermap.org/</p>
<p>The goal is to show the power of Django and key information that are contained in the open weather api.</p>
<p>This project could be the backbone to your own django app for weather forecast.</p>

<p>If you want to see more details, go to the dedicated Notion page I created for this project: https://boulder-roast-f20.notion.site/Openweather-API-Django-Application-af071a119490443ab16ec871c6636707?pvs=4</p>


<h2>How to get started?</h2>

<p>First thing you need to do is to clone this project.</p>

```
git clone https://github.com/kevinbuilds/django_openweather.git
```

<p>I would recommend that you start a virtual environment to start installing all the required packages for this project to start. Let's call this environment "env".</p>

```
python3 -m venv env
```

<p>Once installed, make sure you install all the packages that are included in the requirements.txt file.</p>

```
pip install -r requirementx.txt
```

<p>Lastly, your project cannot work unless you have your own API Key. You can find it directly on https://home.openweathermap.org/api_keys url.</p>

```
echo "$api_key" > API_KEY.txt
```

<h2>Launching the application</h2>

<p>To give a bit of context without doing a full Django tutorial, here are some key elements to consider:</p>
<ul>
<li>/weather_app/views.py contains your scripts,</li>
<li>/weather_app/static/style.css contains your styling,</li>
<li>/weather_app/templates/ contains all your html files,</li>
<li>The django app called weather_app has been added to settings.py in the dedicated section.</li>
</ul>

<p>The manage.py file is the one to launch to make your django app run:</p>

```
python3 manage.py runserver
```
