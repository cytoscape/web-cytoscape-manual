Extending Cytoscape Web
=========================
<a id="extending_cytoscape_web"> </a>

**Apps** add new features to Cytoscape Web or extend existing ones. Cytoscape Web supports two kinds of apps:

-   **Apps** run inside Cytoscape Web, in your web browser. An app can add its own panels, menu items and context menu items, and can work directly with your networks, tables and styles.

-   **Service Apps** are web services that run on a remote server. When you run a Service App, Cytoscape Web sends it data from your current network (for example, a column of gene names), and then applies the result the service sends back, such as new table columns, a new network, a new layout or a new selection.

You find apps in the **[App Store](Extending.md#app_store)** and manage them in the **[App Manager](Extending.md#app_manager)** (**Apps → Manage Apps...**).

If you use Cytoscape Desktop, these work much like its [App Store and App Manager](https://manual.cytoscape.org/en/stable/App_Store.html). However, apps are built for one platform: Cytoscape Desktop apps can't be installed in Cytoscape Web, and Cytoscape Web apps can't be installed in Cytoscape Desktop.

If you want to build your own app, see **[Developing Apps](Developing_Apps.md)**.

***NOTE: Only install apps from sources you trust. Apps run inside Cytoscape Web with the same access to your networks as Cytoscape Web itself, and a Service App receives the network data you send it. Service Apps that work with NDEx can also receive your NDEx sign-in, so they can read or save networks in your NDEx account.***

<a id="app_store"></a>
## The App Store

The [Cytoscape App Store](https://apps.cytoscape.org) lists apps for both Cytoscape Desktop and Cytoscape Web. To see only the apps that work in Cytoscape Web, browse:

-   [Cytoscape Web Apps](https://apps.cytoscape.org/apps/platform/web/)
-   [Cytoscape Web Service Apps](https://apps.cytoscape.org/apps/platform/service/)

To install an app from the App Store:

1.  Open the app's page in the App Store.

2.  Click **Install in Cytoscape Web** (for an App) or **Open in Cytoscape Web** (for a Service App). Cytoscape Web opens with an install link for the app.

3.  Cytoscape Web shows the **Install into this workspace?** dialog. Review the app's name, version, author and address, and click **Install**. See [Installing Apps from a Link](Extending.md#install_links) for details.

Each app's page also shows its **Manifest URL** (Apps) or **Service URL** (Service Apps). You can copy that address and add the app in the App Manager instead, as described in [Install an App from a URL](Extending.md#install_from_url) and [Service Apps](Extending.md#service_apps).

<a id="install_links"></a>
## Installing Apps from a Link

An install link opens Cytoscape Web and installs one or more apps. The App Store's install buttons use these links, and app developers can share them too. An install link looks like this:

```
https://web.cytoscape.org/?installApp=<address of the app>
```

The address of the app is an App's manifest URL or a Service App's URL. A link can contain several `installApp` parameters to install several apps at once.

When you open an install link, Cytoscape Web asks you to confirm in the **Install into this workspace?** dialog. Each app is listed with an **App** or **Service** label, its version, author, description and address. Click **Install** to install all of them, or **Cancel** to install none.

Installed Apps are turned on right away, and a message such as *Added Update tables example* confirms each installation. If an app can't be installed, a message explains why.

<a id="app_manager"></a>
## The App Manager

Choose **Apps → Manage Apps...** to open the App Manager. It has two tabs, **Apps** and **Service Apps**. At the bottom, **Refresh** reloads the list of available apps and **Close** closes the App Manager.

<a id="apps"> </a>
### Apps

The **Apps** tab lists the Apps available in Cytoscape Web and the Apps you have installed. Each App shows its name, version and description, and may have one of these labels:

-   **active**: the App is turned on and running.
-   **failed**: the App couldn't be loaded or started. The reason is shown in red below the App. If the App loaded but failed to start, a **Retry** button lets you try again.
-   **App Store**: you installed this App, from the App Store, from an install link or by URL.
-   **Snapshot**: the App was restored from a workspace you opened from NDEx (see [Apps and Workspaces](Extending.md#apps_and_workspaces)).
-   **orphan**: the App is still recorded in your workspace but is no longer available. Click the trash icon to remove it.

<a id="enable_disable_apps"></a>
#### Enable/Disable Apps

Use the switch next to an App to turn it on or off. When an App is on, its menu items (usually in the **Apps** menu), panels (usually on the right side of the window) and context menu items appear in Cytoscape Web. When it's off, they're removed.

<a id="uninstall_apps"></a>
#### Uninstall Apps

To uninstall an App you installed, click its **⋮** (**More options**) button, choose **Uninstall** and confirm. The App is removed from your workspace. Apps that come with Cytoscape Web, rather than being installed by you, can be turned off but not uninstalled.

<a id="install_from_url"></a>
#### Install an App from a URL

To install an App from its address:

1.  Paste the App's manifest URL into the **Single-entry manifest URL** field under **Install from URL**. You can find this address on the App's page in the App Store, as **Manifest URL**.
2.  Click **Install**.
3.  The App is added to the list, turned off. Use its switch to turn it on.

This field only accepts App manifest URLs. To add a Service App, use the [Service Apps](Extending.md#service_apps) tab.

#### Advanced

Click **Advanced** to show the **Manifest Source** settings. These let developers and advanced users replace the list of available Apps with their own manifest, by URL (**Custom manifest URL**, then **Apply**) or by uploading a manifest file. Click the **✕** button next to the current source to return to the default. Only use manifests from sources you trust.

<a id="core_apps"></a>
#### Core Apps

In Cytoscape Desktop, [core apps](https://manual.cytoscape.org/en/stable/App_Store.html#core-apps) provide essential features and are always installed. Cytoscape Web doesn't include core apps yet, so the **Apps** tab lists only the Apps you install (or shows *No apps available in catalog.*). A set of core apps is planned for a future release, and they will be listed here.

<!-- Placeholder: add the list of Cytoscape Web core apps here when they are released. -->

<a id="service_apps"> </a>
### Service Apps

The **Service Apps** tab lists the Service Apps you have registered. For each one, you see its name, its **Endpoint** (the service's address) and a description.

To add a Service App:

1.  Paste its URL into the **Enter new external service URL** field. You can find this address on the Service App's page in the App Store, as **Service URL**.
2.  Click **Add**. (**Clear** empties the field.)

For example, adding this URL:

```
https://cd.ndexbio.org/cy/cytocontainer/v1/updatetablesexample
```

registers the **Update tables example** Service App, which you can then run from **Tools → Example Service App → Update tables example**.

Click the refresh icon next to a Service App to reload its definition, for example after the service has been updated. **Refresh all** does this for every registered Service App. Click the trash icon to remove a Service App.

If you haven't registered any Service Apps, the tab shows *No services are registered yet* and an **Add Example Services** button, which registers the [example Service Apps](Extending.md#example_service_apps) listed below.

<a id="using_service_apps"></a>
## Using Service Apps

Each Service App decides where its menu item appears. It can be in any of the main menus (**Data**, **Edit**, **Layout**, **Analysis**, **Tools**, **Apps** or **Help**), often in a submenu. If a Service App doesn't name a menu, it appears in the **Apps** menu. Hover over a Service App's menu item to see where it's hosted, its version and its author.

When you choose a Service App's menu item, a dialog opens with the app's name and description, and, if the service needs them:

-   **Input Columns**: the columns whose data will be sent to the service. Only columns of the data type the service needs are listed. Choose **(none)** to leave an optional column out.
-   **Parameters**: settings for the service.

Click **Submit** to run the service. If **Submit** is disabled, hover over it to see why, for example when no network is open. When the service finishes, Cytoscape Web applies its results to your network. If the service reports an error, an *Oops! Something went wrong...* dialog shows the service's error message.

<a id="example_service_apps"></a>
### Example Service Apps

The **Add Example Services** button in the App Manager registers these Service Apps:

**1. Update tables example**

A simple example that adds or updates a column in the node table (or the edge table). Run it from **Tools → Example Service App → Update tables example**.
```
https://cd.ndexbio.org/cy/cytocontainer/v1/updatetablesexample
```

**2. IQuery Enrichment**

Analyzes gene sets against NDEx IQuery to retrieve pathways ranked by similarity-based matches. **Requires** a network with at least one column in the node table that contains a whitespace- or comma-separated list of gene symbols. Run it from **Apps → Run Functional Enrichment → IQuery**.
```
https://cd.ndexbio.org/cy/cytocontainer/v1/iqueryenrichment
```

**3. g:Profiler Enrichment**

Analyzes gene sets against biological databases to identify statistically significant pathways. **Requires** a network with at least one column in the node table that contains a whitespace- or comma-separated list of gene symbols. Run it from **Apps → Run Functional Enrichment → gProfiler**.
```
https://cd.ndexbio.org/cy/cytocontainer/v1/gprofilerenrichment
```

<a id="apps_and_workspaces"></a>
## Apps and Workspaces

Your installed Apps and registered Service Apps belong to your [workspace](Quick_Tour_of_Cytoscape.md#workspace_tab):

-   **Data → Save Workspace** and **Data → Save Workspace As...** save your installed Apps (and whether each one is turned on) and your registered Service Apps to NDEx, together with your networks.

-   **Data → Open Workspace from NDEx...** replaces your current Apps and Service Apps with the ones saved in that workspace. Restored Apps are labeled **Snapshot**. An App that isn't allowed in this copy of Cytoscape Web, or doesn't work with this version, is restored turned off.

-   **Data → Clear Local Database** removes all installed Apps and registered Service Apps. To keep them, save your workspace to NDEx first. For more details, see [Save to NDEx](Creating_Networks.md#save_to_NDEx).

<a id="developers"></a>
## For Developers

<a id="writing_apps"></a>
<a id="writing_service_apps"></a>

To learn how to build Apps and Service Apps for Cytoscape Web, see **[Developing Apps](Developing_Apps.md)**.
