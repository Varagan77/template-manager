import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

NOTICE_TYPES = ["Notice!", "Final Notice!", "Handed!"]
DAYS_OPTIONS = [30, 60, 90]

class NoticeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Payment Notice Generator")
        self.geometry("620x700")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)

        # -------- CLIENT DETAILS --------
        ttk.Label(frame, text="Client Details", font=("Arial", 10, "bold"))\
            .grid(row=0, column=0, columnspan=2, pady=(0, 5), sticky="w")

        self.name = self.add_entry(frame, "Name", 1)
        self.surname = self.add_entry(frame, "Surname", 2)
        self.phone = self.add_entry(frame, "Phone / Cell", 3)
        self.last_paid = self.add_entry(frame, "Date Last Paid (DD/MM/YYYY)", 4)

        # -------- NOTICE OPTIONS --------
        ttk.Label(frame, text="Notice Options", font=("Arial", 10, "bold"))\
            .grid(row=5, column=0, columnspan=2, pady=(15, 5), sticky="w")

        ttk.Label(frame, text="Notice Type").grid(row=6, column=0, sticky="w")
        self.notice_type = ttk.Combobox(frame, values=NOTICE_TYPES, state="readonly")
        self.notice_type.current(0)
        self.notice_type.grid(row=6, column=1, sticky="ew")

        ttk.Label(frame, text="Days Outstanding").grid(row=7, column=0, sticky="w")
        self.days_outstanding = ttk.Combobox(frame, values=DAYS_OPTIONS, state="readonly")
        self.days_outstanding.current(0)
        self.days_outstanding.grid(row=7, column=1, sticky="ew")

        # -------- BUSINESS DETAILS --------
        ttk.Label(frame, text="Business Details (Footer)", font=("Arial", 10, "bold"))\
            .grid(row=8, column=0, columnspan=2, pady=(15, 5), sticky="w")

        self.business_name = self.add_entry(frame, "Business Name", 9)
        self.business_address = self.add_entry(frame, "Address / Location", 10)
        self.business_phone = self.add_entry(frame, "Business Phone", 11)
        self.business_email = self.add_entry(frame, "Business Email", 12)
        self.sign_off = self.add_entry(frame, "Sign-off Name", 13)

        # -------- ACTION --------
        ttk.Button(frame, text="Generate Notice", command=self.generate_notice)\
            .grid(row=14, column=0, columnspan=2, pady=15)

        # -------- OUTPUT --------
        self.output = tk.Text(frame, height=14, wrap="word")
        self.output.grid(row=15, column=0, columnspan=2, sticky="nsew")

        frame.columnconfigure(1, weight=1)

    def add_entry(self, parent, label, row):
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w", pady=4)
        entry = ttk.Entry(parent)
        entry.grid(row=row, column=1, sticky="ew")
        return entry

    def generate_notice(self):
        if not self.name.get() or not self.phone.get():
            messagebox.showerror("Missing Data", "Client name and phone number are required.")
            return

        today = date.today().strftime("%d/%m/%Y")

        footer = (
            f"{self.business_name.get()}\n"
            f"{self.business_address.get()}\n"
            f"Tel: {self.business_phone.get()}\n"
            f"Email: {self.business_email.get()}\n\n"
            f"Regards,\n{self.sign_off.get()}"
        )

        message = (
            f"{self.notice_type.get()}\n\n"
            f"Dear {self.name.get()} {self.surname.get()},\n\n"
            f"Our records indicate that an amount remains outstanding on your account. "
            f"The last recorded payment was on {self.last_paid.get()}.\n\n"
            f"This account is currently {self.days_outstanding.get()} days overdue. "
            f"Please arrange settlement or contact us should you require clarification.\n\n"
            f"Date: {today}\n\n"
            "--------------------------------------\n"
            f"{footer}"
        )

        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, message)


if __name__ == "__main__":
    app = NoticeApp()
    app.mainloop()
