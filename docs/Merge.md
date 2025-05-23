Merge Networks
====================
<a id="merge"> </a>

<a id="merge_networks"> </a>
## Merge Networks

Cytoscape Web allows for merging networks, through **Tools → Merge Networks**. The interface is very similar to that of the Cytoscape desktop application and will be familiar to Cytoscape users. 

![](_static/images/Merge/merge_networks_1.png)

<a id="basic_operations"> </a>
### Basic Operations

-    With the buttons select either **UNION**, **INTERSECTION** or **DIFFERENCE**.

-    All the networks available to merge are listed under **Available Networks**.
     Select 2 or more networks from this list and click the right arrow to transfer
     them to **Networks to Merge**. The first network is marked with a yellow star and is the base network; the other network will 
     be merged into the base network.
     
-    Click **Merge** to continue. The merged network will be displayed as a new network in your workspace.

<a id="advanced_options"> </a>
### Advanced Options

The **Advanced Network Merge** interface includes an expandable
**Advanced Options** panel, where you can specify the details of
how to merge the networks.

![](_static/images/Merge/merge_networks_2.png)

The options available here are:

-    **Merged Network Name**: here you can specify a custom name for the merged network.

-    **Matching columns**: this specifies the network columns that should
     be used for merging. Typically, the **name** column is used as matching attribute.
     Alternatively, you can decide to use a different column that contains some other type of identifier.

-    **How to merge columns**: a table lets the user specify for each of
     the individual network columns, what the corresponding column in the
     merged network should be named as well as its data type.

     Buttons below the table, allow to further specify how to merge columns for **NODES**, **EDGES** and **NETWORK** attributes individually.

![](_static/images/Merge/merge_collapse_nodes.png)

Additional checkboxes let you further specify the merging behavior:

**Enable merging nodes/edges in the same network**
-   This option is active by default and available for all 3 types of merge (Union, Intersection, Difference).
-   It allows to merge nodes within each network, in case they have the same value for the selected *matching attribute*.
-   This makes it possible to perform a network merge even when selecting *only 1 network*.
-   If you don't want to merge nodes within each network, you should disable this option.

**Merge only nodes and ignore edges**
-   This option is disabled by default and can only be used in an Intersection merge.
-   If you are interested in retrieving only the nodes that are shared between 2 or more networks, you should enable this option.






