# Zillow: What is driving the errors in the Zestimates®?

## About the Project
For this project we will be using machine learning <b>clustering methodologies</b> to uncover what are the drivers of the errors found in Zillow's Zestimate® figures. 

What is a [Zestimate®](https://www.zillow.com/zestimate/#acc)? 
- It is Zillow's estimate of a given home's market value. Public (MLS data and tax records) and property owner's submitted data are taken into account to make this estimation. 

How accurate are Zillow Zestimates®? 
- According to [FreeStoneProperties](https://www.freestoneproperties.com/blog/truth-zillow-zestimates/#:~:text=Is%20a%20Zillow%20Zestimate%20High,about%20the%20accuracy%20of%20Zestimates.&text=For%20example%2C%20depending%20on%20the,only%2062%25%20of%20the%20time.),
"The median error for larger markets is usually around 2% of the sale price of the home. But the problem with Zestimates is that when they are wrong, they can be significantly wrong. For example, depending on the metro area, Zillow might be within 5% of the sale price only 62% of the time."   

What data was used in this project?
- The Zillow database for single unit/single family homes properties from 2017


## Goals
- To improve our original estimate of the log error by using clustering methodologies.
- To find the key drivers of error in the Zestimate® figures.


## Deliverables:
- Final notebook: Should contain plenty of markdown documentation and cleaned up code
- README: Explain what the project is, how to reproduce the work, and project planning notes.
- Python modules: Should contain data acquisition and preparation files.


## Data Dictionary
| Feature                   | Definition                                                                                                                                                       | Type        |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| parcelid                  | Assigned by your local tax assessment office, unique for each property                                                                                           | discrete    |
| calculatedfinishedsquarefeet                    | Square feet: length (ft.) x width (ft.)      | continuous  |  
| bedroomcnt                   | Number of bedrooms in a unit      | discrete  |  
| bathroomcnt                   | Number of bathrooms in a unit      | discrete  | 
| taxvaluedollarcnt                   | Property taxes of unit for the year      | continuous  | 
| fips                      | Federal Information Processing Standards (6037, 6059, 6111, or null) uniquely identify geographic areas                                                          | categorical |
| latitude                  | Distance of a place north or south of the earth's equator                                                                                                        | continuous  |
| longitude                 | Distance of a place east or west of the meridian                                                                                                                 | continuous  |
| propertycountylandusecode | Land use zones are the codes that the government uses to classify  parcels of land (chars with numbers)                                                          | discrete    |
| propertyzoningdesc        | Zoning refers to municipal or local laws or regulations that dictate  how real property can and cannot be used in certain geographic areas  (chars with numbers) | discrete    |


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
- Observations: 
- Takeaways: 

## How to Reproduce
All files are reproducible and available for download and use (need login credentials for access to Zillow company database).
- [ ] Read this README.md
- [ ] Download the aquire.py, prepare.py, and Final_Report.ipynb files

## Contact Me 
Dani Bojado
- daniella.bojado@gmail.com 