Introduction
===============

<a id='introduction'> </a>

Cytoscape has been a leading platform for visualization and analysis of complex networks since 2003. To complement the highly successful desktop application, we introduce [Cytoscape Web](https://web.cytoscape.org), a web-based version of Cytoscape that supports modern computing environments without the need for software installation.
 
Cytoscape Web delivers efficient network analysis directly in the browser. Its new UI-centric app framework allows for the seamless migration of existing Cytoscape applications and enables *de novo* development of Service Apps in any programming language, thus enhancing access and flexibility (see **[Extending Cytoscape Web](Extending.md)** and **[Developing Apps](Developing_Apps.md)**).
 
It simplifies data sharing and distribution. Networks can be stored in the [Network Data Exchange (NDEx)](https://www.ndexbio.org) and shared among researchers via unique URLs rather than attaching large session files to email messages.
 
Cytoscape Web expands visualization capabilities with new views such as the **Cell View** for hierarchical networks, and allows analysis of "communities" of genes using Large Language Models (LLM), based on the [Gene Set AI (GSAI)](https://idekerlab.ucsd.edu/gsai/) approach developed by the Ideker Lab at UC San Diego and published in the January 2025 issue of Nature Methods. You can use a commercial LLM such as OpenAI's, or run a model on your own computer.
 
By integrating these features, Cytoscape Web maintains the robust functionality and familiarity of its desktop counterpart while streamlining collaboration and visual analysis within a modern web environment.

Being a newer tool and still in active development, Cytoscape Web doesn't provide all the features and functionalities available in its desktop application counterpart yet. Please refer to the [Feature Comparison](https://github.com/cytoscape/cytoscape-web/wiki/Cytoscape-Web-vs-Desktop-Feature-Comparison) table for more information. 

If you already use Cytoscape Desktop, many features work the same way, and this manual uses the same terms as the [Cytoscape Desktop manual](https://manual.cytoscape.org/en/stable/). Where a feature is the same in both, this manual links to the Desktop manual for more background.

<a id="whats_new"> </a>
## What's New in Cytoscape Web 1.1

These are the main changes since the previous edition of this manual, which described Cytoscape Web 1.0.4. A few of them, such as pie and donut charts, creating nodes and edges, and NDEx folders, first appeared in versions 1.0.5 to 1.0.8.

-   **Getting started**: a welcome dialog and a guided tour introduce Cytoscape Web. See [Getting Started](Quick_Tour_of_Cytoscape.md#getting_started).
-   **Dark mode**: Cytoscape Web follows your computer's light or dark setting, and you can switch between them from the menu bar. See [Dark Mode](Quick_Tour_of_Cytoscape.md#dark_mode).
-   **Finding networks in NDEx**: search NDEx from the Workspace tab. The NDEx network browser shows public networks, your private networks and networks shared with you in one list, and lets you browse NDEx folders. See [Open Network from NDEx](Creating_Networks.md#open_network_from_ndex).
-   **Several styles per network**: give a network several named styles and switch between them, reuse styles across networks with Workspace Styles, and start from preset styles. See [Named Styles](Styles.md#named_styles).
-   **Charts and images on nodes**: show pie and donut charts, or images, on nodes. See [Charts and Images](Styles.md#charts_and_images).
-   **Filters**: the new **FILTER** tab selects or shows the nodes and edges that match conditions on column values, degree and topology, and reads and writes Cytoscape Desktop filter files. See [Filter](Quick_Tour_of_Cytoscape.md#filter_tab).
-   **Editing**: create nodes and edges from the **Edit** menu or by right-clicking in the network view, and duplicate networks. See [Edit](Quick_Tour_of_Cytoscape.md#edit), [Context Menus](Quick_Tour_of_Cytoscape.md#context_menus) and [Duplicate a Network](Creating_Networks.md#duplicate_network).
-   **Tables**: a right-click menu, a list editor, and node and edge IDs in the Table Panel. See [Table Panel](Node_and_Edge_Column_Data.md#table_panel).
-   **Layouts**: the new Biological Flow Layout, and a floating Layout Tools panel. See [Layout](Quick_Tour_of_Cytoscape.md#layout).
-   **LLM Query**: use a local model through Ollama, or any OpenAI-compatible service. See [Analysis](Quick_Tour_of_Cytoscape.md#analysis).
-   **Apps**: install apps from the Cytoscape App Store or from an install link. See [Extending Cytoscape Web](Extending.md).
-   **Several browser tabs**: work on the same workspace in several browser tabs at once. See [Working in Several Browser Tabs](Quick_Tour_of_Cytoscape.md#multiple_tabs).

For the complete list of changes in each release, see the [release notes](https://github.com/cytoscape/cytoscape-web/releases) on GitHub, for example those of [Cytoscape Web 1.1.0](https://github.com/cytoscape/cytoscape-web/releases/tag/v1.1.0).

<a id="requirements"> </a>
## Software Requirements

We recommend that you always update your preferred web browser to the latest version whenever possible. Cytoscape Web fully supports the following browsers:

   - Google Chrome
   - Mozilla Firefox
   - Microsoft Edge

While we don't discourage the use of alternative web browsers, we cannot guarantee that all features will be available and functioning as intended. For example:

   - In Safari, **Open Network in Cytoscape Desktop** is not available.
   - In the Brave browser, you must disable the **Brave Shield**, otherwise **Open Network in Cytoscape Desktop** will not work.

Cytoscape Web keeps your workspace in your web browser's local storage. It can't run in a browser window that blocks local storage, such as some private or incognito windows; use a normal browser window instead.

For **Open Network in Cytoscape Desktop** to work, you also need [Cytoscape Desktop 3.10.5 or later](https://cytoscape.org/download.html) installed and running on your computer, with the **CyNDEx-2** app installed and up to date. The first time you use this feature, your web browser may ask for permission for Cytoscape Web to connect to Cytoscape Desktop on your computer; allow it. See [Open Network in Cytoscape Desktop](Creating_Networks.md#open_in_cytoscape_desktop).
