from reactpy import component, html

@component
def Logs():
    logs = html.div(
                {
                    "style": {
                        "width": "100%",
                        "height": "65.5dvh",
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "center",
                    }
                },
                html.i({"class_name": "material-icons", "style": {"font-size": "5rem"}}, "construction")
            )
    
    return logs