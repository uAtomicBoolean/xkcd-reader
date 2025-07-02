import webbrowser

import slint

import comic_funcs

components = slint.load_file("ui/app-window.slint")


class XkcdReader(components.AppWindow):
    # Removes an error with Ruff that doesn't detect the type.
    comic_id: int

    @slint.callback()
    def get_previous_comic(self):
        self.comic_id -= 1
        comic_data = comic_funcs.get_html_by_id(self.comic_id)
        if not comic_data:
            return

        self.comic_title = comic_data.title
        self.comic_image = slint.Image.load_from_path(comic_data.image_path)

    @slint.callback()
    def get_next_comic(self):
        self.comic_id += 1
        comic_data = comic_funcs.get_html_by_id(self.comic_id)
        if not comic_data:
            return

        self.comic_title = comic_data.title
        self.comic_image = slint.Image.load_from_path(comic_data.image_path)

    @slint.callback()
    def get_random_comic(self):
        comic_data = comic_funcs.get_html_by_random()
        if not comic_data:
            return

        self.comic_id = comic_data.id
        self.comic_title = comic_data.title
        self.comic_image = slint.Image.load_from_path(comic_data.image_path)

    @slint.callback()
    def open_comic(self):
        url = f"https://xkcd.com/{int(self.comic_id)}"
        webbrowser.open(url, new=0)


app = XkcdReader()
app.run()
