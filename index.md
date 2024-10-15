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

# Algorithms

	The artifact I chose for the algorithms and data structures was the Salvare Search for Rescue Web application, that is run in Jupyter Notebooks. The application aims to connect the rescue organization with dogs that can be trained for different types or rescue operations. It does this using a Jupyter Notebook with a Dash application for the web page layouts, which includes surfacing the spreadsheet of selected animals, a selection of radio buttons for the parameters required for each type of rescue, and a graph to show a breakdown of the different animals. The application uses a python API to interact with a MongoDB backend. Before I was able to enhance the project, I had to create a local instance of the MongoDB with the 10000 rows of animals. This was due to the instance available during class being spun down after the semester ended. The numbers in the table are an average of 5 tests, with the highest and lowest score removed, and the middle three averaged out.
	A major inefficiency from the original code was that every time there was a need to sort, or filter the Panda’s data frame, the code would make a new API call to the database, pass the database the filtering parameters, then return the data. While running the local instance, the time for each of these calls to complete is shown in the Original Artifact Time column in yellow, and is still very quick. However, with larger datasets, and cloud based systems, this could lead to massive load times, and increased cloud costs due to repeated and unnecessary database calls. The first enhancement experiment that I made was to use the original data frame: 
  
  ```python
  df = pd.DataFrame.from_records(shelter.read({})) 
  ```

  that is called when the program is started, and when the “Reset” button is pressed; and retrieves the rows based on the required specifications for each animal, and using Python’s copy() function, to create an independent data frame for each type of rescue. This uses O(n) * (number of additional dataframes) memory and keeps the O(n) time complexity for the filter method, but creates the copy for instant reference in the application by removing the extra database calls. This is the best option for the user experience, as shown in the table, with an essentially instant response time when selecting different types of rescue animals. However, this does cache each of the data frames, and will use extra memory to do so. The “Reset” button is the only button that will make a new API call to retrieve the data in the MongoDB database and catch any potential updates. This technique resulted in an average time of 0.020 seconds per animal change, with a total savings from the original artifact of 0.036 seconds.
	For the second experiment, I decided to create a middle ground that would remove the extra API calls, but not have the downsides of the increased memory usage due to caching all the filtered data frames that Enhancement 1 had. This option, Enhancement 2; instead of pre-filtering and storing the different search types in memory, will create the new data frame by applying the filter to the original data frame when the radio button is pressed. The potential network calls are the same as from Enhancement 1, with a new data frame being called only when the “Reset” button is called, and at the beginning of the program to populate the dashboard. The time complexity when a button is pressed would only be O(n) with O(n) memory usage. The average time of selecting each button for the second enhancement was 0.026 seconds per filter, with an average difference of 0.031 seconds from the original artifact.
	When completing this enhancement, I was able to design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution while managing the trade-offs involved in design choices. I also was able to create a table with the enhancements that would be of use in measuring the trade-offs of each different algorithm using small amounts of code to potentially have huge cost savings at scale, especially for a cloud based application. This demonstrates an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals.


| Type of Search        | Original Artifact Time (s) | Enhancement 1 Time (s) | Enhancement 2 Time (s) |
|:----------------------|:---------------------------|:-----------------------|:-----------------------|
| Water                 |                     0.0140 | 0                      | 0.0065                 |
| Mountain / Wilderness | 0.0120                     | 0                      | 0.0055                 |
| Disaster / Tracking   | 0.0105                     |  0                     | 0.0050                 |
| Reset                 | 0.1889                     | 0.0987                 | 0.1017                 |

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


