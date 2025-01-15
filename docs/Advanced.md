Advanced Features and Troubleshooting
=========================
<a id="advanced_features"> </a>

## URL Query Parameter

Cytoscape Web's ```import``` URL parameter provides an easy way for web applications and third-party tools to use Cytoscape Web to inspect and process the result from their workflows as long as the result can be served on a REST endpoint in CX2 format. 

For example, if my Jupyter notebook generates a CX2 network and the file is available at:

```
http://localhost:8080/xyz/mytempresult.cx2
```
using the URL **https://web.cytoscape.org/?import=http://localhost:8080/xyz/mytempresult.cx2** will open the CX2 network in Cytoscape Web in the user's default web browser.

## Troubleshooting Cytoscape Web

1. Clear browser's cache
2. Hard reload
3. Last resort: Clear local db (factory resets Cy-web)


