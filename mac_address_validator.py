import re
import tkinter as tk

def is_valid_mac(mac):
    pattern = r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$'
    return re.fullmatch(pattern, mac) is not None

def get_mac_type(mac):
    first_byte = mac.split(":")[0]
    binary = bin(int(first_byte, 16))[2:].zfill(8)
    return "Multicast" if binary[-1] == '1' else "Unicast"

def get_admin_type(mac):
    first_byte = mac.split(":")[0]
    binary = bin(int(first_byte, 16))[2:].zfill(8)
    return "Locally Administered" if binary[-2] == '1' else "Globally Administered"

class MACValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FA-Designer: A Simulator and Visualizer for Finite Automata")
        self.root.geometry("800x650")
        self.root.configure(bg="#1e1e1e")
        self.setup_ui()

    def setup_ui(self):
        # Header
        header = tk.Label(self.root, text="MAC Address Validator", font=("Poppins", 20, "bold"), bg="#1e1e1e", fg="white")
        header.pack(pady=20)

        # Input Frame
        input_frame = tk.Frame(self.root, bg="#1e1e1e")
        input_frame.pack(pady=10)

        label = tk.Label(input_frame, text="Enter MAC Address (XX:XX:XX:XX:XX:XX):", bg="#1e1e1e", fg="white", font=("Poppins", 12))
        label.pack(pady=5)

        self.entry = tk.Entry(input_frame, font=("Courier", 14), justify='center', width=30)
        self.entry.pack(pady=5)

        # Check Button
        check_button = tk.Button(self.root, text="Validate", command=self.check_mac, font=("Poppins", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5)
        check_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Poppins", 14), bg="#1e1e1e", fg="white")
        self.result_label.pack(pady=20)

        # Group Members
        group_member = tk.Label(self.root, text="GROUP MEMBERS:", justify="left", bg="#1e1e1e", fg="white", font=("Poppins", 12, "bold"))
        group_member.pack()

        members_list = tk.Label(self.root, text="MAGLINTE, Renie Boy\nMULAAN, Ric Ann\nCURSAT, Nica Mae\nESCABAS, Roy Lan\nGANOY, Rubilee", justify="left", bg="#1e1e1e", fg="white", font=("Poppins", 12))
        members_list.pack(pady=5)

    def check_mac(self):
        mac = self.entry.get()
        if is_valid_mac(mac):
            mac_type = get_mac_type(mac)
            admin_type = get_admin_type(mac)
            self.result_label.config(
                text=f"✅ Valid MAC Address\nType: {mac_type}\nAdmin: {admin_type}",
                fg="#4CAF50"
            )
        else:
            self.result_label.config(text="❌ Invalid MAC Address", fg="#F44336")

root = tk.Tk()
app = MACValidatorApp(root)
root.mainloop()
