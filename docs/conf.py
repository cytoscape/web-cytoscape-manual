extensions = []
templates_path = ['_templates']

master_doc = 'index'

from datetime import datetime
current_year = datetime.now().year
copyright = u'2001-{}, The Cytoscape Consortium'.format(current_year)    # f'© 2001-{current_year}, The Cytoscape Consortium'
project = u'Cytoscape Web User Manual'
author = u'The Cytoscape Consortium'

version = '1.0.x'
release = '1.0.x'
language = None

rst_epilog = f"""
.. |index_copyright| replace:: © Copyright 2001-{current_year}, The Cytoscape Consortium.
"""

exclude_patterns = ['_build']
pygments_style = 'sphinx'

import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

def setup(app):
  app.add_css_file( "css/tables.css" )

# from http://stackoverflow.com/questions/32079200/how-do-i-set-up-custom-styles-for-restructuredtext-sphinx-readthedocs-etc/32079202#32079202

html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
html_show_sourcelink = True
htmlhelp_basename = 'Testdoc'
html_logo = '_static/images/cytoscape3-icon-trans-128x128.png'
html_favicon = '_static/images/cytoscape3-icon.ico'

extensions = ['myst_parser',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.viewcode',
              'sphinx_copybutton']


latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

latex_documents = [
  (master_doc, 'Test.tex', u'Cytoscape Web User Manual',
   u'The Cytoscape Consortium', 'manual'),
]

man_pages = [
    (master_doc, 'test', u'Cytoscape Web User Manual',
     [author], 1)
]

texinfo_documents = [
  (master_doc, 'Test', u'Cytoscape Web User Manual',
   author, 'Test', 'Cytoscape Web User Manual',
   'Miscellaneous'),
]

