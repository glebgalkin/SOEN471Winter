# SOEN471Winter
Project.
By 
Gleb Galkin    ID#40026736
Dmytro Semenov ID#40038839






US Accidents - Analysis and Predictions.
                                                       






Abstract:

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

Introduction:

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
 
Tree model, naive bayes classifier and multi layered neural network will be the main functions & tools used in the project. We will experiment with different parameters of the models as well as different sets of information i.e. we will test our assumptions of which data is relevant to determining location of the accident.

We will measure and compare each model and each model version (i.e. different ML model tuning or different information provided) with typical metrics: Recall, Precision and F-measure.
Depending on the application recall may have a higher importance than precision for the user of the modal, so we will include F2-measure as well.

At this moment of time we believe that the most relevant data to determine location of an accident within a given city are: time, weather conditions, most of the POIs listed above. 

Since the dataset is quite big, we will use Apache Spark to work with the dataset, to clean it up, filter, modify and compute data. We will utilize the in memory computation that Spark provides for faster processing compared to MapReduce model. We will test our assumptions and models on a smaller amount of data at first, for example 5% or 10% of the original dataset that totals at 1.5 GB. We will try to use the cluster computers provided by Concordia University to deliver our final models and results, which will be delivered on the original dataset.


