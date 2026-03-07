import flet as ft

def main(page: ft.Page):
    page.title = "Flet App"
    page.theme_mode = 'light'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_label = ft.Text('Info', color='blue', size=20)

    user_text = ft.TextField(
        value="0", 
        width=150, 
        text_align=ft.TextAlign.CENTER,
        on_submit=lambda e: get_info(e)
    )

    def get_info(e):
        if hasattr(e.control, "content") and e.control.content.value == "Do not click me":
            user_label.color = 'red'
        else:
            user_label.color = 'blue'

        user_label.value = user_text.value
        
        user_text.value = ""
        
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.HOME, on_click=get_info),
                ft.Icon(ft.Icons.BACK_HAND),
                ft.Button(content=ft.Text("Click me"), on_click=get_info),
                ft.Button(content=ft.Text("Do not click me"), on_click=get_info),
                ft.Checkbox(label='Do you agree?', value=True, on_change=get_info)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        
        ft.Row(
            [
                user_label,
                user_text
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.run(main)