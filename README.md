# Visualizing-Experiment-Duration

Helping marketers optimize their experimentation efforts

Conducting A/B test takes lot of effort both in terms of time and money. What if the traffic on your site is really low to conduct an A/B test. Hence, it is important to predetermine the expected experiment duration by estimating the sample size required for the test. This helps marketers to optimize their efforts for choosing the fastest and most efficinet test.

Here is an interactive web application that help visualize the experimentation duration required for different variations of A|B tests. 

# Project Outline 
## Data Cleaning 
The data has been handled for any missing values, duplicate entires, text incosistencies and data corruption using Jupyter Notebook. 

## Determine Sample Size for A/B test using Power Analysis 
* The conversion rate for each webpage/country pair as been assigned between 1%-10% randomly
* A significance level of 95% is assumed
* Probability of accepting null hypothesis has been kept at 20%
* An Effect Size of 2% (Relative) has been considered

Sample Size calculator available at https://www.evanmiller.org/ab-testing/sample-size.html has been referred.


## Calculated the Expected Experiment Duration 
The expected experiment duration has been calculated by dividing the sample size required for each variation (calculated above) by the webpage traffic per week (given). 
The units are 'per week'.


## Visualize Durations to determine the best possible test 
The dashboard is available in form of a python application (app.py).Kindly follow the following steps to run the dashboard -
* Download app.py and map.csv in same location
* Install the following libraries - Dash, Plotly, & Pandas. Run following commands in terminal/command_prompt:
```
pip install pandas
```
```
pip install Dash 
```
```
pip install plotly
```


* Run the python file in the traditional way
```
$ python app.py
```
* The dashboard will open in your web browser (As part of localhost) on a freely available port.
* In case the port it is trying to run on is not freely available, follow these steps to restart the stuck port:
 - Paste the following code in terminal
 ```
 ps -fA | grep python
 ```
You will get a pid number by naming of your flask number. Now copy the pid number from second column of your project row of terminal output.

- Then write as below
```
kill -9 pid
```
Restarting and re-running the app should work now

* For quick reference sake, the screenshots of the Dashboard are available under the folder by the same name.


## Author

* **Shriya Gupta** 

## Acknowledgments

* Natalie Zayats
* Dash(https://dash.plot.ly/dash-core-components)




