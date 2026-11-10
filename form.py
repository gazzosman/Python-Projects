from pathlib import Path
import csv
import re
import tkinter
from tkinter import ttk
from tkinter import messagebox

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
window.configure(bg="blue")


window.title("Registration Form")
window.geometry("500x300")

submission_file = Path(__file__).with_name("form_submissions.csv")
#location of the file where the form submissions will be saved

userinfo_frame = tkinter.LabelFrame(frame, text="User Information")
userinfo_frame.grid(row=0, column=0)

tkinter.Label(userinfo_frame, text="Registration Form", font="ar 15 bold").grid(row=0, column=3, padx=10, pady=10)
firstname = tkinter.Label(userinfo_frame, text="First Name:")
lastname = tkinter.Label(userinfo_frame, text="Last Name:")
phone = tkinter.Label(userinfo_frame, text="Phone:")
email = tkinter.Label(userinfo_frame, text="Email:")
location = tkinter.Label(userinfo_frame, text="Location:")
agreement = tkinter.Label(userinfo_frame, text="I agree to the terms and conditions")
#here we created grid that holds the labels


firstname_entry = tkinter.Entry(userinfo_frame)
lastname_entry = tkinter.Entry(userinfo_frame)
phone_entry = tkinter.Entry(userinfo_frame)
email_entry = tkinter.Entry(userinfo_frame)
location_entry = tkinter.Entry(userinfo_frame)
agreement_check = tkinter.Checkbutton(userinfo_frame)
# entries are created for the user to input their information and a checkbox for agreement

firstname.grid(row=1, column=2)
firstname_entry.grid(row=1, column=3)
lastname.grid(row=2, column=2)
lastname_entry.grid(row=2, column=3)
phone.grid(row=3, column=2)
phone_entry.grid(row=3, column=3)
email.grid(row=4, column=2)
email_entry.grid(row=4, column=3)
location.grid(row=5, column=2)
location_entry.grid(row=5, column=3)
agreement.grid(row=6, column=3)
agreement_check.grid(row=6, column=2)
# displaying the labels and entries in the grid


def submit_form():
    firstname_value = firstname_entry.get().strip()
    lastname_value = lastname_entry.get().strip()
    phone_value = phone_entry.get().strip()
    email_value = email_entry.get().strip()
    location_value = location_entry.get().strip()
    agreement_value = "Yes" if agreement_check_var.get() else "No"

    empty_fields = [
        field_name
        for field_name, field_value in (
            ("First Name", firstname_value),
            ("Last Name", lastname_value),
            ("Phone", phone_value),
            ("Email", email_value),
            ("Location", location_value),
        )
        if not field_value
    ]
    if empty_fields:
        messagebox.showerror(
            "Missing information",
            f"Please fill in: {', '.join(empty_fields)}.",
        )
        return
    # error message is displayed for empty fields.

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email_value):
        messagebox.showerror(
            "Invalid email",
            "Please enter a valid email address.",
        )
        return
    # clause to check for valid email format using regular expressions.

    phone_pattern = r"\+?1?[\s.-]?(?:\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}"
    if not re.fullmatch(phone_pattern, phone_value):
        messagebox.showerror(
            "Invalid phone number",
            "Please enter a valid 10-digit phone number.",
        )
        return
    # clause to check for valid phone format using regular expressions.

    if not agreement_check_var.get():
        messagebox.showerror(
            "Agreement required",
            "You must agree to the terms and conditions before submitting.",
        )
        return
    # Clause to check if the user has filled in all the required fields, and if not, it shows an error message. It also checks if the email and phone number are valid formats, and if the user has agreed to the terms and conditions.

    entries = (
        "Registration Form Submitted\n\n"
        f"First Name: {firstname_value}\n"
        f"Last Name: {lastname_value}\n"
        f"Phone: {phone_value}\n"
        f"Email: {email_value}\n"
        f"Location: {location_value}\n"
        f"Agreed to terms: {agreement_value}"
    )

    try:
        file_exists = submission_file.exists()
        with submission_file.open("a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["First Name", "Last Name", "Phone", "Email", "Location", "Agreed to terms"])
            writer.writerow([
                firstname_value,
                lastname_value,
                phone_value,
                email_value,
                location_value,
                agreement_value,
            ])
    except (OSError, PermissionError, ValueError) as error:
        messagebox.showerror("Save failed", f"Could not save the form data:\n{error}")
        return
    # alert pop up is displayed if the form data could not be saved to the CSV file due to an error.

    messagebox.showinfo("Submitted", f"{entries}\n\nSaved to:\n{submission_file}")
    #shows a message box with the submitted information when the submit button is clicked

agreement_check_var = tkinter.BooleanVar(value=False)
agreement_check.config(variable=agreement_check_var)
# BooleanVar is created to hold the state of the agreement checkbox, and it is linked to the checkbox widget.

button = tkinter.Button(userinfo_frame, text="Submit", command=submit_form)
button.grid(row=7, column=3, padx=10, pady=10)
#submit button is created and linked to the submit_form function
    
window.mainloop()