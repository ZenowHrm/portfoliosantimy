from reactpy import component, html

@component
def Ideas():
    ideas = html.div(
        {
            "style": {
                "background": "#0000ff",
                "width": "100px",
                "height": "100px"
            }
        },
        
    )
    
    return ideas