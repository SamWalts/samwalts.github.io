---
layout: default
---

Text can be **bold**, _italic_, or ~~strikethrough~~.

[Link to another page](./another-page.html).

There should be whitespace between paragraphs.

There should be whitespace between paragraphs. We recommend including a README, or a file with information about your project.

# Software Engineering and Design

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

## What I did with to meet milestones

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

# Databases

This was part of the Software Engineering and design. Look at how cool I am!

### Header 3
{:.no_toc}
```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

# Algorithms and Data Structures
[Orignal Artifact](https://github.com/SamWalts/samwalts.github.io/tree/main/CS-499%20Algorithms%20and%20Data%20Structures/Original).
[Enhancement](https://github.com/SamWalts/samwalts.github.io/tree/main/CS-499%20Algorithms%20and%20Data%20Structures/Enhancement).

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


<div style="text-aligh: center;">
  <a href = "https://github.com/SamWalts/samwalts.github.io/blob/main/assets/images/SNHU_CS_499_Algorithms_BarChart_Times.png" target = "_blank">
    <img src="./assets/images/SNHU_CS_499_Algorithms_BarChart_Times.png" width="720px" title="Screen Loading Times Chart" />
  </a>
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


