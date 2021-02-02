from IPython.display import display, Markdown

__version__ = '2102'

#</div>
footer = '''
<div style='position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f7b500; color: #000000; text-align: center; vertical-align: middle; padding: 10px'> 
<b><a style='color: #000000;' href="https://nuflo.de/"><img src="../_libtoolbox/nuflo-logo-N-512x512.png" alt="logo-N" width="16px" />&nbsp;&nbsp;&nbsp;nuflo</a></b>&nbsp;&nbsp;&nbsp;version: {:s}</div>'''.format(__version__)

display(Markdown(footer))