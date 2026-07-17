from reactpy import component, html

@component
def Projects():
    projects = html.div(
        {
            "style": {
                "background": "#ff0000",
                "width": "100px",
                "height": "100px"
            }
        },
        
    )
    
    return projects