import flet as ft
import json
import os

DATA_FILE = "data.json"

def main(page: ft.Page):
    page.title = "Budget Tracker PRO"
    page.window.width = 400
    page.window.height = 650
    page.window.resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT

    def load_data():
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except: return []
        return []

    def save_data():
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(operations, f, ensure_ascii=False, indent=4)

    operations = load_data()

    operation_list = ft.ListView(expand=True, spacing=8, padding=ft.Padding.only(bottom=80))
    balance_text = ft.Text("Total Balance: $0.00", size=18, weight=ft.FontWeight.BOLD)

    description_field = ft.TextField(label="Description", autofocus=True)
    category_dropdown = ft.Dropdown(
        label="Category",
        options=[
            ft.dropdown.Option("Food"),
            ft.dropdown.Option("Transport"),
            ft.dropdown.Option("Salary"),
            ft.dropdown.Option("Entertainment"),
            ft.dropdown.Option("Other"),
        ],
        value="Other"
    )
    amount_field = ft.TextField(label="Amount (use - for expenses)", keyboard_type=ft.KeyboardType.NUMBER)
    amount_error = ft.Text("", color="red", size=12)

    def delete_operation(index):
        operations.pop(index)
        save_data()
        refresh_operations()


    empty_view = ft.Container(
        content=ft.Column([
            ft.Icon(ft.Icons.ACCOUNT_BALANCE_WALLET_OUTLINED, size=50, color=ft.Colors.GREY_300),
            ft.Text("No operations yet", color=ft.Colors.GREY_400, size=16),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        alignment=ft.Alignment(0, 0),
    )

    def refresh_operations():
        operation_list.controls.clear()
        total_balance = sum(op["amount"] for op in operations)
        balance_text.value = f"Total Balance: ${total_balance:.2f}"
        balance_text.color = "green" if total_balance >= 0 else "red"
        if not operations:
            operation_list.controls.append(empty_view)
        else:
            for i, op in enumerate(reversed(operations)):
                real_index = len(operations) - 1 - i
                color = "green" if op["amount"] >= 0 else "red"
                icon = ft.Icons.ARROW_UPWARD if op["amount"] >= 0 else ft.Icons.ARROW_DOWNWARD
                
                operation_list.controls.append(
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(icon, color=color, size=20),
                            ft.Column([
                                ft.Text(op["description"], size=14, weight="bold"),
                                ft.Text(op.get("category", "Other"), size=11, color=ft.Colors.GREY_500),
                            ], expand=1, spacing=1),
                            ft.Text(f"${op['amount']:.2f}", color=color, weight="bold", size=14),
                            ft.IconButton(
                                icon=ft.Icons.DELETE_OUTLINE,
                                icon_size=18,
                                icon_color=ft.Colors.GREY_400,
                                on_click=lambda e, idx=real_index: delete_operation(idx)
                            )
                        ]),
                        bgcolor=ft.Colors.with_opacity(0.05, color),
                        border_radius=8,
                        padding=ft.Padding.symmetric(horizontal=12, vertical=8),
                        border=ft.Border.all(1, ft.Colors.with_opacity(0.15, color)),
                    )
                )
        page.update()

    def save_operation(e=None):
        amount_error.value = ""
        if not description_field.value.strip() or not amount_field.value.strip():
            amount_error.value = "All fields are required."
            page.update()
            return

        try:
            val = float(amount_field.value.replace(",", "."))
            operations.append({
                "description": description_field.value.strip(),
                "amount": val,
                "category": category_dropdown.value
            })
            save_data()
            description_field.value = ""
            amount_field.value = ""
            dialog.open = False
            refresh_operations()
        except ValueError:
            amount_error.value = "Enter a valid number."
            page.update()

    amount_field.on_submit = save_operation

    dialog = ft.AlertDialog(
        title=ft.Text("Add Operation"),
        content=ft.Column([description_field, category_dropdown, amount_field, amount_error], tight=True, spacing=8),
        actions=[
            ft.TextButton("Save", on_click=save_operation),
            ft.TextButton("Cancel", on_click=lambda _: setattr(dialog, "open", False) or page.update())
        ]
    )
    page.overlay.append(dialog)

    def show_statistics(e):
        total_income = sum(op["amount"] for op in operations if op["amount"] > 0)
        total_expenses = sum(op["amount"] for op in operations if op["amount"] < 0)
        net = total_income + total_expenses
        
        stats_dialog = ft.AlertDialog(
            title=ft.Text("Statistics"),
            content=ft.Column([
                ft.Row([ft.Icon(ft.Icons.ARROW_UPWARD, color="green"), ft.Text("Income:"), ft.Text(f"${total_income:.2f}", color="green", weight="bold")], alignment="spaceBetween"),
                ft.Row([ft.Icon(ft.Icons.ARROW_DOWNWARD, color="red"), ft.Text("Expenses:"), ft.Text(f"${total_expenses:.2f}", color="red", weight="bold")], alignment="spaceBetween"),
                ft.Divider(),
                ft.Row([
                    ft.Icon(ft.Icons.ACCOUNT_BALANCE_WALLET, color="green" if net >= 0 else "red"),
                    ft.Text("Net Balance:", expand=1, weight="bold"),
                    ft.Text(f"${net:.2f}", weight="bold", color="green" if net >= 0 else "red")
                ]),
            ], tight=True, spacing=10),
            actions=[ft.TextButton("Close", on_click=lambda _: setattr(stats_dialog, "open", False) or page.update())]
        )
        page.overlay.append(stats_dialog)
        stats_dialog.open = True
        page.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=lambda _: setattr(dialog, "open", True) or page.update()
    )

    page.add(
        ft.Column([
            ft.Row([
                ft.Text("Budget Tracker", size=22, weight="bold"),
                ft.Row([
                    ft.IconButton(icon=ft.Icons.INSERT_CHART_OUTLINED, on_click=show_statistics),
                    ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=lambda _: setattr(page, "theme_mode", 
                        ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT) or page.update()),
                ], spacing=0)
            ], alignment="spaceBetween"),
            ft.Container(content=balance_text, bgcolor=ft.Colors.with_opacity(0.07, ft.Colors.BLUE), 
                         border_radius=10, padding=16),
            ft.Text("Recent Operations", size=14, color=ft.Colors.GREY_600),
            operation_list
        ], expand=True, spacing=12)
    )
    
    refresh_operations()

if __name__ == "__main__":
    ft.run(main)