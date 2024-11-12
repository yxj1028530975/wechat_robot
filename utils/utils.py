import flet as ft


def create_app_bar(title, go_back):
    bt_back = ft.IconButton(
            icon=ft.icons.ARROW_BACK,
            on_click=go_back,
            width=120,
            height=50
     )
    

    return ft.AppBar(
        title=ft.Text(title),
        leading=bt_back
    )

def nav_app_bar(title):
    
    advanced_services = ft.CupertinoFilledButton(
            content=ft.Text("123"),
            opacity_on_click=0.3,
            on_click=lambda e: print("CupertinoFilledButton clicked!"),
     )
    

    return  ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text(title),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            # ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    # ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=lambda e: print("Checked item clicked!")
                    ),
                ]
            ),
        ],
    )


def msg_erro(msg, open):
    banner = ft.Banner(
        open=open,
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(
            ft.icons.DANGEROUS_SHARP,
            color=ft.colors.RED_400,
            size=40
            ),
        content=ft.Text(msg,
                        color=ft.colors.BLACK,
                        size=10
                ),
        )
    return banner
