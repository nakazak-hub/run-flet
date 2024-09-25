import flet as ft

# تعريف الدالة الرئيسية للتطبيق
def main(root: ft.Page):
    root.title = "حاسبة مكافأة المدققين"  # تعيين عنوان الصفحة
    root.window.width = 450  # تعيين عرض نافذة التطبيق
    root.window.height = 800  # تعيين ارتفاع نافذة التطبيق
    root.bgcolor = ft.colors.LIGHT_BLUE_ACCENT_700  # تعيين لون خلفية الصفحة
    root.window.top = 130  # تعيين موقع النافذة من الأعلى
    root.window.left = 760  # تعيين موقع النافذة من اليسار
    root.window.resizable = False  # منع تغيير حجم النافذة
    root.horizontal_alignment = "center"  # محاذاة المحتوى أفقيًا في المركز
    root.vertical_alignment = "top"  # محاذاة المحتوى عموديًا من الأعلى
    root.scroll = 'auto'  # تمكين التمرير التلقائي إذا لزم الأمر
    root.rtl = True  # تمكين دعم RTL (من اليمين إلى اليسار)

    calculate_reward(root)  # استدعاء دالة إنشاء محتوى الحاسبة

# تعريف دالة إنشاء محتوى الحاسبة
def calculate_reward(page):
    reward_per_successful_validation = 0.053  # قيمة المكافأة لكل عملية تحقق ناجحة

    # تعريف دالة معالجة حدث النقر على زر "احسب"
    def on_calculate_click(e):
        try:
            total_operations = int(total_operations_input.value)  # الحصول على قيمة إجمالي التحققات
            successful_operations = int(successful_operations_input.value)  # الحصول على قيمة عمليات التحقق الناجحة

            # التحقق من أن إجمالي التحققات أكبر من عمليات التحقق الناجحة
            if total_operations < successful_operations:
                results_text.value = "يجب أن يكون إجمالي التحققات أكبر من أو يساوي عمليات التحقق الناجحة."
                results_text.update()
                return

            reward = successful_operations * reward_per_successful_validation  # حساب قيمة المكافأة

            print(f"{reward:.3f} Pi")  # طباعة قيمة المكافأة في وحدة التحكم

            results_text.value = f"المكافأة: {reward:.3f} Pi"  # عرض قيمة المكافأة في واجهة المستخدم
            results_text.update()  # تحديث واجهة المستخدم
        except ValueError:
            results_text.value = "أدخل أرقامًا صحيحة."  # عرض رسالة خطأ إذا لم يتم إدخال أرقام صحيحة
            results_text.update()  # تحديث واجهة المستخدم

    # تعريف دوال معالجة أحداث النقر على أيقونات وسائل التواصل الاجتماعي
    def on_nakazak_click(e):
        page.launch_url("https://nakazak.com")  # فتح موقع ناكازاك في المتصفح

    def on_facebook_click(e):
        page.launch_url("https://web.facebook.com/nakazakhub/")  # فتح صفحة الفيسبوك في المتصفح

    def on_telegram_click(e):
        page.launch_url("https://t.me/nakazak_hub")  # فتح قناة التليجرام في المتصفح

    # إنشاء حقول إدخال النص
    total_operations_input = ft.TextField(label="إجمالي تحققات", width=250, color=ft.colors.WHITE, border_color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER)
    successful_operations_input = ft.TextField(label="عمليات التحقق الناجحة", width=250, color=ft.colors.WHITE, border_color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER)

    # إنشاء زر "احسب"
    calculate_button = ft.ElevatedButton(
        text="احسب",
        on_click=on_calculate_click,
        bgcolor=ft.colors.WHITE,
        color=ft.colors.LIGHT_BLUE_ACCENT_700,
        width=150
    )

    # إنشاء عنصر نص لعرض نتيجة الحساب
    results_text = ft.Text(color=ft.colors.WHITE, size=18, text_align=ft.TextAlign.CENTER)

    # إنشاء صف لعرض أيقونات وسائل التواصل الاجتماعي
    icons_row = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.LANGUAGE, 
                        icon_size=50,
                        on_click=on_nakazak_click,
                        tooltip="موقع ناكازاك",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(10)),
                            padding=10 
                        )
                    ),
                    ft.Text("موقع ناكازاك", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Column(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.FACEBOOK,
                        icon_size=50,
                        on_click=on_facebook_click,
                        tooltip="صفحة الفيسبوك",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(10)),
                            padding=10 
                        )
                    ),
                    ft.Text("صفحة الفيسبوك", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Column(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.TELEGRAM,
                        icon_size=50,
                        on_click=on_telegram_click,
                        tooltip="قناة التليجرام",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(10)),
                            padding=10 
                        )
                    ),
                    ft.Text("قناة التليجرام", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
    )
    
    # إنشاء عنصر نص مع إطار لعرض معلومات حول نظام المكافآت
    info_text = """
    في شبكة Pi Network، يتم توزيع المكافآت بعد التحقق من الهوية (KYC) على النحو التالي:

    1. الدفع للتحقق: يدفع المستخدم (Pioneer) 1 Pi لإتمام عملية التحقق.

    2. التوزيع:
        20% من هذا المبلغ (0.2 Pi) تذهب إلى فريق Pi Core.
        80% من المبلغ (0.8 Pi) توزع على مدققي KYC.

    3. عدد المدققين: يتم التحقق من هوية المستخدم بواسطة 15 مدققًا.

    4. المكافأة لكل مدقق: يحصل كل مدقق KYC على 0.053 Pi بعد التحقق الناجح.

    باختصار، من الـ 1 Pi المدفوع:
        يحصل فريق Pi Core على 0.2 Pi.
        يتم توزيع 0.8 Pi على المدققين، بحيث يحصل كل مدقق على 0.053 Pi.
    """
    
    info_container = ft.Container(
        content=ft.Text(info_text, color=ft.colors.WHITE, size=14, text_align=ft.TextAlign.RIGHT), 
        padding=10,
        border=ft.border.all(1, ft.colors.WHITE),
        border_radius=10,
        margin=ft.margin.only(top=20, bottom=20)
    )


    # إضافة عناصر واجهة المستخدم إلى الصفحة
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("حاسبة مكافأة المدققين في\n     Pi Network", size=20, weight="bold", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                    total_operations_input,
                    successful_operations_input,
                    calculate_button,
                    results_text,
                    info_container,
                    icons_row, 
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            ),
            padding=20
        )
    )

# تشغيل تطبيق Flet
ft.app(target=main)
