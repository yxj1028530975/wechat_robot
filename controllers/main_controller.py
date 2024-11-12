import flet as ft
from views.main_view import MainView
from views.group.group_view import group_view


class MainController:
    def __init__(self, page: ft.Page, app):   
        self.page = page
        self.app = app
        self.view = MainView(page, self.switch_navigation_rail)

        # 切换导航栏展示
    def switch_navigation_rail(self,old_index,index):
        if old_index == index:
            return
        print("切换导航栏展示",index)
        if index == 0:
            self.page.content.controls = [group_view()]
        elif index == 1:
            self.page.content.controls = [ft.Text("好友列表内容")]
        elif index == 2:
            self.page.content.controls = [ft.Text("公众号列表内容")]
        elif index == 3:
            self.page.content.controls = [ft.Text("全局设置内容")]
        elif index == 4:
            self.page.content.controls = [ft.Text("高级功能内容")]
        elif index == 5:
           self.page.content.controls = [ft.Text("应用插件内容")]
        self.page.selected_index = index
        self.page.content.update()