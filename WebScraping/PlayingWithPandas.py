import pandas as pd
from bokeh.plotting import figure, show
from bokeh.transform import factor_cmap 

titledCols = {"Total Deaths": [1, 2, 3, 4], "NewDeaths": [4, 5, 6, 7], "Deaths Per Million": [1, 1, 1, 1]}
test = pd.DataFrame(titledCols)
#test.index = ["Brazil", "Croatia", "Argentina", "Chad"]

print(test)

# what if I populate the lists in a for loop then create the dataframe in one line. Not create the df in a for loop