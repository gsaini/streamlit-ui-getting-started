# streamlit-ui-getting-started
Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver dynamic data apps with only a few lines of code. Build and deploy powerful data apps in minutes. Let's get started!


## To run Streamlit from the command line:
```
streamlit run uber_pickups.py
```

## Step 1: Run Coverage with the Configuration
Run the coverage command as before, and it will now ignore the test files:

```
coverage run --source=uber_pickups -m unittest discover -s /workspaces/streamlit-ui-getting-started -p "test_*.py"
```

## Step 2: Generate the Coverage Report
Generate the coverage report to verify that the test files are excluded:
```
coverage report -m
```

## Step 3: (Optional) Generate an HTML Report
If you want a detailed HTML report, run:
```
coverage html
```


## Try out a limited version of Streamlit right in your browser.

Just edit the code below and the app on the right updates automatically. 

https://streamlit.io/playground
