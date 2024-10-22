# Cytoscape Web
This project contains the complete user manual for Cytoscape  Web. 
There are versions of the manual based on specific versions of Cytoscape. 
There is also a "stable" that links to the latest Cytoscape version. 
A "latest" link refers to the master branch. 
The versions are automatically built at ReadTheDocs.org from 
[tags of this repo](https://github.com/cytoscape/web-cytoscape-manual/tags), for example 1.0.0. 

Latest Cytoscape Web version link: TO BE ADDED

Version-specific link: TO BE ADDED

Master branch version: TO BE ADDED

## Building the Manual locally

* Requirements

   * Python 3.9+
   * Install packages found in ``docs/requirements.txt``

Clone repo and run the following commands:

```bash
git clone https://github.com/cytoscape/web-cytoscape-manual.git
cd web-cytoscape-manual
make docs
```
The above should launch the default browser with the documentation, but if not the html
can be found under ``docs/_build/html``


## Rebuilding the Manual

TO BE ADDED

### Pre-release checks

1. Review updates to docs and images at GitHub.
2. Add any new manual sections to index.rst and update Copyright year (if applicable).
3. Double-check the manual at ReadTheDocs here: TO BE ADDED

:warning: When you're checking a new version of the manual, be sure to clear your browser's cache ... otherwise, you'll be looking at 
an obsolete version, which will quickly become confusing.

### Process for updating the manual for a new CS release ###

NOT WORKING YET

1. Update version number and Copyright year (if applicable) in conf.py
2. [Create a new release](https://github.com/cytoscape/web-cytoscape-manual/releases) with the relevant release number, for example 1.0.0. **AUTO BUILD NOT WORKING YET** **This will automatically trigger a build at ReadTheDocs for this release.** Leave "binary attachments" emtpy. Do not added the "v" in front of the version number as suggested by GitHub (i.e., use 1.0.0 instead of v1.0.0). 
3. After 3-10 minutes, verify that the version-specific link works, for example: TO BE ADDED

### Troubleshooting ###

If a problem with a new tagged release (and the corresponding ReadTheDocs build) is discovered, the tag at GitHub has to both be removed and recreated in order to fix the ReadTheDocs build. 
1. Delete the relevant release via the github.com UI. Go to tags (https://github.com/cytoscape/web-cytoscape-manual/tags), click on the title of the tag you want to delete, then click the "Delete" button in upper right. 
2. Log into ReadTheDocs. Under "Builds", select the appropriate build number, for example 1.0.0, in the drop-down and then click the "Build" button. 

Note: If the build you are looking for does not appear in the drop-down even though it should be there (i.e. there is a tag at GitHub), it is possible that the build is just "inactive". Go to the "Versions" page and scroll down to the list at the bottom. Locate the build there, for example 3.8.1, and click "Activate". 

## Editing the Manual
To edit manual text, you must first check out this repository and use a text editor on your workstation. For small edits, you can use GitHub's native Markdown editor.

* All document components are in the "docs" directory. Each chapter is contained in its own file, and the files are assembled as a complete document by naming them in the "docs/index.rst" file.
* Images are stored in the "docs/_static/images" directory, organized into subdirectories by chapter. For high quality images, vector graphic files produce best results (e.g., .png).
* Simple tables can be represented in Markdown, but high quality formatting requires direct HTML coding. By convention, we encode tables as HTML-tagged data, but do not specify visual attributes and layout inline. Instead, we use preset table styles contained in "docs/_static/css" for formatting -- we do not use Markdown's table formatting. Note that additional CSS files can be added, but must be accounted for in "_templates/layout.html" and "conf.py". Note that while the tables appear in the HTML document, they do not appear in the PDF version -- we're working on this.

Note that the GitHub file viewer displays Markdown files reasonably well. However, it only approximates the look of tables created via HTML. For an accurate view of a table, you must look at a document rendered by ReadTheDocs.

Note that a full (browsable) link to a location has the form: "TO BE ADDED" where "TO BE ADDED" is the full URL, "Launching_Cytoscape" is the root name of the file containing the target link, and "mylink" is a named section (e.g., <a name="mylink">System requirements</a>). A link between chapters in the document has the form [My Link](Launching_Cytoscape.html#mylink), and a link within the same chapter can have the form [My Link](#mylink). For intra-document references, it is best to use the Launching_Cytoscape.html#mylink form, as ReadTheDocs will append the full URL appropriate for the build (e.g., "stable", "latest", "3.3", etc).

## How the manual works

While the manual sources are maintained in GitHub, the document is actually assembled, formatted, and staged by the ReadTheDocs.org site. ReadTheDocs presents online and PDF versions.

ReadTheDocs can present versions of the manual for each Cytoscape Web release, as identified by GitHub tags. For example, given a tag of 3.3, ReadTheDocs will produce a document containing the repository files as they were for TO BE ADDED. ReadTheDocs will make a "stable" version of the manual available at TO BE ADDED ... it will resolve to the latest tagged version (ignoring beta versions such as 3.4b1). The "latest" version of the manual will be available at TO BE ADDED, and will contain all of the latest GitHub content, irrespective of tagging.

Note that for a manual under developement, "latest" has been configured as non-public (configurable in ReadTheDocs) so it isn't indexed by Google.

For anyone interested in how ReadTheDocs works, see [their documentation](https://docs.readthedocs.io/en/stable/).
