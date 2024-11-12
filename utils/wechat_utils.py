import winreg
import os
import flet as ft

def wechat_version_warning(self):
    if wechat_install_path:=get_wechat_install_path():
        if not get_wechat_version(wechat_install_path):
            self.app_bar = ft.AppBar(
            title=ft.Text('微信版本错误,请安装[3.9.10.19]版本微信'),color=ft.colors.RED_400
            )
            self.page.add(self.app_bar)
    else:
        self.app_bar = ft.AppBar(
        title=ft.Text('微信未安装,请安装[3.9.10.19]版本微信'),color=ft.colors.RED_400
        )
        self.page.add(self.app_bar)
        return 
    
def get_wechat_install_path():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Tencent\WeChat")
    WeChatPath = winreg.QueryValueEx(key, "InstallPath")
    if not WeChatPath:
        return False
    return WeChatPath[0]

def get_wechat_version(WeChatPath):
    wx_path = WeChatPath + '/[3.9.10.19]'
    # 判断微信版本是否正确
    if not os.path.exists(wx_path):
        return False
    return wx_path
        
                                                                         

if __name__ == '__main__':
    WeChatPath = get_wechat_install_path()
    wx_path = get_wechat_version(WeChatPath)