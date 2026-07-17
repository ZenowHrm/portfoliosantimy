from reactpy import component, html

@component
def Logs():
    logs = html.div(
        {
            "style": {
                "background": "#000000",
                "width": "100px",
                "height": "100px"
            }
        },
        
    )
    
    return logs