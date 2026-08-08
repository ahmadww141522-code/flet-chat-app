import flet as ft

def main(page: ft.Page):
    page.title = "معهد العمران"
    page.theme_mode = "light"
    page.padding = 15
    
    sections_data = {
        "الحروف والكتابة 📚": "منهج الحروف:\n- التعرف على الحروف.\n- التدرب على الكتابة.",
        "الرسم الحر 🎨": "منهج الرسم:\n- تنمية الخيال.\n- التعبير بالرسم.",
        "تصميم الأزياء 👗": "منهج التصميم:\n- تنسيق الألوان.\n- مهارات الابتكار.",
        "الأنشطة والمهارات 🛠️": "منهج الأنشطة:\n- مهارات الحركة.\n- ألعاب التركيب.",
        "تعديل السلوك ☀️": "منهج السلوك:\n- تعزيز السلوك الإيجابي.\n- إدارة الانفعالات.",
        "تحسين النطق 🗣️": "منهج النطق:\n- تمارين أعضاء الفم.\n- التدريب على مخارج الحروف.",
        "الحساب الذهني 🔢": "منهج الحساب:\n- فهم الأرقام.\n- وسائل بصرية.",
        "المتابعة المدرسية 📖": "منهج المتابعة:\n- دعم الواجبات.\n- تبسيط المواد."
    }

    display = ft.Text("اضغط على أي قسم بالأعلى لاستعراض المنهج.", size=14)

    def clicked(e):
        display.value = sections_data.get(e.control.data, "")
        page.update()

    grid = ft.GridView(expand=False, runs_count=2, max_extent=160, child_aspect_ratio=2.6, spacing=8, run_spacing=8)
    for title in sections_data.keys():
        grid.controls.append(ft.ElevatedButton(title, data=title, on_click=clicked))

    chat = ft.ListView(expand=True, spacing=10, padding=5)
    field = ft.TextField(hint_text="اسأل المدرب...", expand=True)

    def send(e):
        if field.value:
            chat.controls.append(ft.Text(f"أنت: {field.value}"))
            field.value = ""
            page.update()

    page.add(
        ft.Text("معهد العمران", size=20, weight="bold"),
        ft.Container(content=grid, height=190),
        ft.Divider(),
        ft.Container(content=chat, expand=True, border=ft.border.all(1, "grey"), padding=10),
        ft.Row([field, ft.ElevatedButton("إرسال", on_click=send)]),
        ft.Divider(),
        display
    )

ft.app(target=main)
