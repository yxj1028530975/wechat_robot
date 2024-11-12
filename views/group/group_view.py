import flet as ft


# 群列表视图
def group_view():
    ft_tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="群管理",
                content=ft.Container(
                    ft.Column(
                        [
                            group_select_delete_find_view(),
                            group_admin_tab(),
                        ]
                    ),
                ),
            ),
            ft.Tab(
                text="帮助说明",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
        ],
        expand=1,
    )
    return ft_tabs


def group_select_delete_find_view():

    ft_checkbox = ft.Checkbox(label="全选", value=True)
    ft_delete = ft.TextButton(text="删除")
    ft_find = ft.TextField(
        label="查找",
        autofill_hints=ft.AutofillHint.NAME,
        text_size=12,
        height=30,
    )
    ft_find_button = ft.ElevatedButton(
        "查找",
        width=80,
        height=30,
    )

    ft_first_row = ft.Container(
        content=ft.Row([ft_checkbox, ft_delete, ft_find, ft_find_button]),
        padding=ft.padding.all(10),
    )
    return ft_first_row


def group_admin_tab():
    ft_lv = ft.ListView(expand=1, spacing=10, padding=20)
    count = 1
    # 生成测试数据，序号，昵称，备注，状态，被删除，被拉黑，总管理员
    data = [
        {"id": 1, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 2, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 3, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 4, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 5, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 6, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 7, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 8, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 9, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 10, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 11, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 12, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 13, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 14, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 15, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 16, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 17, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 18, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 19, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 20, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 21, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 22, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
        {"id": 23, "nickname": "张三", "remark": "张三", "status": "正常", "deleted": "否", "black": "否", "admin": "是"},
    ] 
    for i in data:
        ft_lv.controls.append(
            group_admin_tab_line(i)    
    )
        count += 1
    ft_datatab = ft.Container(
        height=400,
        content=ft.Column(
            [
                group_admin_tab_line_title(),
                ft_lv,
            ],
        ),
        border=ft.border.all(1, ft.colors.GREY)
    )
    return ft_datatab

def group_admin_tab_line_title():
    ft_row = ft.Container(
        width=400,
        content=ft.Row(
        [
            ft.Text("序号"),
            ft.Text("昵称"),
            ft.Text("备注"),
            ft.Text("状态"),
            ft.Text("被删除"),
            ft.Text("被拉黑"),
            ft.Text("总管理员"),
        ],
        # 平均分配空间
        spacing=400/7,
    ),
                          )
    return ft_row

def group_admin_tab_line(data):
    # 每行增加边框
    ft_row = ft.Container(content=ft.Row(
        [
            ft.Checkbox(label=data['id'], value=False),
            ft.Text(data['nickname']),
            ft.Text(data['remark']),
            ft.Text(data['status']),
            ft.Text(data['deleted']),
            ft.Text(data['black']),
            ft.Text(data['admin']),
        ],
        spacing=400/7,
    ),
    border=ft.border.all(1, ft.colors.GREY))
    return ft_row

