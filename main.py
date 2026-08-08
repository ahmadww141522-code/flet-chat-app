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

    # 1. منهج تعلم الحروف والكتابة
    def open_alphabet(e):
        content_area.controls.clear()
        content_area.controls.extend([
            ft.Text("📚 المنهج التعليمي: تعلم الحروف والكتابة", size=18, weight="bold", color="purple"),
            ft.Text("• الأهداف: إتقان نطق وكتابة الحروف العربية الهجائية من الألف إلى الياء.", size=14),
            ft.Text("• المحاور التدريبية:", size=14, weight="bold"),
            ft.Text("  1. التعرف على شكل الحرف في أول ووسط وآخر الكلمة.", size=13),
            ft.Text("  2. ربط الحرف بكلمات حسية وأمثلة من البيئة المحيطة (مثل أ - أسد، ب - بطة).", size=13),
            ft.Text("  3. تمارين تتبع الخطوط وتثبيت حركة الأصابع على الشاشة أو الورق.", size=13),
        ])
        page.update()

    # 2. منهج الرسم الحر والتعبير الفني
    def open_drawing(e):
        content_area.controls.clear()
        content_area.controls.extend([
            ft.Text("🎨 المنهج التعليمي: الرسم الحر والتعبير الفني", size=18, weight="bold", color="teal"),
            ft.Text("• الأهداف: تنمية التآزر البصري الحركي والتعبير عن المشاعر بالألوان.", size=14),
            ft.Text("• المحاور التدريبية:", size=14, weight="bold"),
            ft.Text("  1. التدريب على استخدام الألوان الأساسية والثانوية وتمييزها.", size=13),
            ft.Text("  2. تمارين تلوين المساحات المحددة لزيادة التركيز ودقة التحكم.", size=13),
            ft.Text("  3. الرسم الحر والتعبير عن الأفكار الذاتية لتعزيز الثقة بالنفس.", size=13),
        ])
        page.update()

    # 3. منهج تصميم الأزياء وتنسيق الألوان
    def open_fashion(e):
        content_area.controls.clear()
        content_area.controls.extend([
            ft.Text("👗 المنهج التعليمي: تصميم الأزياء وتنسيق الألوان", size=18, weight="bold", color="deeppink"),
            ft.Text("• الأهداف: تنمية الذوق العام، التنسيق البصري، والمهارات الحياتية.", size=14),
            ft.Text("• المحاور التدريبية:", size=14, weight="bold"),
            ft.Text("  1. تعليم تناسق الألوان المتجانسة والمتضادّة في الملابس.", size=13),
            ft.Text("  2. دمج قطع الملابس واختيار الطقم المناسب لكل فصل أو مناسبة.", size=13),
            ft.Text("  3. تنمية مهارات الاعتماد على النفس في اختيار المظهر الشخصي.", size=13),
        ])
        page.update()

    # 4. الأنشطة والمهارات الحركية والذهنية
    def open_skills(e):
        content_area.controls.clear()
        content_area.controls.extend([
            ft.Text("🛠️ المنهج التعليمي: الأنشطة والمهارات الحركية", size=18, weight="bold", color="sienna"),
            ft.Text("• الأهداف: تحسين اللياقة الحركية الدقيقة، وسرعة الاستجابة والتركيز.", size=14),
            ft.Text("• المحاور التدريبية:", size=14, weight="bold"),
            ft.Text("  1. تمارين تقوية عضلات اليدين والأصابع لتسهيل الكتابة.", size=13),
            ft.Text("  2. ألعاب تتبع الأشكال الهندسية وتركيب المتاهات البصرية.", size=13),
            ft.Text("  3. أنشطة التوازن والتركيز الحركي البصري اليومي.", size=13),
        ])
        page.update()

    # 5. برنامج تحسين النطق ومخارج الكلمات
    def open_speech(e):
        content_area.controls.clear()
        content_area.controls.extend([
            ft.Text("🗣️ المنهج التعليمي: تحسين النطق ومخارج الكلمات", size=18, weight="bold", color="brown"),
            ft.Text("• الأهداف: وضوح الكلمات، تصحيح مخارج الحروف، وتعزيز التواصل الاجتماعي.", size=14),
            ft.Text("• المحاور التدريبية:", size=14, weight="bold"),
            ft.Text("  1. تمارين الإحماء لعضلات النطق والفم واللسان.", size=13),
            ft.Text("  2. نطق الأصوات الصعبة وتكرار المقاطع الصوتية بوضوح.", size=13),
            ft.Text("  3. تدريبات سرد الجمل القصيرة والأدعية والأذكار اليومية.", size=13),
        ])
        page.update()

    # 6. برنامج تعديل السلوك والتعزيز الإيجابي
    def open_behavior(e):
        content_area.controls.clear()
        content_area.controls.extend([
            ft.Text("🌟 المنهج التعليمي: تعديل السلوك والتعزيز الإيجابي", size=18, weight="bold", color="indigo"),
            ft.Text("• الأهداف: بناء بيئة إيجابية، تعزيز الثقة، وتنمية مهارات التكيف الاجتماعي.", size=14),
            ft.Text("• المحاور التدريبية:", size=14, weight="bold"),
            ft.Text("  1. استخدام القصص التوجيهية الهادفة لغرس القيم والأخلاق.", size=13),
            ft.Text("  2. نظام التعزيز والنجوم التحفيزية للإنجازات اليومية.", size=13),
            ft.Text("  3. تدريب الطالب على الصبر، الالتزام بالمواعيد، واحترام الزملاء.", size=13),
        ])
        page.update()

    # 7. برنامج المتابعة المدرسية والواجبات
    def open_tutoring(e):
        content_area.controls.clear()
        content_area.controls.extend([
            ft.Text("📖 المنهج التعليمي: المتابعة المدرسية والواجبات", size=18, weight="bold", color="pink"),
            ft.Text("• الأهداف: دعم التحصيل الدراسي ومواكبة المناهج المدرسية الرسمية.", size=14),
            ft.Text("• المحاور التدريبية:", size=14, weight="bold"),
            ft.Text("  1. المساعدة الفردية في حل الواجبات المدرسية اليومية.", size=13),
            ft.Text("  2. تبسيط الشرح للمفاهيم الصعبة في المواد الأساسية.", size=13),
            ft.Text("  3. التحضير المسبق للامتحانات وتقديم اختبارات تجريبية مبسطة.", size=13),
        ])
        page.update()

    # 8. برنامج الحساب الذهني والتفكير السريع
    def open_mental_math(e):
        content_area.controls.clear()
        content_area.controls.extend([
            ft.Text("🔢 المنهج التعليمي: الحساب الذهني والعد", size=18, weight="bold", color="orange"),
            ft.Text("• الأهداف: تنمية سرعة البديهة والقدرة على إجراء العمليات الحسابية.", size=14),
            ft.Text("• المحاور التدريبية:", size=14, weight="bold"),
            ft.Text("  1. التدريب على العد التصاعدي والتنازلي باستخدام الأصابع والوسائل الحسية.", size=13),
            ft.Text("  2. استراتيجيات الجمع والطرح البسيط بطرق ممتعة ومبتكرة.", size=13),
            ft.Text("  3. ألعاب الذاكرة الرقمية لتنشيط الفص العشقي والمخ.", size=13),
        ])
        page.update()

    # شبكة الأزرار الثمانية الشاملة
    sections_grid = ft.Column([
        ft.Row([
            ft.ElevatedButton("📚 الحروف والكتابة", width=150, height=35, on_click=open_alphabet),
            ft.ElevatedButton("🎨 الرسم الحر", width=150, height=35, on_click=open_drawing),
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.ElevatedButton("👗 تصميم الأزياء", width=150, height=35, on_click=open_fashion),
            ft.ElevatedButton("🛠️ الأنشطة والمهارات", width=150, height=35, on_click=open_skills),
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.ElevatedButton("🗣️ تحسين النطق", width=150, height=35, on_click=open_speech),
            ft.ElevatedButton("🌟 تعديل السلوك", width=150, height=35, on_click=open_behavior),
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.ElevatedButton("📖 المتابعة المدرسية", width=150, height=35, on_click=open_tutoring),
            ft.ElevatedButton("🔢 الحساب الذهني", width=150, height=35, on_click=open_mental_math),
        ], alignment=ft.MainAxisAlignment.CENTER),
    ], spacing=6)

    # عناصر محادثة المدرب الذكي (Groq) المرئية بوضوح
    chat_list = ft.ListView(expand=True, spacing=5, auto_scroll=True)
    user_input = ft.TextField(label="اسأل المدرب في معهد العمران...", expand=True, height=45)

    def send_to_groq(e):
        if not user_input.value:
            return
        user_text = user_input.value
        chat_list.controls.append(ft.Text(f"أنت: {user_text}", color="blue", weight="bold"))
        
        current_query = user_text
        user_input.value = ""
        page.update()

        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "أنت مساعد ذكي ومدرب خبير في معهد العمران لأصحاب الهمم. أجب عن أسئلة أولياء الأمور والزبائن بدقة واحترافية وبأسلوب لطيف ومشجع."},
                    {"role": "user", "content": current_query}
                ],
                model="llama-3.1-8b-instant", 
            )
            ai_reply = chat_completion.choices[0].message.content
            chat_list.controls.append(ft.Text(f"المدرب: {ai_reply}", color="green", weight="bold"))
        except Exception as ex:
            chat_list.controls.append(ft.Text(f"خطأ في الاتصال: {str(ex)}", color="red"))
            
        page.update()

    title_text = ft.Text("معهد العمران - الدليل الشامل لأصحاب الهمم", size=18, weight="bold", color="orange")

    # الترتيب الجديد والمثالي للشاشة بحيث تظهر المحادثة فوراً بدون تمرير
    page.add(
        ft.Column([
            title_text,
            sections_grid,
            ft.Divider(),
            ft.Text("💬 محادثة فورية مع مدرب معهد العمران:", size=13, weight="bold", color="purple"),
            ft.Container(
                content=chat_list,
                height=100,
                bgcolor="#ffffff",
                padding=5,
                border_radius=8
            ),
            ft.Row([
                user_input, 
                ft.ElevatedButton("إرسال", bgcolor="orange", color="white", on_click=send_to_groq)
            ]),
            ft.Divider(),
            ft.Container(
                content=content_area, 
                padding=10, 
                bgcolor="#f8f9fa", 
                border_radius=8
            )
        ], scroll=ft.ScrollMode.AUTO, expand=True, spacing=8)
    )

ft.app(target=main)
