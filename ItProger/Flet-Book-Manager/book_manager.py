import flet as ft
import json
import os

def main(page: ft.Page):
    page.title = "Book reading manager"
    page.window.width = 450
    page.window.height = 800
    page.window.resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    DATA_FILE = "books_data.json"

    def save_data():
        items = []
        for ctrl in book_list.controls:
            if hasattr(ctrl, "data") and ctrl.data:
                items.append(ctrl.data)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=4)

    def load_data():
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data if isinstance(data, list) else []
            except (json.JSONDecodeError, Exception):
                return []
        return []

    book_title = ft.TextField(label="Book title", border_radius=10)
    book_author = ft.TextField(label="Author of the book", border_radius=10)
    book_list = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True, spacing=15)

    def delete_book(container):
        book_list.controls.remove(container)
        if len(book_list.controls) == 0:
            book_list.controls.append(empty_state)
        save_data()
        page.update()

    def create_book_card(title, author, progress=0):
        txt_title = ft.Text(f"{title}", size=16, weight="bold", expand=True)
        txt_author = ft.Text(f"by {author}", size=14, italic=True, color=ft.Colors.GREY_700)
        percent_label = ft.Text(f"{int(progress)}%", weight="bold", color=ft.Colors.BLUE_600)

        edit_title = ft.TextField(value=title, label="Edit title", visible=False, dense=True)
        edit_author = ft.TextField(value=author, label="Edit author", visible=False, dense=True)

        def on_slider_change(e):
            percent_label.value = f"{int(e.control.value)}%"
            container.data["progress"] = int(e.control.value)
            save_data()
            page.update()

        def toggle_edit(e):
            is_editing = edit_title.visible
            if is_editing:
                container.data["title"] = edit_title.value
                container.data["author"] = edit_author.value
                txt_title.value = edit_title.value
                txt_author.value = f"by {edit_author.value}"
                btn_edit.icon = ft.Icons.EDIT_OUTLINED
                btn_edit.tooltip = "Edit"
            else:
                btn_edit.icon = ft.Icons.CHECK_CIRCLE_OUTLINE
                btn_edit.tooltip = "Save changes"

            edit_title.visible = not is_editing
            edit_author.visible = not is_editing
            txt_title.visible = is_editing
            txt_author.visible = is_editing
            
            if is_editing: save_data()
            page.update()

        slider = ft.Slider(
            value=progress, min=0, max=100, divisions=20,
            on_change=on_slider_change, expand=True
        )

        btn_edit = ft.IconButton(
            icon=ft.Icons.EDIT_OUTLINED,
            icon_color=ft.Colors.BLUE_GREY_400,
            on_click=toggle_edit,
            tooltip="Edit"
        )

        container = ft.Container(
            padding=15,
            border_radius=12,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            content=ft.Column([
                ft.Row([
                    ft.Icon(ft.Icons.BOOK, color=ft.Colors.BLUE_400),
                    txt_title,
                    edit_title,
                    btn_edit,
                    ft.IconButton(
                        icon=ft.Icons.DELETE_OUTLINE,
                        icon_color=ft.Colors.RED_400,
                        on_click=lambda _: delete_book(container),
                        tooltip="Delete"
                    ),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                txt_author,
                edit_author,
                ft.Row([slider, percent_label], spacing=10)
            ], spacing=5)
        )
        container.data = {"title": title, "author": author, "progress": int(progress)}
        return container

    def add_book(e):
        if not book_title.value:
            book_title.error_text = "Please enter a title"
            page.update()
            return
        if not book_author.value:
            book_author.error_text = "Please enter an author"
            page.update()
            return

        book_title.error_text = None
        book_author.error_text = None

        if any(c == empty_state for c in book_list.controls):
            book_list.controls.clear()

        new_card = create_book_card(book_title.value, book_author.value)
        book_list.controls.insert(0, new_card)

        book_title.value = ""
        book_author.value = ""
        save_data()
        page.update()

    empty_state = ft.Container(
        content=ft.Column([
            ft.Icon(ft.Icons.LIBRARY_BOOKS, size=48, color=ft.Colors.GREY_400),
            ft.Text("No books yet", size=15, color=ft.Colors.GREY_500),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        alignment=ft.Alignment(0, 0),
        expand=True,
    )

    saved_books = load_data()
    if saved_books:
        for b in saved_books:

            if b and isinstance(b, dict):
                book_list.controls.append(
                    create_book_card(
                        b.get("title", "Unknown"), 
                        b.get("author", "Unknown"), 
                        b.get("progress", 0)
                    )
                )
    

    if not any(hasattr(c, "data") for c in book_list.controls):
        book_list.controls.clear() 
        book_list.controls.append(empty_state)

    main_content = ft.Column([
        ft.Row([
            ft.Icon(ft.Icons.LIBRARY_BOOKS, color="blue", size=30),
            ft.Text("Book reading manager", size=22, weight="bold", expand=True),
            ft.IconButton(
                icon=ft.Icons.BRIGHTNESS_6,
                on_click=lambda _: (
                    setattr(page, "theme_mode", 
                            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT),
                    page.update()
                )
            ),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

        book_title,
        book_author,
        ft.FilledButton(
            "Add the book",
            icon=ft.Icons.ADD,
            on_click=add_book,
            height=50
        ),

        ft.Divider(height=30),
        ft.Text("My library:", size=16, weight="bold", color=ft.Colors.BLUE_GREY_700),
        book_list
    ], expand=True, spacing=10, horizontal_alignment=ft.CrossAxisAlignment.STRETCH)

    page.add(main_content)

if __name__ == "__main__":
    ft.run(main)