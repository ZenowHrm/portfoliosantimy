from reactpy import component, html

@component
def Me():
    yo = html.div(
        {
            "style": {
                "background": "#00ff00",
                "width": "100px",
                "height": "100px"
            }
        },
        
    )
    
    return yo