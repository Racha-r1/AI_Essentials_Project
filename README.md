# AI_Essentials_Project

AI assignment to predict the quality of white wine using the KNN model and the Random forest model.
There is also an API available for both models that is build with flask.

## API Routes

#### ```POST /knn =>``` returns the predictions of the data send through the post request using the KNN model

#### ```POST /random-forest =>``` returns the predictions of the data send through the post request using the random forest model

## Data format

This section gives more information about the format of the data that you need to send in the POST request to each endpoint. You have to send a JSON object with a property data. That property data should map to a 2d array. Each array item needs to have 10 elements that stand for the following.

| Index | Value |
| ----- | ----- |
| 0 | volatile acidity |
| 1 | citric acid |
| 2 | residual sugar |
| 3 | chlorides |
| 4 | free sulfur dioxide |
| 5 | total sulfur dioxide	 |
| 6 | density |
| 7 | pH |
| 8 | sulphates |
| 9 | alcohol |

The response is an array with the labels that correspond to the quality score of the wine.
- Bad => quality score <= 5
- Mediocre => quality score of 6 or 7
- Good => quality score > 8

### Example request
``` 
{
   "data" : "[[0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.0010, 3.00, 0.45, 8.8],[0.37, 0.36, 20.7, 0.045, 42.0, 120.0, 1.0010, 3.00, 0.45, 8.8]]"
}
```

### Example response
``` 
["Mediocre", "Mediocre"]
```
