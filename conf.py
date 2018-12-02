# import sys, os
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest',
              'sphinx.ext.intersphinx', 'sphinx.ext.todo',
              'sphinx.ext.coverage', 'sphinx.ext.imgmath',
              'sphinx.ext.ifconfig', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Grundkurs C'
copyright = '2015-2017, Bernhard Grotz'
version = '0.2.0d'
release = '0.2.0d'
# exclude_patterns = ["physik"]
language = 'de'
spelling_lang = 'de_DE'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'sphinxdoc'
html_static_path = ['_static']
html_additional_pages = {'home': 'home.html'}
htmlhelp_basename = 'Grundkurs C'
html_short_title = "Grundkurs C"

exclude_patterns = ["notes.rst", "*/notes.rst",
                    "**/notes.rst","todos.rst","README.rst"]

html_logo = "logo.png"
html_favicon = "favicon.ico"
latex_logo   = 'logo_print.png'


html_last_updated_fmt = '%d.%m.%Y'
today_fmt = '%d.%m.%Y'

html_use_smartypants = True
html_domain_indices  = False
html_use_index       = True
html_show_sourcelink = True
html_show_copyright  = False
html_show_sphinx     = False
html_search_language = 'en'
html_search_options = {'type': 'default'}

trim_footnote_reference_space = True

latex_preamble = r'''
    \usepackage[version=3]{mhchem}
    \usepackage{amsmath, units}
    \usepackage{amsfonts, amssymb}
    \usepackage{nicefrac,marvosym} 
    \setcounter{secnumdepth}{-1}
    \setlength{\headheight}{15pt}
    \setcounter{tocdepth}{2}
    \clubpenalty  = 10000 % Disable single lines at the start of a page ("Schusterjungen")
    \widowpenalty = 10000 % Disable single lines at the end   of a page ("Hurenkinder")
    \displaywidowpenalty = 10000
    \setcounter{tocdepth}{3}
    \usepackage{hyperref,url}
    \hypersetup{
    pdftitle={Grundkurs C},
    pdfsubject={Eine Einführung in die Programmiersprache C},
    pdfauthor={Bernhard Grotz},
    pdfkeywords={Programmiersprache C} {Programmierung} {C} {Lehrbuch} {Tutorial},
    }
'''

imgmath_latex_preamble = latex_preamble

latex_elements = {
    'preamble': latex_preamble,
    'classoptions': 'oneside,openany,',
    'papersize': 'a4paper,',
    'pointsize': '12pt,',
    'babel': '\\usepackage[ngerman]{babel}',
    'geometry': '\\usepackage[left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm]{geometry}',
    'fontpkg': '',
    'fncychap': ''
}


latex_documents = [
  ('index', 'grundkurs-c.tex', 'Grundkurs C',
   'Bernhard Grotz', 'manual'),
]

intersphinx_mapping = {
    'gw': ('http://grund-wissen.de/', None),
    'gwe': ('http://grund-wissen.de/elektronik', None),
    'gwm': ('http://grund-wissen.de/mathematik', None),
    'gwp': ('http://grund-wissen.de/physik', None),
    'gwl': ('http://grund-wissen.de/linux', None),
    'gwip': ('http://grund-wissen.de/informatik/python', None),
    'gwil': ('http://grund-wissen.de/informatik/latex', None),
}

