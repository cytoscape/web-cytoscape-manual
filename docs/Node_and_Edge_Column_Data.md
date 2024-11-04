Node and Edge Column Data
========================================
<a id="node_and_edge_column_data"> </a>

Interaction networks are useful as stand-alone models but they are
most powerful for answering scientific questions when integrated with
additional information. Cytoscape Web allows the user to add arbitrary node,
edge and network information as node/edge/network column data. This could include, 
for example, annotation data on a gene or confidence values in a protein-protein 
interaction. These column data can then be visualized in a user-defined way by setting up a mapping
from columns to network attributes (colors, shapes, and so on). The
section on **[Styles](Styles.html#styles#)** discusses this in greater detail.

<a id="import_data_table_files"> </a>
## Import Data Table Files

Cytoscape Web offers support for importing data from delimited text data tables.

***Sample Data Table 1***

<table cellspacing="0" style="table-layout: fixed; dwidth: 500px">
<caption style="width: 500px">Sample Data</caption>
<tr> <th class="">Object Key</th>  <th class="center">Alias</th>        <th class="center">SGD ID</th>  </tr>
<tr> <th class="spec">AAC3</th>    <td class="">YBR085W|ANC3</td>       <td class="">S000000289</td>    </tr> 
<tr> <th class="specalt">AAT2</th> <td class="alt">YLR027C|ASP5</td>    <td class="alt">S000004017</td> </tr>
<tr> <th class="spec">BIK1</th>    <td class="">YCL029C|ARM5|PAC14</td> <td class="">S000000534</td>    </tr>
</table>
<br>


The data table file should contain a primary key column and at least one
data column. The maximum number of data columns is unlimited. The
**Alias** column is an optional feature, as is using the first row of
data as column names. Alternatively, you can specify each column name
from the **File → Import → Table from File...** user interface.

<a id="basic_operation"> </a>
### Basic Operation

1.  Load your network via **Data → Open network(s) from NDEx**, or **Import → Network from File** in the **Data** option of the **Menu Bar**.

2.  Select **Data → Import → Table from File...**.

2.  Select a data file in either .txt or .csv format.
    Alternatively, you can click the **Import Table from File...** button ![Importtablebutton.png](_static/images/Node_Edge_Column_Data/Importtablebutton.png) in the **Table Panel**.

3.  The **Edit Column Definitions** interface will open:

![](_static/images/Node_Edge_Column_Data/EditColumnDefinitions.png)

4.  First, select where you want to import your data to under **Import data as**, either "Node table columns" or "Edge     table columns".

5.  Next, designate which column in your network contains the ++Key** to be used to map the network to the data under **Key Column for Network**. 

6.  To select a **Key** column in the data file, click on the column header, and click the key icon under **Meaning** in the pop-up interface. Make sure the column designated as key matches the key in the network.

![](_static/images/Node_Edge_Column_Data/DataColumnKey.png)

7.  Similarly, to change the data type of a column, for example from 
    integer to string, click the column header and select the correct data type under **Data Type**.
    
8. A message at the bottom of the interface will inform you of how many rows of data will be imported to your network. Click **Confirm** to continue.
    
9.  The **Advanced Settings** allows you skip one or more of the first rows of data, and to specify if the first row contains column names.
    
8.  Click **Confirm** to import.

<a id="table_panel"> </a>
### Table Panel

When data has been imported, it is visible in the corresponding tab in the **Table Panel**:

![](_static/images/Node_Edge_Column_Data/TablePanelData.png)

-   Column data can be edited by double-clicking the cell. Once finished
editing, click outside of the editing cell in the **Table Panel** to save your edits. If you want to apply the same value to all rows in the column, select **APPLY VALUE TO COLUMN** at the top. Similarly, you can choose to apply your edits to all selected nodes by clicking **APPLY VALUE TO SELECTED NODES**. Pressing **Esc** while editing will undo any changes.

-   To select a node in the network corresponding to a row in the **Table Panel**, select the row and then click **SELECT NODES** at the top.

-   Rows in the panel can be sorted by specific column. To sort, click on a column heading and select the **Sort Ascending** ![](_static/images/Node_Edge_Column_Data/SortAscending.png) or **Sort Descending** ![](_static/images/Node_Edge_Column_Data/SortDescending.png) button. 

-   A new column can be created using the **Insert New column**
![](_static/images/Node_Edge_Column_Data/InsertColumns.png)
button. Columns can be deleted using the **Delete
Columns...**
![](_static/images/Node_Edge_Column_Data/DeleteColumns.png)
button. This will remove the column from Cytoscape Web completely, not just
from the **Table Panel**.

-   Columns can be renamed by clicking on the **Rename column** ![](_static/images/Node_Edge_Column_Data/RenameColumn.png) button and typing in a new name.