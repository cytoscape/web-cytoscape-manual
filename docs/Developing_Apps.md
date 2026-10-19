Developing Apps for Cytoscape Web
==================================
<a id="developing_apps"> </a>

Anyone can build apps that add new features to Cytoscape Web. This page helps you choose which kind of app to build and points you to the developer documentation. The developer documentation lives on GitHub, where it is updated together with Cytoscape Web; this manual doesn't repeat it.

To learn how users find, install and run apps, see **[Extending Cytoscape Web](Extending.md)**.

<a id="choose_app_type"></a>
## Choose the Kind of App

Cytoscape Web supports two kinds of apps:

<table cellspacing="0" style="table-layout: fixed; width: 700px">
<colgroup> <col style="width:140px"> <col style="width:280px"> <col style="width:280px"> </colgroup>
<tbody>
<tr> <th></th>                                 <th>App</th>                                                                 <th>Service App</th> </tr>
<tr> <th class="specalt">Runs</th>             <td class="alt">In the user's web browser, inside Cytoscape Web</td>       <td class="alt">On your own web server</td> </tr>
<tr> <th class="spec">Written in</th>          <td>JavaScript or TypeScript</td>                                              <td>Any programming language</td> </tr>
<tr> <th class="specalt">What it can do</th>   <td class="alt">Add panels, menu items and context menu items; read and change networks, tables, styles and layouts through the App API</td> <td class="alt">Receive network or table data from Cytoscape Web, process it, and return results that Cytoscape Web applies (new columns, networks, layouts, selections and more)</td> </tr>
<tr> <th class="spec">Good for</th>            <td>Interactive tools and new user interface</td>                             <td>Analyses that need server-side code, large libraries or data</td> </tr>
<tr> <th class="specalt">Start here</th>       <td class="alt"><a href="https://github.com/cytoscape/cytoscape-web-app-examples#readme">Cytoscape Web app examples</a></td> <td class="alt"><a href="https://github.com/cytoscape/cytoscape-web/wiki/Specification-for-Service-App-in-Cytoscape-Web-(draft-v2)">Service App specification</a></td> </tr>
</tbody>
</table>
<br>

***NOTE: The App API used by Apps is a developer preview and may change between releases. Check the developer documentation for its current status.***

<a id="developer_resources"></a>
## Developer Resources

All developer documentation is on GitHub:

-   **[Cytoscape Web Developer Hub](https://github.com/cytoscape/cytoscape-web/wiki/Cytoscape-Web-Developer-Tutorial)**: the starting point for all developer documentation, for both kinds of apps and for working on Cytoscape Web itself.

-   **[Build an App](https://github.com/cytoscape/cytoscape-web-app-examples#readme)**: a quick start that creates a new app project for you, step-by-step guides, and example apps.

-   **[App API reference](https://github.com/cytoscape/cytoscape-web/tree/development/packages/api-types#readme)**: the programming interface available to Apps.

-   **[Build a Service App](<https://github.com/cytoscape/cytoscape-web/wiki/Specification-for-Service-App-in-Cytoscape-Web-(draft-v2)>)**: the specification a Service App's web service must follow, with example services.

-   **[Contribute to Cytoscape Web](https://github.com/cytoscape/cytoscape-web/blob/development/docs/guides/README.md)**: the guide for developers who want to work on Cytoscape Web itself.

You can also open the Developer Hub from Cytoscape Web, with **Help → Developer → Developer's Guide**.

<a id="try_your_app"></a>
## Try Your App in Cytoscape Web

While you develop, you can install your app in Cytoscape Web like any other app:

-   Add an App by its manifest URL, or a Service App by its URL, in the App Manager. See [Install an App from a URL](Extending.md#install_from_url) and [Service Apps](Extending.md#service_apps).
-   Share an install link with testers. See [Installing Apps from a Link](Extending.md#install_links).

<a id="publish_your_app"></a>
## Publish Your App

When your app is ready, submit it to the [Cytoscape App Store](https://apps.cytoscape.org/submit/select_platform) so that users can find and install it. Choose **Cytoscape Web - Bundle** for an App, or **Cytoscape Web - Service App URL** for a Service App.

<a id="get_help"></a>
## Get Help

-   Ask questions and report problems with the App API or the developer documentation on the [Cytoscape Web issue tracker](https://github.com/cytoscape/cytoscape-web/issues).
-   For other questions, [contact the Cytoscape team](https://cytoscape.atlassian.net/servicedesk/customer/portal/1/group/1/create/7).
