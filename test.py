import gi
from Solution import HashTag
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.add(Gtk.Label(label=data))


class ListBoxWindow(Gtk.Window):
    def __init__(self,tag='#javad'):
        super().__init__(title="Tweets Like")
        self.set_border_width(10)

        self.tag = tag

        box_outer = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.add(box_outer)

        scroll_widget = Gtk.ScrolledWindow()
        # scroll.set_size_request (400, 1);
        scroll_widget.set_policy(
            Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(scroll_widget, True, True, 0)

        #gScrolo
        # show posts


        posts = HashTag().show_bytag(self.tag)
        l = Gtk.Label(label="hashtag: " + self.tag + " occurnce: ")
        listbox.add(l)
        for post in posts :
            label = Gtk.Label(label=post)
            label.set_line_wrap(True)
            label.set_justify(Gtk.Justification.FILL)
            label.set_max_width_chars(32)
            listbox.add(label)

        scroll_widget.add(listbox)

        # right side box => trend hashtags
        listbox_2 = Gtk.ListBox()
        items = HashTag().topten_tags()

        for item in items:
            listbox_2.add(ListBoxRowWithData(item[0]))

        def sort_func(row_1, row_2, data, notify_destroy):
            return row_1.data.lower() > row_2.data.lower()

        def filter_func(row, data, notify_destroy):
            return False if row.data == "Fail" else True

        listbox_2.set_sort_func(sort_func, None, False)
        listbox_2.set_filter_func(filter_func, None, False)

        def on_row_activated(listbox_widget, row):
            self.__init__(str(row.data))
            print(row.data)

        listbox_2.connect("row-activated", on_row_activated)

        box_outer.pack_start(listbox_2, True, True, 0)
        listbox_2.show_all()


win = ListBoxWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
