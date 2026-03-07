import flet as ft

def main(page: ft.Page):
    page.title = "Unit Converter"
    page.window.width = 350
    page.window.height = 550
    page.window.resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    input_field = ft.TextField(
        label='Input value',
        width=280, 
        keyboard_type=ft.KeyboardType.NUMBER,
        text_align=ft.TextAlign.CENTER,
        autofocus=True,
        error=None
    ) 
    
    unit_selector = ft.Dropdown(
        label='Select unit of measurement:',
        options=[
            ft.dropdown.Option('Days'),
            ft.dropdown.Option('Hours'),
            ft.dropdown.Option('Minutes'),
            ft.dropdown.Option('Seconds')
        ],
        value='Days',
        width=280
    )

    result_fields = {
        'Hours': ft.Text('0', size=16, weight=ft.FontWeight.BOLD),
        'Minutes': ft.Text('0', size=16, weight=ft.FontWeight.BOLD),
        'Seconds': ft.Text('0', size=16, weight=ft.FontWeight.BOLD),
        'Milliseconds': ft.Text('0', size=16, weight=ft.FontWeight.BOLD),
        'Weeks': ft.Text('0', size=16, weight=ft.FontWeight.BOLD)
    }

    def convert(e):
        try:
            number = float(input_field.value)
            unit = unit_selector.value
            
            if unit == 'Days':
                hour = number * 24
                minute = hour * 60
                second = minute * 60
                millisecond = second * 1000
                week = number / 7
            elif unit == 'Hours':
                hour = number
                minute = hour * 60
                second = minute * 60
                millisecond = second * 1000
                week = hour / 168
            elif unit == 'Minutes':
                minute = number
                hour = minute / 60
                second = minute * 60
                millisecond = second * 1000
                week = minute / 10080
            elif unit == 'Seconds':
                second = number
                minute = second / 60
                hour = minute / 60
                millisecond = second * 1000
                week = second / 604800

            result_fields['Hours'].value = f"{hour:,.2f}"
            result_fields['Minutes'].value = f"{minute:,.2f}"
            result_fields['Seconds'].value = f"{second:,.2f}"
            result_fields['Milliseconds'].value = f"{millisecond:,.0f}"
            result_fields['Weeks'].value = f"{week:,.4f}"
            
            input_field.error = None

        except ValueError:
            input_field.error = 'Please enter a valid number'
            for key in result_fields:
                result_fields[key].value = '0'
        finally:
            page.update()

    def reset(e):
        input_field.value = ''
        input_field.error = None
        for key in result_fields:
            result_fields[key].value = '0'
        page.update()

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Time Converter", size=25, weight=ft.FontWeight.BOLD, color="blue"),
                    unit_selector,
                    input_field,
                    ft.Row(
                        [
                            ft.Button(content=ft.Text("Convert"), on_click=convert, icon=ft.Icons.CALCULATE),
                            ft.OutlinedButton("Reset", on_click=reset, icon=ft.Icons.REFRESH),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Divider(height=20, thickness=2),
                    ft.Column(
                        [
                            ft.Row(
                                [ft.Text(f"{key}:", width=120), result_fields[key]],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ) for key in result_fields
                        ],
                        spacing=10,
                        width=280
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            padding=20
        )
    )

if __name__ == "__main__":
    ft.run(main)