import calendar
import tkinter as tk
from datetime import date
from tkinter import messagebox, ttk

US_STATES = (
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",
)


def main() -> None:
    root = tk.Tk()
    root.title("Date and State Form")
    root.resizable(False, False)

    content = ttk.Frame(root, padding=20)
    content.grid()

    ttk.Label(
        content,
        text="Select a date and state",
        font=("TkDefaultFont", 14, "bold"),
    ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 16))

    selected_date = tk.StringVar(value=date.today().isoformat())
    ttk.Label(content, text="Date").grid(
        row=1, column=0, sticky="w", padx=(0, 12), pady=6
    )
    date_row = ttk.Frame(content)
    date_row.grid(row=1, column=1, sticky="ew", pady=6)
    date_entry = ttk.Entry(
        date_row, textvariable=selected_date, state="readonly", width=18
    )
    date_entry.grid(row=0, column=0, padx=(0, 8))

    def open_date_picker() -> None:
        chosen = date.fromisoformat(selected_date.get())
        current_month = [chosen.replace(day=1)]
        picker = tk.Toplevel(root)
        picker.title("Choose a date")
        picker.resizable(False, False)
        picker.transient(root)

        calendar_frame = ttk.Frame(picker, padding=10)
        calendar_frame.grid()

        def change_month(offset: int) -> None:
            month_index = current_month[0].month - 1 + offset
            current_month[0] = date(
                current_month[0].year + month_index // 12,
                month_index % 12 + 1,
                1,
            )
            render_month()

        def select_day(day: int) -> None:
            selected_date.set(
                date(current_month[0].year, current_month[0].month, day).isoformat()
            )
            picker.destroy()

        def render_month() -> None:
            for widget in calendar_frame.winfo_children():
                widget.destroy()

            ttk.Button(
                calendar_frame, text="<", width=3, command=lambda: change_month(-1)
            ).grid(row=0, column=0)
            ttk.Label(
                calendar_frame,
                text=current_month[0].strftime("%B %Y"),
                anchor="center",
            ).grid(row=0, column=1, columnspan=5, sticky="ew")
            ttk.Button(
                calendar_frame, text=">", width=3, command=lambda: change_month(1)
            ).grid(row=0, column=6)

            for column, weekday in enumerate(calendar.day_abbr):
                ttk.Label(calendar_frame, text=weekday, anchor="center", width=4).grid(
                    row=1, column=column, pady=(8, 2)
                )

            for week_index, week in enumerate(
                calendar.monthcalendar(current_month[0].year, current_month[0].month),
                start=2,
            ):
                for column, day in enumerate(week):
                    if day:
                        ttk.Button(
                            calendar_frame,
                            text=str(day),
                            width=3,
                            command=lambda selected_day=day: select_day(selected_day),
                        ).grid(row=week_index, column=column, padx=1, pady=1)

        render_month()
        picker.grab_set()
        picker.wait_window()

    ttk.Button(date_row, text="Choose date", command=open_date_picker).grid(row=0, column=1)

    ttk.Label(content, text="State").grid(
        row=2, column=0, sticky="w", padx=(0, 12), pady=6
    )
    selected_state = tk.StringVar()
    state_picker = ttk.Combobox(
        content,
        textvariable=selected_state,
        values=US_STATES,
        state="readonly",
        width=25,
    )
    state_picker.grid(row=2, column=1, sticky="ew", pady=6)

    def submit_form() -> None:
        state = selected_state.get()
        if not state:
            messagebox.showerror(
                "Missing information", "Please select a state.", parent=root
            )
            return

        messagebox.showinfo(
            "Submitted",
            f"Date: {selected_date.get()}\nState: {state}",
            parent=root,
        )

    ttk.Button(content, text="Submit", command=submit_form).grid(
        row=3, column=1, sticky="e", pady=(16, 0)
    )

    root.mainloop()


if __name__ == "__main__":
    main()
