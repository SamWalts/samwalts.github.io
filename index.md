# Computer Science Capstone
{: .no_toc}

## CS-499 | SNHU
{: .no_toc}

### Professional Self Assessment 
<img id="self-assessment" src="assets/images/header_photos/professional_self_assessment.png" alt="Professional Self-Assessment" title="Professional Self-Assessment" />


### Code Review 
The purpose of a code review is to ensure quality and standards are upheld. This is a vital step for imparting knowledge, early bug detection, and improving collaboration on the development team. This is a highly important step in producing quality code. Below, you can the code review that I completed before starting on the enhancements that are displayed in this portfolio.

<div style="text-align: center;">
    <div style="position: relative; padding-bottom: 56.25%; padding-top: 30px; height: 0; overflow: hidden;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/WBrN8XKE9ro?si=HCTj1QMMw5N6LwOX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
</div>

Figure 1 - Software Design and Engineering Code Review Video


# Software Engineering and Design
<img id="self-assessment" src="assets/images/header_photos/software_engineering_and_design.png" alt="Software Engineering and Design.png" title="Software Engineering and Design" />

This artifact was created using the code from CS-320, a test automation and QA course, that contained only the Contact and ContactService classes with the accompanying tests classes. I designed a GUI that would turn the middle services into a full contact application, using Java with JavaFX, CSS, and MySQL. To handle dependencies, and accommodate JavaFX and MySQL, I have added a Maven file to handle dependencies and integrated Github Actions that build the project based on the pom file, will run the unit tests, and then build and package the jar file for download.

<div style="text-align: center;">
    <img src="assets/images/ContactApp_Github_CI_Screenshot.png" width="100%" title="Task Scheduler Diagram - Thermostat Lab Guide" />
    <p><em>Figure 1 - Github Actions for Portfolio Enhancement - CS20 Software Test Automation and QA</em></p>
</div>

With this CI/CD pipeline, I can showcase my devops skills. While creating the project, I demonstrated an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals. I was also able to keep the application loosely coupled, and a CI pipeline that will automatically run the tests on push to main to protect the main branch. In addition, the user input is validated, secured by my implementation of the database with JDBC and prepared statements. This shows that I have Developed a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources.  

While creating the Github Actions, I was able to start making the beginnings of a CI pipeline and start the process of running the integration tests for Regressions that occur when you are making any code changes. This included writing the .yml file and creating the rules that pull requests must pass certain checks. While the application itself is simple, I am able to show my design processes, and best practices from a design, security, and efficiency standpoint. This included keeping following the MVC pattern to separate the concerns of the model from the view and the controller. This was accomplished by having minimal validity checks on the controller, to only see if a field was empty. The actual data is passed to the model, and then validated, with a success or failure message surfaced on the controller as shown on _Figure 2_.

<div style="text-align: center;">
    <img src="assets/images/ContactApp_UML_Diagram_10-18-24.png" width="100%" title="Task Scheduler Diagram - Thermostat Lab Guide" />
    <p><em>Figure 2 - UML diagram CS320 - CS320 Software Test Automation and QA</em></p>
</div>

---

### Milestones Completed

* Completed an MVC application
   * Loosely coupled and easily tested and extensible
   * Followed best practices for seperation of concerns
* Created a Maven file for dependency management


---

Databases and Software Engineering and Design [Enhanced](https://github.com/SamWalts/samwalts.github.io/tree/adding_DB/CS-499%20Database%20and%20Software%20Engineering%20and%20Design/Enhancement)

Databases and Software Engineering and Design [Original](https://github.com/SamWalts/samwalts.github.io/tree/adding_DB/CS-499%20Database%20and%20Software%20Engineering%20and%20Design/Original)

---

<div style="text-align: right;">
    <a href="#">
        <button style="font-size: 10px; font-weight: 500; background: #4169e1; color: #ffffff; border-radius: 50px; border-style: solid; border-color: #4169e1; padding: 5px 5px;">Back to Top &#8593;</button>
    </a>
</div>


# Databases
<img id="self-assessment" src="assets/images/header_photos/databases.png" alt="Databases" title="Databases" />

The artifact that I chose for the Database enhancement was the same artifact I chose for the software Design and Engineering. The artifact is based on the SNHU course CS 320, a class which emphasized customer requirements and appropriate unit testing. The original files were a contact service middleware and accompanying unit tests that I enhanced to include a JavaFX graphical user interface and backend database. This enhancement will show the changes that I made to implement the MySQL database with the user interface to create persistent storage. Specifically, the enhancements will include the implementation of the database with the Java Database Connectivity (JDBC). Because the JDBC is such a resource intensive object, it will only be created once, and reused several times using the singleton pattern. The ContactService makes extensive use of the DBConnection class. As such, Unit testing and mocking were not enough. In order to satisfy testing needs, and ensure that data is correctly stored, the ContactServiceTest class was changed to implement [testcontainers](https://testcontainers.com/) that allow for integration tests using a real database. Using this method I was able to test all of the methods but one, cover over 90% of the lines of code in the models.

<div style="text-align: center;">
    <img src="assets/images/ContactApp_Test_Coverage.png" width="100%" title="Task Scheduler Diagram - Thermostat Lab Guide" />
    <p><em>Figure 1 - Github Actions for Portfolio Enhancement - CS20 Software Test Automation and QA</em></p>
</div>

The skills that I demonstrate with this enhancement include a full stack capability with the Java language. This includes how to surface errors on the main page, error handling for SQL errors, and how to manage resource intensive operations such as handling the JDBC. I continue to demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals. This includes utilizing an industry leading database, MySQL. I was able to develop a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources. This was enforced by using encapsulation for the program and enforcing the Model View Controller design pattern for safety and security, to create easily extensible software that is well written and well tested.

List of enhancements performed from the original artifact
1. Created MySQL database with first name, last name, address, phone number, and an id.
1. Implemented a JavaFX GUI for interacting with the contact database.
1. Implemented a table view for showing saved contacts.
1. On click, text fields will automatically populate for easy updating.
1. Changed the Contact and ContactService classes to use DBConnection instead of a HashMap.
1. Implemented Maven for dependency management.
	1. Enforced encapsulation with Model View Controller design pattern.
	1. Updated unit tests to ensure proper testing.
	1. Implemented Mocking for the updated ContactService class.
	1. Using Github Actions, created a CI pipeline for pull and push to Main:
		1. Automatically build based on Maven pom.xml
		1. Run unit tests
		1. Create zip file containing completed JavaFX project
---

Databases and Software Engineering and Design [Enhancement](https://github.com/SamWalts/samwalts.github.io/tree/adding_DB/CS-499%20Database%20and%20Software%20Engineering%20and%20Design/Enhancement)

Databases and Software Engineering and Design [Original](https://github.com/SamWalts/samwalts.github.io/tree/adding_DB/CS-499%20Database%20and%20Software%20Engineering%20and%20Design/Original)

---

<div style="text-align: right;">
    <a href="#">
        <button style="font-size: 10px; font-weight: 500; background: #4169e1; color: #ffffff; border-radius: 50px; border-style: solid; border-color: #4169e1; padding: 5px 5px;">Back to Top &#8593;</button>
    </a>
</div>

# Algorithms and Data Structures
<img id="self-assessment" src="assets/images/header_photos/algorithms_and_data_structures" alt="Algorithms and Data Structures" title="Algorithms and Data Structures" />

The artifact I chose for the algorithms and data structures was the Salvare Search for Rescue Web application, that is run in Jupyter Notebooks. The application aims to connect the rescue organization with dogs that can be trained for different types or rescue operations. It does this using a Jupyter Notebook with a Dash application for the web page layouts, which includes surfacing the spreadsheet of selected animals, a selection of radio buttons for the parameters required for each type of rescue, and a graph to show a breakdown of the different animals. The application uses a python API to interact with a MongoDB backend. Before I was able to enhance the project, I had to create a local instance of the MongoDB with the 10000 rows of animals. This was due to the instance available during class being spun down after the semester ended. The numbers in the table are an average of 5 tests, with the highest and lowest score removed, and the middle three averaged out.

A major inefficiency from the original code was that every time there was a need to sort, or filter the Panda’s data frame, the code would make a new API call to the database, pass the database the filtering parameters, then return the data. While running the local instance, the time for each of these calls to complete is shown in _Figure 1_ in the Original Artifact Time column, and is still very quick. However, with larger datasets, and cloud based systems, this could lead to massive load times, and increased cloud costs due to repeated and unnecessary database calls. The enhancements and experiments I created are designed to showcase the potential time and cost savings of using the dataframes more effeciently. The first enhancement experiment that I made was to use the original data frame and then create cached dataframes by storing the new frame that was filtered from the original into their own seperate dataframes.
```python
df_Mountain_Wilderness = df[            # DF for Mountain / Wilderness
                (df['animal_type'] == 'Dog') &
                (df['breed'].isin(['German Shepherd', 'Alaskan Malamute', 'Old English Sheepdog', 'Siberian Husky', 'Rottweiler'])) &
                (df['sex_upon_outcome'] == 'Intact Male') &
                (df['age_upon_outcome_in_weeks'] >= 26) &
                (df['age_upon_outcome_in_weeks'] <= 156)].copy()
```

This uses O(n) * (number of additional dataframes) memory and keeps the O(1) time complexity for retrieving the cached dataframes, but creates the copy for instant reference in the application by removing the extra database calls. This is the best option for the user experience, as shown in _Figure 1 Enhancement 1 column_, with an essentially instant response time when selecting different types of rescue animals. However, this does cache each of the data frames, and will use extra memory to do so. This is not a problem for smaller data sets, but with every added option, the memory required would rapidly increase. The “Reset” button is the only button that will make a new API call to retrieve the data in the MongoDB database and catch any potential updates. 

### Logging the Time ###
The time was captured by using the time module in Python, and making a start, and end point inside of the update_dashboard() method, then making a print statement with the elapsed time. I would then select each option and read from the console the time for each. The tests were then ran 5 times each, and the result is the _Figure 1_ table, and _Figure 2_ bar chart of the average over 5 times.
  
| Type of Search        | Original Artifact Time (s) | Enhancement 1 Time (s) | Enhancement 2 Time (s) |
|:----------------------|:---------------------------|:-----------------------|:-----------------------|
| Water                 | 0.0140                     | 0                      | 0.0065                 |
| Mountain / Wilderness | 0.0120                     | 0                      | 0.0055                 |
| Disaster / Tracking   | 0.0105                     | 0                      | 0.0050                 |
| Reset                 | 0.1889                     | 0.0987                 | 0.1017                 |

_Figure 1 - Table of loading times for the Original, Enhancement 1, and Enhancement2, in seconds_

For the second experiment, I decided to create a middle ground that would remove the extra API calls, but not have the downsides of the increased memory usage due to caching every single one of the filtered data frames that Enhancement 1 had. This option is enhancement 2, and you can see the the comparison of it in _Figure 1_ and _Figure 2_; instead of pre-filtering and storing the different search types in memory, this enhancement creates makes a data frame by applying the filter to the original data frame when the radio button is pressed. The potential network calls are the same as from Enhancement 1, with a new data frame being called only when the “Reset” button is called, and at the beginning of the program to populate the dashboard. The time complexity when a button is pressed would only be O(n) with O(n) memory usage. You can see the The average time of selecting each button for the second enhancement was 0.026 seconds per filter, and the comparison of enhancement 2 and the original in _Figure 2_.

When completing this enhancement, I was able to design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution while managing the trade-offs involved in design choices. I also was able to create a table and chart with the enhancements that would be of use in measuring the trade-offs of each different algorithm using small amounts of code to potentially have huge cost savings at scale, especially for a cloud based application. This demonstrates an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals.

---
Algorithms and Datastructures [Original](https://github.com/SamWalts/samwalts.github.io/tree/main/CS-499%20Algorithms%20and%20Data%20Structures/Original)

Algorithms and Datastructures [Enhancement](https://github.com/SamWalts/samwalts.github.io/tree/main/CS-499%20Algorithms%20and%20Data%20Structures/Enhancement)

---

<div style="text-aligh: center;">
    <img src="./assets/images/SNHU_CS_499_Algorithms_BarChart_Times.png" width="720px" title="Screen Loading Times Chart" />
  <p><em>Figure 2 - Bar chart of the orginal artifact and two options of enhancements - CS-340 Client/Server Development </em></p>
</div>

#### Header 4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### Header 6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### There's a horizontal rule below this.

* * *

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

### Small image

![Octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)

### Large image


### Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```


