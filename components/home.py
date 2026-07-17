from reactpy import component, html

@component
def Home():
    home = html.div(
        {
            "style": {
                "background": "#ffffff",
                "width": "100px",
                "height": "100px"
            }
        },
        
    )
    
    return home