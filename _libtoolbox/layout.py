#!/bin/env python3

from IPython.display import display, Markdown

def header():
    header = '''&nbsp;<a href="https://nuflo.de"><img hspace="45%" align="middle" src="../_libtoolbox/nuflo-logo-N-512x512.png" alt="logo-N" width="8%" /></a>

<center><h1>nuflo Engineering Toolbox</h1></center>

[nuflo is an engineering company](https://nuflo.de) that supports digitalization of engineering processes in fluid mechanics.

After a period of inactivity you may need to reload the webpage for the tool to work properly. If you find yourself using these tools a lot, consider a local installation. Please feel free to contact us at johannes.kneer@nuflo.de for support.

*The code for this tool can be found over at [github](https://github.com/JohK/engineering-toolbox).*  
*More interactive tools are located at [toolbox.nuflo.de](http://toolbox.nuflo.de).*


''' 
#div style='margin-top: auto;'>
    display(Markdown(header))
    
def footer(version):
    footer = '''
<div style='position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f7b500; color: #000000; text-align: center; vertical-align: middle; padding: 10px'> 
<b><a style='color: #000000;' href="https://nuflo.de/"><img src="../_libtoolbox/nuflo-logo-N-512x512.png" alt="logo-N" width="16px" />&nbsp;&nbsp;&nbsp;nuflo</a></b>&nbsp;&nbsp;&nbsp;version: {:s}</div>'''.format(version)
    display(Markdown(footer))