# streamlit-ui-getting-started

[![codecov](https://codecov.io/gh/gsaini/streamlit-ui-getting-started/graph/badge.svg?token=3AF9C435OO)](https://codecov.io/gh/gsaini/streamlit-ui-getting-started)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![CodeCov](https://img.shields.io/badge/codecov-%23ff0077.svg?style=for-the-badge&logo=codecov&logoColor=white)


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



