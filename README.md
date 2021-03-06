# Zillow: What is driving the errors in the Zestimates®?

## About the Project
For this project we will be using machine learning clustering methodologies to uncover what are the drivers of the errors found in Zillow's Zestimate® figures. 

<b>What is a [Zestimate®](https://www.zillow.com/zestimate/#acc)?</b> 
- It is Zillow's estimate of a given home's market value. Public (MLS data and tax records) and property owner's submitted data are taken into account to make this estimation. 

<b>How accurate are Zillow Zestimates®?</b> 
- According to <b>[FreeStoneProperties](https://www.freestoneproperties.com/blog/truth-zillow-zestimates/#:~:text=Is%20a%20Zillow%20Zestimate%20High,about%20the%20accuracy%20of%20Zestimates.&text=For%20example%2C%20depending%20on%20the,only%2062%25%20of%20the%20time.)</b> ,
"The median error for larger markets is usually around 2% of the sale price of the home. But the problem with Zestimates is that when they are wrong, they can be significantly wrong. For example, depending on the metro area, Zillow might be within 5% of the sale price only 62% of the time."   

<b>What data was used in this project?</b> 
- The Zillow database for single unit/single family homes properties from 2017


## Goals
- To improve our original estimate of the log error by using clustering methodologies.
- To find the key drivers of error in the Zestimate® figures.


## Deliverables:
- Final notebook: Should contain plenty of markdown documentation and cleaned up code
- README: Explain what the project is, how to reproduce the work, and project planning notes.
- Python modules: Should contain data acquisition and preparation files.


## Data Dictionary
| Feature | Definition |
|---------------------------|--------------------------------------------------------------------------------------------------------------|
| parcelid                       | Assigned by your local tax assessment office, unique for each property | 
| logerror                       | Discrepancy between actual sell price and listed sell price |  
| calculatedfinishedsquarefeet   | Square feet: length (ft.) x width (ft.) |  
| bedroomcnt                     | Number of bedrooms in a unit |  
| bathroomcnt                    | Number of bathrooms in a unit | 
| taxvaluedollarcnt              | Property taxes of unit for the year |
| taxamount                      | Amount of tax due for the given year |  
| fips                           | Federal Information Processing Standards (6037, 6059, 6111, or null) uniquely identify geographic areas | 
| latitude                       | Distance of a place north or south of the earth's equator |
| longitude                      | Distance of a place east or west of the meridian |


## Initial Thoughts & Hypothesis
### Thoughts
- Clustering should be a useful tool to answer this question

### Hypothesis
Tax amount is the main cause of error in Zestimate  
- Null hypothesis: The log error is independent of the tax amount 
- Alternative hypothesis: The log error is dependent of the tax amount  

## Project Steps
### Acquire
- Data is aquired from the Zillow SQL Database.
- Login credentials are required.
- The functions are stored in the acquire.py file.
- File is a reproducible component for gathering the data.

### Prepare
- Created a prepare.py file. 
- Data is split into train, validate, and test. 
- Data is scaled as necessary.
- Make sure that column data types are appropriate for the data they contain.
- Missing values are investigated and handled.
- Outliers are investigated and handled.
- File is a reproducible component that handles missing values, outliers, and changes in data types. 

### Explore
- Run statistical testing and visualization.
- At least 3 combinations of features for clustering should be tried.
- Summarized your takeaways and conclusions.  

### Model
- At least 4 different models are created and their performance is compared. 
- One model is the distinct combination of algorithm, hyperparameters, and features.


### Conclusion
<b>Key Drivers of Log Error:</b>
- Tax amount 
- Bedroom count 
- Calculated square footage

<b>Takeaways:</b> 
- There seems to be a normal distribution relationship between logerror and taxamount
- As tax amount gets lower, log error increases
- Homes with tax amount < 50,000 start to have more log error
- As bedroom count increases, log error increases
- Slightly more log error in homes with < 3000 sqft

### Future Investigations
- What is relationship between bedroom count and total home square footage?
- Perform more K-means testing on more features 

## How to Reproduce
All files are reproducible and available for download and use (need login credentials for access to Zillow company database).
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, and Final_Report.ipynb files

## Contact Me  
Dani Bojado
- daniella.bojado@gmail.com 
