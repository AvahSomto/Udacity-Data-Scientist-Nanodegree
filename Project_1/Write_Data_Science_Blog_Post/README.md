# In-depth analysis of Seattle and Boston Airbnb Data

## Brief Overview

The Seattle and Boston Airbnb datasets were mined based on the CRISP-DM framework.

The business problems I tried to uncover were:
What features strongly affect Airbnb rental price?
What features distinguished Airbnb homes in Seattle from those in Boston?
How to differentiate the reviews based on price?

## File Description

- The IDE used was DataSpell.
- Two datasets:
   Detailed Listings data for Boston and Seattle.
   Dataset Link: insideairbnb.com
- A Third dataset was used to ensure generalization of the model. The New York dataset was sourced from https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data.

## Results of the analysis

Results and discussion were published on Medium: [Deep Dive Into Seattle and Boston Airbnb Data](https://medium.com/@sajjadmanal/deep-dive-into-seattle-and-boston-airbnb-data-d8e6fea5eab0?sk=0834ffb85786e74bd95e5e45ffe4bf23)
   
In this project, I used two datasets - Seattle and Boston, I compared the two datasets and developed a machine learning model to forecast the rental price for both cities. Features that didn't correlate with the target label [price] were dropped. In order to ensure that the model could be able to generalize well with unseen data, a third dataset was used. The New York dataset was used to ensure that the model generalize well with unseen data.
