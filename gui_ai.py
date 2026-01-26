import flet as ft
import os

def main(page: ft.Page):
    page.title = "Realme C75 AI Dashboard"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "adaptive"

    # واجهة احترافية
    header = ft.Text("مساعد محمد الذكي 🤖", size=32, weight="bold", color="blue400")
    
    file_list = ft.Column()

    def scan_files(e):
        path = "/sdcard/Download/"
        if os.path.exists(path):
            # جلب الملفات الـ 20 التي اكتشفناها سابقاً
            files = [f for f in os.listdir(path) if f.lower().endswith(('.mp4', '.jpg', '.png'))]
            file_list.controls.clear()
            for f in files:
                file_list.controls.add(
                    ft.Card(
                        content=ft.Container(
                            content=ft.ListTile(
                                leading=ft.Icon(ft.icons.IMAGE if f.endswith(('.jpg', '.png')) else ft.icons.PLAY_CIRCLE),
                                title=ft.Text(f),
                                subtitle=ft.Text("اضغط للتحليل"),
                            ), padding=10
                        )
                    )
                )
            page.update()

    page.add(
        header,
        ft.ElevatedButton("البحث عن الوسائط 🔍", on_click=scan_files),
        ft.Divider(),
        file_list
    )

# تشغيله كواجهة ويب لضمان عمله على الأندرويد
ft.run(main, view=ft.AppView.WEB_BROWSER)
