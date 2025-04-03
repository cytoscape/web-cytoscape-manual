Introduction
===============

<a id='introduction'> </a>

Cytoscape has been a leading platform for visualization and analysis of complex networks since 2003. To complement the highly successful desktop application, we introduce [Cytoscape Web](https://web.cytoscape.org), a web-based version of Cytoscape that supports modern computing environments without the need for software installation.
 
Cytoscape Web delivers efficient network analysis directly in the browser. Its new UI-centric app framework allows for the seamless migration of existing Cytoscape applications and enables *de novo* development of Service Apps in any programming language, thus enhancing access and flexibility.
 
It simplifies data sharing and distribution. Networks can be stored in the [Network Data Exchange (NDEx)](https://www.ndexbio.org) and shared among researchers via unique URLs rather than attaching large session files to email messages.
 
Cytoscape Web expands visualization capabilities by supporting multiple rendering engines such as the new "Cell View", and allows analysis of "communities" of genes using a variety of Large Language Models (LLM) thanks to the [Gene Set AI (GSAI)](https://idekerlab.ucsd.edu/gsai/) service, recently developed by the Ideker Lab at UC San Diego and published in the January 2025 issue of Nature Methods.
 
By integrating these features, Cytoscape Web maintains the robust functionality and familiarity of its desktop counterpart while streamlining collaboration and visual analysis within a modern web environment.

Being a newer tool and still in active development, Cytoscape Web doesn't provide all the features and functionalities available in its desktop application counterpart yet. Please refer to the [Feature Comparison](https://github.com/cytoscape/cytoscape-web/wiki/Cytoscape-Web-vs-Desktop-Feature-Comparison) table for more information. 

<a id="requirements"> </a>
## Software Requirements

We recommend that you always update your preferred web browser to the latest version whenever possible. Cytoscape Web fully supports the following browsers:

   - Google Chrome
   - Mozilla Firefox
   - Microsoft Edge

While we don't discourage the use of alternative web browsers, we cannot guarantee that all features will be available and functioning as intended. For example, if using the Brave browser, you must disable the **Brave Shield** otherwise the **Open in Cytoscape** feature in Cytoscape Web will not work.

For the **Open in Cytoscape** feature to work properly, you also need [Cytoscape 3.10 or higher](https://cytoscape.org/download.html) installed and running on your machine, and the **cx support** core-app updated to the latest version available.



