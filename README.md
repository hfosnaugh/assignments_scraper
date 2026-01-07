**Directions for use**
Set up .venv --> ```python -m pip install beautifulsoup4, pandas, openpyxl```
1. Download Assignments page on Canvas
2. Replace the HTML string variable with the filepath of the assignments html
3. Run the code. You now have all your assignments and due dates in assignments.xlsx :)



**Directions for adding to Notion calendar**

NOTE: this is for the calendar database view, not the seperate Notion calendar app

After completing the steps above:
1. Open assignments.xlsx
2. Open Notion calendar in table view
3. Copy the assignment names and dates from excel. Select several rows from the table and paste.
Now the names and dates should automatically be added to your calendar.


*Other tips:*
- You can change the properties of multiple pages at once by selecting them, right clicking, and editing properties
- If you don't have Excel, you can simply change ```.to_excel``` to ```.to_csv``` and ```assignments.xlsx``` to ```assignments.csv``` to get a CSV instead.
