import flet as ft
from groq import Groq

client = Groq(api_key="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")

def main(page: ft.Page):
    page.title = "مهندس أحمد"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    def calculate_all(e):
        try:
            v_val = float(v.value)
            r_val = float(r.value)
            current = v_val / r_val
            power = v_val * current
            res_ohm.value = f"التيار: {current:.2f} أمبير"
            res_power.value = f"الاستطاعة: {power:.2f} واط"
            page.update()
        except:
            res_ohm.value = "خطأ: أدخل أرقاماً صحيحة"
            res_power.value = ""
            page.update()

    v = ft.TextField(label="الجهد (Volt)", width=200)
    r = ft.TextField(label="المقاومة (Ohm)", width=200)
    res_ohm = ft.Text(size=16, weight="bold")
    res_power = ft.Text(size=16, weight="bold", color="blue")

    chat_list = ft.ListView(expand=True, spacing=10, height=200)
    user_input = ft.TextField(label="اسأل المهندس أحمد...", expand=True)

    def send_to_groq(e):
        if not user_input.value:
            return
        user_text = user_input.value
        chat_list.controls.append(ft.Text(f"أنت: {user_text}", color="blue"))
        
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": user_text}],
                model="llama-3.1-8b-instant", 
            )
            ai_reply = chat_completion.choices[0].message.content
            chat_list.controls.append(ft.Text(f"المهندس أحمد: {ai_reply}", color="green"))
        except Exception as ex:
            chat_list.controls.append(ft.Text(f"خطأ: {str(ex)}", color="red"))
            
        user_input.value = ""
        page.update()

    # جعل الصفحة قابلة للتمرير لكي تظهر كافة العناصر بوضوح
    page.add(
        ft.Column([
            ft.Text("الحسابات الهندسية (أوم والاستطاعة)", size=18, weight="bold"),
            v, r, 
            ft.ElevatedButton("احسب التيار والاستطاعة", on_click=calculate_all), 
            res_ohm,
            res_power,
            ft.Divider(),
            ft.Text("محادثة مع المهندس أحمد", size=18, weight="bold"),
            chat_list,
            ft.Row([user_input, ft.ElevatedButton("إرسال", on_click=send_to_groq)])
        ], scroll=ft.ScrollMode.AUTO, expand=True, spacing=10)
    )

ft.app(target=main)
