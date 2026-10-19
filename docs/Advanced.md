Advanced Features and Troubleshooting
=========================
<a id="advanced_features"> </a>

## URL Query Parameters
<a id="url_parameters"></a>

You can control what Cytoscape Web does when it opens by adding parameters to its address (URL). This lets other web applications and tools send networks to Cytoscape Web, and lets you share a network so that it opens the way you set it up.

All parameters are applied once, when Cytoscape Web opens, and are then removed from the browser's address bar.

<a id="import_parameter"></a>
### Opening a CX2 File from a URL

The ```import``` parameter provides an easy way for web applications and third-party tools to use Cytoscape Web to inspect the results of their workflows, as long as the result can be served on a REST endpoint in CX2 format. 

For example, if my Jupyter notebook generates a CX2 network and the file is available at

```
http://localhost:8080/xyz/mytempresult.cx2
```

using the following URL

```
https://web.cytoscape.org/?import=http://localhost:8080/xyz/mytempresult.cx2
```

will open the CX2 network in Cytoscape Web in the user's default web browser.

The file must be in CX2 format and no larger than 10 MB. To import several files, repeat the parameter (```?import=<first URL>&import=<second URL>```). The last file imported becomes the current network.

<a id="install_app_parameter"></a>
### Installing Apps from a URL

The ```installApp``` parameter installs an App or a Service App, after asking the user to confirm. See [Installing Apps from a Link](Extending.md#install_links).

<a id="network_links"></a>
### Linking to an NDEx Network

An address of the form

```
https://web.cytoscape.org/0/networks/<NDEx network UUID>
```

opens the NDEx network with that UUID, adding it to your workspace if it isn't there yet. This is the kind of address that the **Share Network** button copies (see [Network View Panel](Quick_Tour_of_Cytoscape.md#network_view)).

<a id="display_parameters"></a>
### Display Parameters

Additional URL parameters specify how the interface is set up when the network opens: for example, whether the Table Panel is open, which of its tabs is active, and which nodes and edges are selected. Senders can use them to share a network with collaborators exactly as they want it displayed.

The resulting URL not only gives immediate interactive access to the network in the recipient's Cytoscape Web workspace, but also preserves the interface settings that the sender defined. The **Share Network** button adds these parameters for you, based on how your window is set up when you click it. It includes the selection if 1 to 300 nodes and edges are selected.

For example, pasting the following URL in a web browser

```
https://web.cytoscape.org/0/networks/9a8f5326-aa6e-11ea-aaef-0ac135e8bacf?selectednodes=41536+41580+41605+41606+41719&selectededges=e42257+e42161+e42160+e42117&left=open&right=closed&bottom=open&activeTableBrowserTab=2
```

will open a network in Cytoscape Web that has 5 nodes and 4 edges selected in the "Homologous Recombination" cluster on the left side of the graphic rendering, an expanded Table Panel and the active Table Panel tab set to "Network". 

Below is the list of all the display parameters available:

```selectednodes``` >> The selected nodes, as a list of node IDs separated by spaces (written as ```+``` in a URL). Node IDs are shown in the **ID** column of the Table Panel.

```selectededges``` >> The selected edges, as a list of edge IDs separated by spaces. Edge IDs are shown in the **ID** column of the Table Panel's **Edges** tab and start with ```e```.

```left``` >> The state of the Control Panel on the left (the Workspace, Style and Filter tabs): ```open```, ```closed``` or ```hidden```.

```right``` >> The state of the panel on the right (the Sub Network Viewer and panels added by Apps): ```open```, ```closed``` or ```hidden```.

```bottom``` >> The state of the Table Panel: ```open```, ```closed``` or ```hidden```.

```activeTableBrowserTab``` >> The active tab in the Table Panel: ```0``` for Nodes, ```1``` for Edges, or ```2``` for Network.

The following parameters apply to [hierarchical networks](Quick_Tour_of_Cytoscape.md#cell_view):

```activeNetworkViewTab``` >> The active network view tab: ```0``` for Tree View, ```1``` for Cell View.

```activeNetworkView``` >> The ID of the network view to make active, such as the subnetwork shown in the Sub Network Viewer.

```selectedSubnetworkNodes```, ```selectedSubnetworkEdges``` >> The selected nodes and edges in the subnetwork, as lists of IDs separated by spaces.

```filterFor```, ```filterBy```, ```filterRange``` >> A filter to apply to the subnetwork: ```filterFor``` is ```node``` or ```edge```, ```filterBy``` is the name of the column to filter on, and ```filterRange``` is a comma-separated list of the values to show.


## Troubleshooting Cytoscape Web
<a id="troubleshooting"></a>

Web applications are complex software, and sometimes they get into an abnormal state that prevents normal operation; Cytoscape Web is no exception. If Cytoscape Web stops working normally, try the following measures, in this order.

The first measure consists in performing a **hard reload** of the Cytoscape Web application. This can be achieved by holding down the **Shift** key on your keyboard and clicking the browser's reload icon ![](_static/images/Advanced/reload_icon.png). A hard reload bypasses the browser's cache and can help restore a web application's normal state by refreshing outdated files in the cache.

The second measure consists in **clearing the browser's cache** entirely and then reloading Cytoscape Web. [THIS PAGE](https://www.wikihow.com/Clear-Your-Browser%27s-Cache) describes how to clear the cache in different web browsers and platforms. Clear only the cache: if you also clear cookies and site data for Cytoscape Web, your local workspace is deleted.

The third and last measure involves **clearing the local database**. This feature is available in the Cytoscape Web main menu under **Data → Clear Local Database** and should only be used as a last resort. You can think about this as a "factory reset", that will completely erase and restore Cytoscape Web to a clean slate. Cytoscape Web asks you to confirm in the **Reset Local Workspace (for developers)** dialog; click **Reset Workspace (cannot be undone)** to continue. This deletes all the networks in your local workspace, your installed Apps and Service Apps, and your Workspace Styles. Networks saved to NDEx are not affected, so save anything you want to keep to NDEx first. If Cytoscape Web is open in other browser tabs, they reload too.

<a id="startup_problems"></a>
### Problems When Cytoscape Web Starts

If Cytoscape Web can't open your local workspace, it shows one of these messages instead of the usual window:

-   **Error: An unexpected error has occurred.** Click **Reset Workspace and Reload Cytoscape** to clear the local database (as described above) and start again.

-   **This browser has a newer Cytoscape Web database.** This can happen after you've used a newer version of Cytoscape Web in the same browser. To continue, click **Reset Workspace and Reload Cytoscape**, then **Confirm — permanently delete**. This deletes the local workspace in this browser, including every network in it. Networks saved to NDEx are not affected.

-   **Cytoscape Web cannot access local storage.** Your browser window doesn't allow Cytoscape Web to store data, which is common in private or incognito windows. Open Cytoscape Web in a normal browser window.

<a id="tab_sync_problems"></a>
### Several Browser Tabs

If you have Cytoscape Web open in several browser tabs, a tab may show the message *This tab is no longer receiving changes made in your other Cytoscape Web tabs*. Reload that tab to reconnect it; otherwise, the changes you make there may overwrite changes made in your other tabs. See [Working in Several Browser Tabs](Quick_Tour_of_Cytoscape.md#multiple_tabs).

<a id="report_a_bug"></a>
### Reporting a Bug

Cytoscape Web is still in active development and may contain unidentified bugs. Should you find one, please report it by choosing **Help → Report a Bug** in the Cytoscape Web main menu and clicking **Click here to report a bug**. It helps us if you include the version information shown in **Help → About Cytoscape Web**; click **Copy** there to copy it.

Cytoscape Web also sends crash reports automatically to help us fix problems. See the [Privacy Policy](Cytoscape_Privacy_Policy.md) for details.
