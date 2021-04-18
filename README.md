# SOEN471Winter
Project.
By 
Gleb Galkin    ID#40026736
Dmytro Semenov ID#40038839

**Full Report with data analysis and exploration can be found here:**

**jupyter notebook accessible at the root of the project:**

[./US Accidents technical analysis and regression.ipynb](https://github.com/glebgalkin/SOEN471Winter/blob/main/US%20Accidents%20technical%20analysis%20and%20regression.ipynb)

**or view in nbviewer if ipynb does not work for you**

https://nbviewer.jupyter.org/github/glebgalkin/SOEN471Winter/blob/main/US%20Accidents%20technical%20analysis%20and%20regression.ipynb





# US Accidents - Analysis and Predictions.
                                                       






## Abstract:

Despite the technological growth and its significant impact on safety the amount of car accidents is still a huge problem. 
The goal of this project is to analyze a dataset containing the information about car accidents in the United States from 2016 to 2020.
Main objectives:
Provide statistics and expected amount of cases in the upcoming year
Display state & amount of severity distribution in terms of accidents
Compare road types and amount of cases

Team's expectations - substantive results:
Most populated states such as California, Texas, Florida and New York will contain the most amount of car accidents.  
Such states with higher population will have the biggest aggregated wait time during the traffic.
The increase of car accidents due to the winter season in northern states. 
Highway cases severity is greater than cases occurred on regular roads.

## Introduction:

The United States of America is known as one of the busiest nations in terms of road traffic and car crashes. According to “Statista” (Jul, 2020), there are approximately 280 million vehicles in use and more than 228 million citizens have a valid license. However, each year there are thousands of cases involving car crashes that affect the traffic. 

In this project we are going to analyze a dataset of 4’200’000 accidents recorded in the US from 2016 to 2020. The data is gathered from Bing and Mapquest, two big companies that collect accident and traffic data. The dataset was suggested as a challenge on kaggle and can be found here: https://www.kaggle.com/sobhanmoosavi/us-accidents.


On a daily basis most people waste a significant amount of time stuck in traffic. In this project we have outlined the following objectives:
Based on the data from 2016 to 2020 forecast traffic for year 2021: provide statistics and valuable information on how many cases should be expected in the upcoming year.
Analyze the 4’200’000 accidents and display state distribution, accident severity distribution and time length of the traffic caused by the accident.
Compare the cases between different road types, and, based on analysis, deduct what road type contains the most amount of car accidents.

Main challenge we set before us is to build an ML model to predict the location of an accident. The challenge includes analyzing the dataset and selecting the factors that are most likely to influence the next accident location and time, such as weather conditions, time of the day, day of the week etc.

Patterns found in accident occurrence can help authorities understand the causes of the accidents, such as potholes, poor traffic signal visibility and poor road markings. Any fixes they apply to the listed problems will reduce the amount of accidents happening as well as average daily traffic.

Materials and Methods:
As stated in the Introduction we will use a dataset containing various information about traffic accidents that occurred in the US between 2016 and 2020 years. The data is very diverse including the following information: 
accident severity,
time period of the traffic flow problems caused by the accident
location in lat/lng coordinates.
traffic length in miles caused by the accident
street, street side, city, state, county and zip code of the accident
weather conditions such as humidity, visibility, temperature etc.
presence of amenities, bumps on the roads, crossings, junctions, give way signs, no exit, railways roundabouts, stations, stops, presence of traffic signals etc.

Our end goal is to analyze the dataset and build an ML model that could predict latitude and longitude of an accident given other parameters of the accident.
 
Logistic regression and Decision Tree Classifier will be the main classifiers used in the project. We will experiment with different parameters of the models as well as different sets of information i.e. we will test our assumptions of which data is relevant to determining location of the accident.

We will measure and compare each model and each model version (i.e. different ML model tuning or different information provided) with typical metrics: F-measure.
Depending on the application recall may have a higher importance than precision for the user of the modal, so we will include F2-measure as well.
We will handle the problem of the present dataset imbalance by simply overfitting the minor class and underfitting the majority.

We will use 80/20% split for train test of our models

At this moment of time we believe that the most relevant data to determine location of an accident within a given city are: time, weather conditions, most of the POIs listed above. 

Since the dataset is quite big, we will use Apache Spark to work with the dataset, to clean it up, filter, modify and compute data. We will utilize the in memory computation that Spark provides for faster processing compared to MapReduce model. We will test our assumptions and models on a smaller amount of data at first, for example 5% or 10% of the original dataset that totals at 1.5 GB.

## Results
From Address location we extracted the type of the road where an accidents happen as can be seen on the pie chart below:

![image](https://user-images.githubusercontent.com/22376976/114464927-6cfef980-9bb4-11eb-8481-e5482f025a89.png)

Figure 1. Ratio of accidents happening on regular street vs other types of road

As can be seen the big majority of accidents happen on fast roads like highways, parkways etc.

We also observed that accidents in general happen mostly during work days, which makes sense since people are in rush when going to and from work:

![image](https://user-images.githubusercontent.com/22376976/114464950-77b98e80-9bb4-11eb-9fd2-8bbd3ee87a49.png)

Figure 2. Ratio of accidents by day of the week

![image](https://user-images.githubusercontent.com/22376976/114464993-843de700-9bb4-11eb-8671-50377a377701.png)

Figure 3. Accidents by state

Roads often get blocked for maintenance, there are a lot of unknown external factors besides all the given information. People in the US states are also very different in their cultural values, mindsets. Our main objective is to be able to predict the severity level of traffic caused by an accident that occurred in a selected state. The authorities can use that information to improve existing conditions or predict ahead of time the locations where high severity traffic may occur under certain conditions and improve the road/signs or just warn people. Further on GPS navigators the moment the know about an accident can predict the severity of traffic it may cause, then proactively choose another route and avoid traffic accumulation in general.

To demonstrate model performance we will learn the models on the accidents that occurred in highest accidents states, which as can be seen above are CA, TX and FL
we care about accuracy and f measure in this case, since over predicting level 4 accidents may make a GPS navigation way too unreliable to use.
Since we are trying to predict classes 1, 2, 3, 4, we are required to use multi class classification models like Logistic Regression and Decision Tree:

![image](https://user-images.githubusercontent.com/22376976/114465044-915ad600-9bb4-11eb-85e9-2d30006d251a.png)

We can see from the results that Logistic Regression constantly had worse performance than Decision Tree, that may have to do with a lot of categorical data that we have in our dataset. Also The F measure is actually higher for all the tests. This usually means that the model is very good at predicting a specific class but not so good at predicting the other.

## Discussion
Predicting 4 classes with an extreme imbalance turned out to be a very challenging task. It would help a lot if the sources that provide the data could define a clear criteria of when a traffic goes to severity levels 2 or 3 or 4. Also there are other external factors at play, human factor in general has a huge impact on the traffic severity, it would really help to know for example how many lanes got blocked because of the accident or a percentage of still available road, maybe that percentage could take into account any already existing construction present etc. maybe for each street the dataset could contain a typical business of a road or some measure bby how quick authorities react to cleanup the accident and thus clean up traffic
Still, surely a giant like Google with Google Maps and many satellites deployed could gather and predict traffic severity for their route prediction, so the investigation and further research in this subject can yield amazing results


