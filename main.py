import flet as ft
from groq import Groq

# تهيئة عميل الذكاء الاصطناعي لمدرب معهد العمران
client = Groq(api_key="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")

def main(page: ft.Page):
    page.title = "معهد العمران - أصحاب الهمم"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # منطقة عرض المحتوى العلمي والمنهجي لكل قسم
    content_area = ft.Column([
        ft.Text("مرحباً بك في دليل معهد العمران الشامل.", size=16, weight="bold", color="blue"),
        ft.Text("اضغط على أي قسم بالأعلى لاستعراض الخطة التدريبية والمحتوى التعليمي الكامل المقدم للطلاب.", size=14)
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # وظائف عرض المناهج
    def open_alphabet(e):
        content_area.controls.clear()
        content_area.controls.append(ft.Text("📚 المنهج التعليمي: تعلم الحروف والكتابة", size=18, weight="bold", color="purple"))
        page.update()

    def open_drawing(e):
        content_area.controls.clear()
        content_area.controls.append(ft.Text("🎨 المنهج التعليمي: الرسم الحر والتعبير الفني", size=18, weight="bold", color="teal"))
        page.update()

    def open_fashion(e):
        content_area.controls.clear()
        content_area.controls.append(ft.Text("👗 المنهج التعليمي: تصميم الأزياء وتنسيق الألوان", size=18, weight="bold", color="deeppink"))
        page.update()

    def open_skills(e):
        content_area.controls.clear()
        content_area.controls.append(ft.Text("🛠️ المنهج التعليمي: الأنشطة والمهارات الحركية", size=18, weight="bold", color="sienna"))
        page.update()

    def open_speech(e):
        content_area.controls.clear()
        content_area.controls.append(ft.Text("🗣️ المنهج التعليمي: تحسين النطق ومخارج الكلمات", size=18, weight="bold", color="brown"))
        page.update()

    def open_behavior(e):
        content_area.controls.clear()
        content_area.controls.append(ft.Text("🌟 المنهج التعليمي: تعديل السلوك والتعزيز الإيجابي", size=18, weight="bold", color="indigo"))
        page.update()

    def open_tutoring(e):
        content_area.controls.clear()
        content_area.controls.append(ft.Text("📖 المنهج التعليمي: المتابعة المدرسية والواجبات", size=18, weight="bold", color="pink"))
        page.update()

    def open_mental_math(e):
        content_area.controls.clear()
        content_area.controls.append(ft.Text("🔢 المنهج التعليمي: الحساب الذهني والعد", size=18, weight="bold", color="orange"))
        page.update()

    # شبكة الأزرار
    sections_grid = ft.Column([
        ft.Row([ft.ElevatedButton("📚 الحروف", on_click=open_alphabet), ft.ElevatedButton("🎨 الرسم", on_click=open_drawing)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton("👗 الأزياء", on_click=open_fashion), ft.ElevatedButton("🛠️ المهارات", on_click=open_skills)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton("🗣️ النطق", on_click=open_speech), ft.ElevatedButton("🌟 السلوك", on_click=open_behavior)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton("📖 المتابعة", on_click=open_tutoring), ft.ElevatedButton("🔢 الحساب", on_click=open_mental_math)], alignment=ft.MainAxisAlignment.CENTER),
    ], spacing=6)

    # المحادثة
    chat_list = ft.ListView(expand=True, height=100)
    user_input = ft.TextField(label="اسأل المدرب...", expand=True)

    def send_to_groq(e):
        if not user_input.value: return
        chat_list.controls.append(ft.Text(f"أنت: {user_input.value}", color="blue"))
        page.update()
        # هنا سيتم استدعاء الذكاء الاصطناعي
        user_input.value = ""
        page.update()

    page.add(
        ft.Column([
            ft.Text("معهد العمران - الدليل الشامل", size=20, weight="bold", color="orange"),
            sections_grid,
            ft.Divider(),
            chat_list,
            ft.Row([user_input, ft.ElevatedButton("إرسال", on_click=send_to_groq)]),
            ft.Container(content=content_area, padding=10)
        ], scroll=ft.ScrollMode.AUTO)
    )

ft.app(target=main)
