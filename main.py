import flet as ft 
from groq import Groq
client= Groq(api_key="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")
def main(page: ft.Page):
    page.title="AI Chat Interface"
    page.theme_mode=ft.ThemeMode.LIGHT
    page.rtl=True
    chat_display= ft.ListView(expand=True, spacing=10, auto_scroll=True)
    user_input = ft.TextField(hint_text="اكتب سؤالك هنا", expand=True)
    def send_message(e):
        prompt = user_input.value
        if not prompt:
            return
        chat_display.controls.append(ft.Text(f"انت: {prompt}", weight=ft.FontWeight.BOLD))
        user_input.value = ""
        page.update()
        try :
            completion=client.chat.completions.create(model="llama-3.1-8b-instant",messages=[{"role":"user","content": prompt}])
            result= completion.choices[0].message.content
            chat_display.controls.append(ft.Text(f"AI: {result}"))
        except Exception as ex:
            chat_display.controls.append(ft.Text(f"حدث خطأ : {ex.name}"))
        page.update()
    send_btn = ft.ElevatedButton("ارسال",on_click=send_message)
    page.add(
        chat_display,
        ft.Row([user_input, send_btn]))
if __name__=="__main__":
    ft.app(target=main)           
