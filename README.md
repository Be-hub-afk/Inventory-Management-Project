## Inventory Management System

    Authors 
1. Ben Ochoro.
2. Joan Njoroge.
3. Jacquiline Tulinye.

### Overview

The Inventory Management System project aims to develop a comprehensive system for managing inventory levels, orders, and stock.This initiative is to support the marketing team by offering resources and insights that improve their approaches and decision-making procedures. The system can provide useful insights on market trends, product performance, and consumer behaviour by utilising data analytics. The marketing team can improve their outreach efforts overall, target audiences more precisely, and fine-tune their campaigns thanks to this data-driven strategy.


### Project Goal
To create an intelligent inventory management system that can predict stock requirements, automate reordering processes, and identify trends in inventory usage.The system aims to automate and simplify the process of managing product inventories. Real-time inventory level monitoring will be provided by the system, which will also issue alarms when quantities drop below predetermined levels. In addition to preventing stockouts, this proactive warning system makes sure that the marketing team is aware of the availability of products. By integrating such a system, overall operational efficiency is improved and the danger of lost sales opportunities owing to inadequate inventory is reduced.


### Business Understanding
The project addresses the challenge of managing inventory in a dynamic sales environment.

### Data Understanding 
The dataset includes historical inventory data, sales records, and supplier lead times. It captures the quantity of items sold, dates of transactions, stock levels, and reorder points.


###  EDA

The metrics used for the EDA analysis include :

1. Popular products : 
   Determining which products have the highest sales volume or revenue.

2. Sales trends : 
   Analyzing how sales have changed over time.

3. Sales seasonality : 
   Identifying any patterns or trends that repeat over a specific period (e.g., monthly, quarterly, annually).


First ,we take a look at the descriptive statistics of our dataset to gain further Numerical insights of our dataset.

#### Descriptive Statistics

Key insights from the descriptive statistics of the dataset:

1. Transactions: There are 5020 transactions, with some duplicate transaction IDs (4908 unique IDs). This suggests possible multiple entries per transaction.

2. Date Range: The data spans from January 1, 2022, to December 31, 2022.

3. Products: There are 10 unique products, with 'Thai Tea' being the most frequent.

4. Price and Quantity: The average price per unit (Price_x and Price_y seem to be the same and range from 3,200 to 18,000, with an average of about 9,685. The average quantity purchased in a transaction is about 3.64.

5. TotalAmount: The total amount spent per transaction ranges from 7,500 to 88,000, with an average of about 32,279.

6. Store Details: There are 12 unique stores, and the data includes 7 different store groups. The majority of transactions are in 'General Trade' type stores.

7. Customer Demographics: The age of customers ranges from 0 to 72, with an average of about 40. The gender field is binary (0 or 1), suggesting two gender categories.


### Popular products

Our approach was determining which products have the highest :

1. Sales volume/Total quantity sold.
2. Total Revenue generated.

##### Sales Volume 

This visualization paints a clear picture on the products with the highest quantity sold,with 'Thai Tea' and 'Ginger candy' being the most purchased products.
 
Top 5 Products by Sales Volume:

1. Thai Tea
2. Ginger Candy
3. Choco Bar 
4. Coffee Candy 
5. Yoghurt

##### Total revenue generated

This  visualizations and data shows which products are most popular in terms of total sales revenue. 
'Cheese Stick' and 'Choco Bar' are particularly notable for their high revenue generation , with the highest revenue generators being :
1. Cheese Stick
2. Choco Bar
3. Coffee Candy
4. Yoghurt
5. Oat

### Sales Trends

Our analysis entailed determining and visualizing Sales Trends(i.e based on the monthly total sales amount) and analyze how sales have changed over time, looking at daily, weekly, and monthly trends. Metrics for analysis inluded :

1. Product Performance :

   To Examine which products are top-sellers and how their sales vary over time.


2. Store Performance : 

   To Explore how sales differ by store type and location.
   
Let's start with analyzing sales trends over time. 

We'll create visualizations to help understand these trends better.

Based on the the monthly sales trends chart, here are some key insights we can infer:

Seasonal Variations:

There appears to be a peak in sales around the second month on the chart, which suggests a possible seasonal influence or a special event that caused a temporary increase in sales. This could be related to a holiday period, a major sales event, or a successful marketing campaign.

Sales Decline:

After the peak, there is a noticeable decline in the following month, which is quite sharp. This might indicate that the peak was indeed due to a one-time event or that there was an inventory or stock issue following the high-demand period.

Recovery and Fluctuations:

Following the sharp decline, sales seem to recover but do not reach the previous peak. There is some fluctuation with a general downward trend. This could imply that the market is facing some instability or that consumer demand is waning for the products offered.

Overall Trend:

The overall trend from the start to the end of the period seems to be slightly downward, despite the fluctuations. This might indicate a need for concern and could be a point of focus for the business to investigate further.


Implications for Business Strategy:

Depending on the cause of the peak and subsequent decline, the business might need to consider diversifying its products, adjusting pricing, improving supply chain resilience, or enhancing marketing efforts to smooth out such volatility.

### Sales Seasonality 

Our analysis identified sales seasonality behaviour over varied time ,any patterns or trends that repeat over a specific period (eg., monthly, quarterly, annually).
Started by :

1. Aggregating sales data monthly, quarterly, and annually.

2. Analyzing trends and patterns in these time frames.
3. Visualizing the results to identify any recurring patterns or significant insights.

 Plot showing the total transaction amount over the time period.

Some observations that could be useful for the marketing team :

Fluctuations in Transaction Amounts: The graph shows significant fluctuations in transaction amounts over time, with some peaks that suggest occasional high-value transactions.

Time Series Data: The data is time series, spanning a number of months, which indicates a good amount of historical data that can be analyzed for trends.

No Clear Seasonal Pattern: There doesn't appear to be a clear, repeating seasonal pattern. For marketing purposes, identifying periods of increased transactions could align with specific campaigns or market events.

Outliers: There are several spikes that stand out above the rest. These could be special events, sales, or promotions that resulted in higher transaction volumes.

A bar plot showing distribution of transactions over months.

Some key insights and analysis that could be relevant for a marketing team:

Transaction Volume by Month: The chart suggests a variation in the number of transactions across different months. The highest number of transactions occurs in the 2nd month, and the lowest is seen in the 6th month.

Possible Seasonality: There may be seasonality in the transaction data, with certain months consistently seeing higher or lower transaction volumes. For example, months 1, 2, 11, and 12 show higher transaction volumes which could indicate seasonal peaks.

Planning Marketing Campaigns: Knowing which months have the highest and lowest number of transactions can help in planning marketing campaigns. Campaigns could be timed to boost transactions during typically low months or to capitalize on high-transaction months.

Consumer Behavior: The variations might reflect consumer behavior patterns, such as increased spending during specific seasons or holidays which correspond to certain months.

Resource Allocation: This data can help the marketing team allocate resources effectively, focusing their efforts on months that require a push or scaling back during months where the transaction volume is traditionally high.

Historical Data Comparison: It would be useful to compare this data with the same months in previous years to identify if the patterns are consistent or if there are any anomalies.

Promotional Impact: If there were any promotions or special deals offered in certain months, their impact on transaction volumes could be assessed. For instance, if the 2nd month had a major sale event, this could explain the peak in transactions.

Product/Service Review: The months with fewer transactions might be a good time to review the product or service offerings or customer service touchpoints to understand if improvements can be made.



A bar plot showing distribution of transactions over days of the week.

The bar chart illustrates the distribution of the number of transactions per day of the week. Here are several insights and an analysis that could be valuable for a marketing team:

Transaction Distribution: The transactions are fairly evenly distributed across the days of the week, with no single day showing a dramatically higher or lower number of transactions compared to the others.

Mid-Week Peak: There is a slight peak on the third day of the week (Wednesday), which may indicate mid-week is a slightly more popular time for transactions.

Weekend Analysis: The number of transactions does not drop significantly on the weekend (days 5 and 6), suggesting that consumer purchasing behavior remains consistent through the end of the week.

Marketing Strategies: Since there is no dramatic fluctuation, daily marketing efforts could be uniform throughout the week. However, slightly increased efforts on Wednesday could capitalize on the mid-week peak.

Operational Planning: The consistent number of transactions across the week suggests that staffing and operational support should be steady, without the need for significant scaling up or down on any particular day.

Promotional Timing: If promotions are run, they could be tested on different days of the week to see if they can shift the distribution curve and stimulate additional transactions on lower volume days.

Customer Engagement: The data may be indicative of consistent customer engagement throughout the week, which is positive for any retail or service business.

Further Segmentation: The marketing team might want to segment these transactions by time of day or customer demographics to refine their understanding of when and who is transacting.

Competitor Activity: It would be beneficial to understand competitor promotions and activities to see if there's a correlation between their marketing efforts and the transaction distribution.

External Factors: Consideration of external factors, such as holidays or local events, which might affect the number of transactions on specific days, could also provide more context.

In conclusion, while there are slight variances in transactions per day, the overall distribution is quite balanced. This suggests that the marketing team could implement a consistent daily strategy with the potential for small adjustments to optimize for the slight mid-week peak.

### Modelling

Our analysis aims to forecast future product sales, enabling us to create an effective inventory management system. To achieve this, we will employ univariate time series analysis, allowing us to generate predictions for each distinct product within our inventory.

Our first step  is use to use our data to generate the daily aggregate sales for each unique product


Our data is stationary

## Model Using VAR

Vector Autoregression, is a statistical model used for time series analysis which is particularly suitable for analyzing relationships among multiple time series variables. As we want to analyse and predict sales for different products , VAR is a suitable model for our analysis.

From the results of our forecast we can see that our predictions become similar at some point. This could be as a result of the lack of diversity or variability in the training data making it difficult for the model to capture patterns that lead to diverse and distinct predictions. This is being caused by the fact that our data only has sales for only one time period (2022)

Our RMSE is 4.40 which is relativley low meaning our model prediction accuracy is reasonable. However due to the lack of diversity in the predictions, we will experiment with VAR models with other values to see if the predictions will improve.

From our analysis observation , our model with an order of 1 performs better with the lowest AIC and BIC as compared to other models. An outregressive order of 1 means that  each variable in the model is regressed on its own past value (lag 1).

Our models rmse is similar to our first's model's rmse. At some point this model is also making similar predictions.


## Model Using LSTM

Make use of a long short-term memory model due to its ability to identify deviations or anamolies and also its ability to handle sequences of different lengths irrespective of the duration of the time series. in this case, our dataset is very small with only one year sales.


Build another model  with two LSTM layers in the encoder and two LSTM layers in the decoder.

Our E1D1 model has a slightly smoother curve compared to our E2D2 model. While a smoother validation loss curve is generally a sign that the model is performing better we need to make use of other technique to have a more comprehensive understanding of the models performance.

From our observation the RMSE of e1d1 is higher by 0.005. This is a significant difference in our case because our first model had an rmse 
 4.40 meaning every slight improvment of model performance counts.

From our observation our ltsm model is still making predictions with similar values. We will experiment with a neural network model due to its ability to learn patterns and irregular fluctuations from data and contain noise especially in instances with little historical data as in our case



## RNN MODEL

### Challenges during modelling
Despite experimenting with various models and prediction methods , the biggest challange has been the models still generating similar forecast values.Despite the ensemble model generating different results, we find that the results are very close in value.

One main reason for this would be not having enough historical data as the data we are working on only has sales for one year making it not enough for the models to determine patters in the data. 

### Recommendations

Collect more data for our analysis

### INVENTORY MANAGEMENT

