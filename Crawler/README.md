## Jupyter notebook: Mining and predicting housing prices for real estate data

### Web-crawler 
Code for crawler is inside: [FCSE-Data-Mining/Crawler/0-Crawler.py](https://github.com/zelenkastiot/FCSE-Data-Mining/blob/master/Crawler/0-Crawler.py). 

The inital scraped csv is: [FCSE-Data-Mining/Crawler/real-estate.csv](https://github.com/zelenkastiot/FCSE-Data-Mining/blob/master/Crawler/real-estate.csv)


The rest of the scripts are just preprocessing the real estate dataset aqcuired with scraping, maping the values to ordinal (ordinal encoding) and then we have several different models and their accuracy scores based on a 75-25 split on the dataset (75% train, 25% test): 
- <code>1-CategoricalNB.py</code>
- <code>2-DecisionTreeClassifier.py</code>
- <code>3-RandomForrest.py</code>
- <code>4-LogisticRegression.py</code>
