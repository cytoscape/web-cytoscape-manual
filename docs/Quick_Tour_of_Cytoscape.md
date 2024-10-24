Quick Tour of Cytoscape Web
========================================
<a id="quick_tour_of_cytoscape_web"> </a>

This chapter describes the basic layout and mechanics of using Cytoscape Web. When you start Cytoscape Web for the first time, the interface will look like the image below:

![](_static/images/Quick_Tour/quick_tour_1.png)

The interface layout is very similar to that of the Cytoscape desktop application, whith the **Control Panel** on the left, **Table Panel** at the bottom and **Network View Window** on the right.

When a network is loaded, Cytoscape Web will look similar to the image
below:

![](_static/images/Quick_Tour/quick_tour_2.png)

Most functionalities are self-explanatory, but we'll go through a
concise explanation of the interface components for clarity.

-   The **Menu Bar** is at the top of the screen and contains several options (see below for more information about
    each menu). Also in the Menu Bar, to the right, are the **Search Tool** and **NDEx Login** button.

-   The **Workspace Panel** (Workspace tab of the Control Panel). 
    This is where all the networks you are working with are listed.
    You can have several networks in your workspace, but only one of them can be selected and dispayed at any given time; this is called the 'current' network.
      
-   The **Network View** window displays the current network. At the bottom right corner
    of the network view are a set of network view tools, mouse over for more information on each tool. 

-   The full-width **Table Panel** uses the bottom portion of the screen and displays columns of data
    for nodes and edges in your network. The table also allows you to modify the values of
    column data.

The Workspace Panel and Table Panel can be resized according to your preference or even fully collapsed 
to maximize the screen space available for the Network View.

<a id="the_menus"> </a>
## The Menus

<a id="data"> </a>
### Data

The **Data** menu contains most basic file functionality: **Data → Open**
for opening NDEx networks and workspaces; **Data → Save** for saving networks and workspaces to NDEx; 
**Data → Import** for importing data such as networks and tables; and **Data → Export** for exporting data. 

Updated Data menu image goes here (quick_tour_3.pmg)

![](_static/images/Quick_Tour/quick_tour_3.png)

<a id="edit"> </a>
### Edit

The **Edit** menu allows to delete the nodes and/or edges of a selected subset of
the network.

Other editing options will be added in future releases.

<a id="layout"> </a>
### Layout

The **Layout** menu lists a variety of layout algorithms that can easily be applied to your network with just 1 click.
Choosing any of these options will lay the network out using the default settings for that algorithm. In this version of Cytoscape Web, the available options are:
-    DAGRE
-    Force-directed
-    Radial
-    Grid
-    Circle
-    COSE
-    Concentric
-    Cosmos

Choosing **Layout → Settings...** will open a dialog window where you can select each available layout algorithm to modify its parameters. You can also specify a default algorithm to use via the **Apply Default Layout** feature available in the Network View Window.
    
![](_static/images/Quick_Tour/quick_tour_4.png)

<a id="analysis"> </a>
### Analysis

The **Analysis** menu contains features to analyze your networks.

**Run LLM Query** will analize a list of genes and provide details about their involvement in known biological processes. In this version of Cytoscape Web, the analysis is only available if your network is a hierarchical structure where its nodes are "communities" of genes. In future releases, the analysis will be extended to non-hierarchical networks too. Other analysis tools will also be added in future releases.

Choosing **Analysis → LLM Query Options** lets you select the LLM used for analysis, add your own API key as well as review and choose the prompt template to use. Currently, the available LLMs are OpenAi's *gpt-3.5-turbo* and *gpt-4-1106-preview*.

![](_static/images/Quick_Tour/quick_tour_5.png)

***NOTE: the **Run LLM Query** leverages commercially available LLMs and is therefore a paid feature. In order to use it, you must provide an API key linked to your OpenAI account so you can be billed based on usage. The API key is stored locally in your browser's cache, encrypted and only trasmitted to OpenAI via secure hyper text transfer protocol (https)***.

<a id="tools"> </a>
### Tools

The **Tools** menu contains advanced features like **[Network Merge](Merge.html#merge)**. Other advanced feature tools will be added in future releases. 

<a id="apps"> </a>
### Apps >> NEEDS UPDATE

The **Apps** menu gives you access to the **App Manager** (**Apps → App
Manager**) for managing (install/update/delete) your apps and may have
options added by apps that have been installed. Depending on which apps
are loaded, the apps that you see may be different than what appear
here. The below picture shows a Cytoscape installation without installed
apps.

![](_static/images/Quick_Tour/AppsMenu.png)

**Note: A list of available Cytoscape apps with descriptions is available online at: [http://apps.cytoscape.org](http://apps.cytoscape.org)**

In previous versions of Cytoscape, apps were called plugins and served a
similar function.


<a id="help"> </a>
### Help

The **Help** menu allows you to easily access basic information **About Cytoscape Web**, this **Manual**, the **Code Repository** and **Bug Report** interface. The **Citation** option displays the literature citation for
Cytoscape Web.

>> Updated Help Menu image goes here >>

![](_static/images/Quick_Tour/quick_tour_6.png)


<a id="network_management"> </a>
## Network Management

<a id="workspace"> </a>
### Workspace

In Cytoscape Web, the **Workspace** replaces the **Session** concept that Cytoscape desktop application users are familiar with. 
The Cytoscape Web **Workspace** allows multiple networks to be loaded, but only one can be displayed at any given time. 

An example where a number of networks have been loaded is shown below:

![](_static/images/Quick_Tour/quick_tour_7.png)

The **Workspace Panel** (Workspace tab in Control Panel) shows all the networks that are
loaded. Clicking on a network here will dispay the network in the **Network View** window.
Each network has a name, size (number of nodes and edges) and a label that identifies its provenance. 

If a network is loaded from NDEx, a ![](_static/images/Quick_Tour/ndex_labelx24.png) label is displayed in front of its name.
If the network is loaded from a file, the network name is the name of the file and a ![](_static/images/Quick_Tour/local_labelx24.png) label is displayed instead.

Some networks are very large and cannot be loaded in Cytoscape Web due to limitations in web browser's performance and capabilities:
-    For NDEx networks, the network size must be less than *500 Mb* and/or the nodes and edges count less than *20,000 elements*.
-    For networks imported from file, the text file must be less than *5 Mb*.

<a id="layout_tools"> </a>
### Layout Tools

The **Layout Tools** panel is available below the **Workspace Panel**; this panel is collapsed by default and can be expanded
by clicking it. 

![](_static/images/Quick_Tour/quick_tour_9.png)

The **Layout Tools** let you adjust the *height* and *width* of the entire network independently or together (both) by using an intuitive slider. The *circular arrow* button on the right resets the slider position >>and the original network view.>> ????

<a id="the_network_overview_window"> </a>
### Network View

This is where your selected network is displayed and you can interact with it. At the bottom right corner of the **Network View** Window is a set of 4 network view tools as shown below:

-   ![](_static/images/Quick_Tour/apply_default_layout.png) **Apply Default Layout** will apply the default network layout (*G6: gForce*) or whatever other layout you have specified as "default" in the **[Layout Settings](Quick_Tour_of_Cytoscape.html#layout)**.

-   ![](_static/images/Quick_Tour/fit_to_screen.png) **Fit Network to Window** will resize the current network and fit it to the **Network View** window.

-   ![](_static/images/Quick_Tour/open_in_cytoscape.png) **Open in Cytoscape** will open the current network in the Cytoscape desktop application if it is already running on your computer (default port: 1234).

-   ![](_static/images/Quick_Tour/share_url.png) **Share Network** copies the URL of the current network to your computer's clipboard so you can paste it in emails and other documents.


<a id="cell_view"> </a>
### Cell View

If the currently selected network is a *hierarchy*, the interface will display the **Cell View** tab at the top of the **Network View** window. Click it to switch to the **Cell View**, also know as circle packing view:

![](_static/images/Quick_Tour/quick_tour_10.png)

**Cell View** displays the network in systems and sub-systems (circles) that might or might not be nested.
A good comparison is to think about thisrepresentation as Matryoshka dolls.

Single click a system to select it, or double click to zoom in and see the next-level sub-systems.

When a system is selected, you can explore the underlying interaction network by opening the sliding **Sub-network Viewer** panel using the ![](_static/images/Quick_Tour/quick_tour_10.png) button in the top right corner of the **Cell View** window:

![](_static/images/Quick_Tour/quick_tour_11.png)

>> TO BE CONTINUED WHEN THE FEATURE WORKS !!! >>


For information on user privacy, see the **[Cytoscape Web Privacy
Policy](Cytoscape_Privacy_Policy.html#cytoscape_web_privacy_policy)**.
