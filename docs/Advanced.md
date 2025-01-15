Advanced Features and Troubleshooting
=========================
<a id="advanced_features"> </a>

## URL Query Parameters

Cytoscape Web's ```import``` URL parameter provides an easy way for web applications and third-party tools to use Cytoscape Web to inspect and process the result from their workflows as long as the result can be served on a REST endpoint in CX2 format. 

For example, if my Jupyter notebook generates a CX2 network and the file is available at *http://localhost:8080/xyz/mytempresult.cx2*,

using the URL **https://web.cytoscape.org/?import=http://localhost:8080/xyz/mytempresult.cx2** will open the CX2 network in Cytoscape Web in the user's default web browser.

Additional URL parameters allow to specify the behavior of some of the interface components. These parameters let users customize the way a network is displayed in Cytoscape Web prior to sharing it with collaborators, such as a collapsed or expanded table panel, the active table panel’s tab and the node/edge selection in the network’s graphic rendering.

The resulting URL not only allows immediate interactive access to the network in the recipient’s Cytoscape Web workspace, but also preserves some of the interface settings that the sender defined, 

For example, the following URL:

**https://web.cytoscape.org/0/networks/9a8f5326-aa6e-11ea-aaef-0ac135e8bacf?selectednodes=41536+41580+41605+41606+41719&selectededges=e42257+e42161+e42160+e42117&left=open&right=closed&bottom=open&activeTableBrowserTab=2**

will open a network in Cytoscape web that has 5 nodes and 4 edges selected in the "Homologous Recombination" cluster on the left side of the graphic rendering, an expanded table panel and the active table panel tab set to "Network". 

Below is the list of all the additional query parameters available:

```selectednodes``` >> Defines the selected nodes

```selectededges``` >> Defines the selected edges

```left``` >> Defines the state of Workspace Panel (open or closed)

```right``` >> Defines the state of Sub Network View Panel (open or closed)

```bottom``` >> Defines the state of Table Panel (open or closed)

```activeTableBrowserTab``` >> Defines the active tab in the table panel (0= Nodes, 1= Edges or 2= Network)


## Troubleshooting Cytoscape Web >> TO DO

1. Clear browser's cache
2. Hard reload
3. Last resort: Clear local db (factory resets Cy-web)


