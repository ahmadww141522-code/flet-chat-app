import flet as ft

def main(page: ft.Page):
    page.title = "معهد العمران - الدليل الشامل"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 15

    # بيانات المناهج والأقسام (لم نلغِ منها شيئاً، كل التفاصيل موجودة هنا)
    sections_data = {
        "الحروف والكتابة 📚": "منهج الحروف والكتابة:\n- التعرف على الحروف الهجائية بطرق حسية وبصرية.\n- التدرب على مسك القلم والكتابة بخطوات مبسطة.\n- تمارين تقوية عضلات اليد الدقيقة.",
        "الرسم الحر 🎨": "منهج الرسم الحر:\n- التعبير عن المشاعر والأفكار باستخدام الألوان.\n- تنمية الخيال والإبداع الحسي.\n- استخدام أدوات رسم متنوعة تناسب قدرات الطالب.",
        "تصميم الأزياء 👗": "منهج تصميم الأزياء:\n- دمج الألوان وتنسيقها.\n- التعرف على الأقمشة والملمس.\n- مهارات الابتكار وتصميم أشكال مبسطة.",
        "الأنشطة والمهارات 🛠️": "منهج الأنشطة والمهارات:\n- تنمية مهارات التآزر البصري الحركي.\n- ألعاب التركيب وفك وتركيب المكعبات.\n- الأنشطة اليدوية اليومية لزيادة الاستقلالية.",
        "تعديل السلوك ☀️": "منهج تعديل السلوك:\n- تعزيز السلوكيات الإيجابية بأساليب تحفيزية.\n- إدارة التوتر والانفعالات.\n- بناء الروتين اليومي المريح للطالب.",
        "تحسين النطق 🗣️": "منهج تحسين النطق:\n- تمارين أعضاء النطق والفم.\n- التدريب على مخارج الحروف والكلمات البسيطة.\n- تشجيع التواصل البصري واللفظي.",
        "الحساب الذهني 🔢": "منهج الحساب الذهني:\n- فهم الأرقام والعد بطرق تفاعلية ممتعة.\n- استخدام الوسائل البصرية للجمع والطرح البسيط.\n- ربط الأرقام بالحياة اليومية.",
        "المتابعة المدرسية 📖": "منهج المتابعة المدرسية:\n- دعم الواجبات المدرسية وتنسيقها.\n- تبسيط المواد الدراسية المعقدة.\n- متابعة التقدم الأكاديمي بشكل دوري."
    }

    # منطقة عرض محتوى القسم المختار (لتظهر التفاصيل عند الضغط)
    content_display = ft.Text(
        "مرحباً بك في دليل معهد العمران الشامل.\nاضغط على أي قسم بالأعلى لاستعراض الخطة التدريبية والمحتوى التعليمي الكامل المقدم للطلاب.",
        size=14,
        color=ft.colors.BLUE_700
    )

    def on_section_click(e):
        section_name = e.control.data
        if section_name in sections_data:
            content_display.value = sections_data[section_name]
            page.update()

    # تصميم الأيقونات في الأعلى بشكل مرتب ومريح
    grid = ft.GridView(
        expand=False,
        runs_count=2,
        max_extent=160,
        child_aspect_ratio=2.6,
        spacing=8,
        run_spacing=8,
    )

    for title in sections_data.keys():
        btn = ft.ElevatedButton(
            text=title, 
            data=title, 
            on_click=on_section_click,
            style=ft.ButtonStyle(padding=5)
        )
        grid.controls.append(btn)

    # حقل المحادثة والرسائل (مع expand=True لملء الفراغ الأبيض بالكامل)
    chat_list = ft.ListView(expand=True, spacing=10, padding=5)
    chat_list.controls.append(
        ft.Text("🤖 مساعدةك اليوم؟ هل تود إستفسارًا عن البرامج التعليمية في معهد العمران لأصحاب الهمم؟", color=ft.colors.GREEN_800)
    )

    user_input = ft.TextField(hint_text="اسأل المدرب في معهد العمران...", expand=True, border_radius=8)

    def send_message(e):
        if user_input.value:
            chat_list.controls.append(ft.Text(f"أنت: {user_input.value}", color=ft.colors.BLACK))
            query = user_input.value
            user_input.value = ""
            
            # رد تلقائي ذكي مبسط
            response = "أهلاً بك! يمكنك الضغط على الأقسام بالأعلى للاطلاع على المنهج التدريبي المفصل."
            for key, val in sections_data.items():
                if any(word in query for word in key.split()):
                    response = f"تفاصيل {key}:\n{val}"
                    break
            
            chat_list.controls.append(ft.Text(f"المدرب: {response}", color=ft.colors.BLUE_900))
            page.update()

    send_btn = ft.ElevatedButton("إرسال", on_click=send_message, bgcolor=ft.colors.ORANGE, color=ft.colors.WHITE)

    # الترتيب الهيكلي للشاشة لاستغلال المساحات وتجنب الفراغ الأبيض
    page.add(
        ft.Text("معهد العمران - الدليل الشامل لأصحاب الهمم", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.AMBER_900),
        ft.Container(content=grid, height=190), # مساحة محددة للأيقونات في الأعلى بدون تداخل
        ft.Divider(),
        ft.Row([ft.Icon(ft.icons.CHAT, size=18), ft.Text("محادثة فورية مع مدرب معهد العمران:")], tight=True),
        # صندوق المحادثة أصبح يتمدد (expand=True) ليمتلئ الفراغ الأبيض
        ft.Container(
            content=chat_list, 
            expand=True, 
            border=ft.border.all(1, ft.colors.GREY_300), 
            border_radius=8,
            padding=10
        ),
        ft.Row([user_input, send_btn]),
        ft.Divider(),
        # قسم عرض المنهج التفصيلي عند الضغط
        ft.Container(
            content=content_display,
            padding=10,
            bgcolor=ft.colors.GREY_50,
            border_radius=8
        )
    )

ft.app(target=main)
