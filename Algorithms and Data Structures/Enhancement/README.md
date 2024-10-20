# Algorithms and Data Structures from CS-340 Client/Server Development

This artifact contains the enhancement of the [Original](./Original) artifact. 
The application aims to connect the rescue organization with dogs that can be trained for different types or rescue operations. It does this using a Jupyter Notebook with a Dash application for the web page layouts, which includes surfacing the spreadsheet of selected animals, a selection of radio buttons for the parameters required for each type of rescue, and a graph to show a breakdown of the different animals. The application uses a python API to interact with a MongoDB backend.

For the enhancement, I created an experiment inside of Jupyter Notebook, to decrease the loading time for the dataframes. This included reducing the number of API calls, and implementation of algorithmic principles to reduce the load times to O(n), and the memory usage to O(1) while cutting out the repeated API calls that could result in a large bill from any cloud provider.

For the full story on what I completed, as well as graphical aids, please see the [Algorithms and Data Structures](https://samwalts.github.io/#algos-and-ds) of my portfolio.
