from pathlib import Path
import csv
import tkinter
from tkinter import ttk
from tkinter import messagebox

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

window.title("Registration Form")
window.geometry("500x300")

submission_file = Path(__file__).with_name("form_submissions.csv")

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

    messagebox.showinfo("Submitted", f"{entries}\n\nSaved to:\n{submission_file}")

    #shows a message box with the submitted information when the submit button is clicked
agreement_check_var = tkinter.BooleanVar(value=False)
agreement_check.config(variable=agreement_check_var)
button = tkinter.Button(userinfo_frame, text="Submit", command=submit_form)
button.grid(row=7, column=3, padx=10, pady=10)
    
window.mainloop()