#!/bin/env python3

import ipywidgets as widgets
def quantity(description, min=0.001, max=1, step=0.00001, value=0.032):
    quantity_item_layout = widgets.Layout(display='flex', flex_flow='row')

    quantity_label = widgets.Label(description, layout=widgets.Layout(flex='1 1 auto', width='auto'))
    quantity_slider = widgets.FloatSlider(readout = False,
                                          min=min, max=max, step=step,
                                          value=value,
                                          layout=widgets.Layout(flex='10 1 auto', width='auto')
                                         )

    quantity_text = widgets.BoundedFloatText(min=min, max=max, step=step, value=value, readout_format='.6f',
                                            layout=widgets.Layout(flex='1 1 auto', width='auto'))

    widgets.link((quantity_slider, 'value'), (quantity_text, 'value'))
    quantity = widgets.HBox([quantity_label, quantity_slider, quantity_text], layout=widgets.Layout(display='flex', width='50%'))
    return quantity, quantity_slider, quantity_text