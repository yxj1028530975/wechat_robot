import flet as ft
from utils.utils import nav_app_bar
from views.group.group_view import group_view
class MainView:
    def __init__(self, page: ft.Page, switch_navigation_rail):
        self.page = page
        self.page.window_width = 1650
        self.page.window_height = 1700
        self.switch_navigation_rail = switch_navigation_rail
        self.page.content = ft.Column([group_view()], alignment=ft.MainAxisAlignment.START, expand=True)
        self.page.selected_index = 0
        self.setup_page()
        self.main_page_ui()
        self.app_bar = nav_app_bar("主页")
        #print(create_app_bar("Login", on_back))
        self.page.add(self.app_bar)

    def setup_page(self):
        self.page.controls.clear()
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width = 950
        self.page.window_height = 650
        self.page.window_resizable = True
        self.page.window_always_on_top = True
        self.page.title = '主页'
        # 获取导航栏内容
        # content = self.switch_navigation_rail(1)

        # 将内容添加到页面
        # self.page.controls.append(content)
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  
        self.page.update()
    
    
    def main_page_ui(self):
        
        rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        # leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="群列表"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="好友列表",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("公众号列表"),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("全局设置"),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("高级功能"),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("应用插件"),
            ),
        ],
        on_change=lambda e: self.switch_navigation_rail(self.page.selected_index,e.control.selected_index),
    )
        self.page.add(
            ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                self.page.content,
            ],
            expand=True,
        ))
        self.page.update()

        
        
