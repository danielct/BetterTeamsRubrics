# Better Teams Rubrics

Short script to generate a Microsoft Teams rubric to help mark assignments.

<img src="https://github.com/danielct/RubricsForTeamsTests/blob/main/pics/Marking.png?raw=true" width="200"/>

Microsoft Teams doesn't have great support for assignments that have multiple open-ended questions with different mark values. However, given question values, it's possible to make a [rubric](https://support.microsoft.com/en-us/office/create-and-manage-grading-rubrics-in-microsoft-teams-68292a5f-f582-4a41-8ba3-8c96288ec5ca) which can [assign the correct mark value](https://answers.microsoft.com/en-us/education_ms/forum/all/marking-maths-tests-on-assignments-on-teams/5d202645-867d-455b-b9dc-189493c2bef5) for each question. 

Creating such a rubric by hand is tedious, so I have written a short script to generate a rubric given question values.

# Usage  

1. Download RubricCreator.exe (or RubricCreator.py if you have python installed) from this repo.

2. Using excel, create a CSV file that specifies the question values. The first column should contain the question names and the second column should contain the corresponding values.

   ![](https://github.com/danielct/RubricsForTeamsTests/blob/main/pics/Excel1.png?raw=true)

3. Run RubricCreator and select your CSV file.

   ![](https://github.com/danielct/RubricsForTeamsTests/blob/main/pics/Run.PNG?raw=true) 

4. A rubric corresponding to the question values will be generated in the same folder as the specification CSV file. The filename will be the same but with "_Rubric" appended.

   ![](https://github.com/danielct/RubricsForTeamsTests/blob/main/pics/Output.png?raw=true) 

5. [Upload](https://support.microsoft.com/en-us/office/create-and-manage-grading-rubrics-in-microsoft-teams-68292a5f-f582-4a41-8ba3-8c96288ec5ca#ID0EAABAAA=Share_rubrics) and attach this rubric to the assignment in Teams. You may need to enter the correct value for "Total Marks". 

6. Grade assignments using the rubric. The total number of marks is calculated automatically. Be careful not to select the "N/A" options or you will get fractional marks.

<img src="https://github.com/danielct/RubricsForTeamsTests/blob/main/pics/Marking.png?raw=true" width="300"/>

   In the Examples folder you can find an example assignment, specification file, and the generated rubric.

# Limitations

- Teams won't let you have more than 20 categories in a rubric. For us, that means a maximum of 20 questions. Maybe they'll fix this later.
- The way Teams handles decimals is a bit odd, so you may encounter fractional marks (eg. 5.01) if the total number of marks does not divide 100, or for questions that have 3 or 6 marks.
- If the total number of marks doesn't divide 100 you may get an "error uploading rubric message". One workaround is to add a dummy question to bring the total number of marks to a number that divides 100. 
- The teams rubric specification is undocumented and a bit finnicky. If you get an "error uploading rubric" message, feel free to contact me.

