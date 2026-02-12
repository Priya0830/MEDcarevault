#heading font-ockwell extra bold
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import filedialog
import shutil
import cv2
import random
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt 
import datetime
    
current_user_position = None
current_user_empid = None
current_user_name = None

# Function for the login screen
def logscreen():
    login = tk.Tk()
    login.title("Login - MedCareVault")
    login.geometry("600x400")
    login.config(bg="#A9CBF9")
    logo = Image.open("logo.png")   
    logo = logo.resize((50, 50))    
    logo_img = ImageTk.PhotoImage(logo)
    heading=tk.Label(login,text=" MedCareVault",font=("rockwell extra bold",40,"bold"),background="#62A4FA",anchor="center",foreground = "#0D47A1",bd=1.5, relief="raised",image=logo_img,compound="left")
    heading.pack(side='top',fill ='x')
    tk.Label(login, text="Username:", font=("Consolas", 14), bg="#A9CBF9").place(x=125, y=150)
    username_entry = tk.Entry(login, font=("Consolas", 14))
    username_entry.place(x=230, y=150)

    tk.Label(login, text="Password:", font=("Consolas", 14), bg="#A9CBF9").place(x=125, y=200)
    password_entry = tk.Entry(login, font=("Consolas", 14), show="*")
    password_entry.place(x=230, y=200)
    
    def validate_login():
        global current_user_position, current_user_empid, current_user_name
        import pandas as pd, os

        uname = username_entry.get().strip()
        pword = password_entry.get().strip()

        if not os.path.exists("userdata.csv"):
            tk.Label(login, text="No userdata.csv found!", fg="red", bg="#A9CBF9").place(x=50, y=200)
            return

        df = pd.read_csv("userdata.csv")

        row = df[(df["username"] == uname) & (df["password"] == pword)]

        if not row.empty:
            current_user_empid = int(row.iloc[0]["empid"])
            current_user_name = row.iloc[0]["username"]
            current_user_position = int(row.iloc[0]["position"])

            login.destroy()
            show_main_screen()
        else:
            tk.Label(login, text="Invalid credentials!", fg="red", bg="#A9CBF9").place(x=50, y=200)

    tk.Button(login, text="Login", font=("Consolas", 14, "bold"),
              bg="#0D47A1", fg="white", command=validate_login).place(x=250, y=260)

    login.mainloop()

# Function to display the main screen
def show_main_screen():
        global logo_img
        def show_default():
            for widget in body.winfo_children():
                widget.destroy()
            # Centered heading
            tk.Label(body, text="Welcome to MedCareVault!", font=("rockwell extra bold", 34, "bold"),
                    bg="#62A4FA", fg="#0D47A1").place(relx=0.5, y=30, anchor="center")
            tk.Label(body, text="Choose a video language:", font=("Consolas", 18),
                    bg="#62A4FA", fg="#0D47A1").place(relx=0.5, y=90, anchor="center")

            def open_video(lang):
                import subprocess, platform, os
                if lang == "malayalam":
                    vid_path = r"intromalayalam.mp4"  # Change path accordingly
                else:
                    vid_path = r"introhindi.mp4"
                if os.path.exists(vid_path):
                    if platform.system() == "Windows":
                        os.startfile(vid_path)
                    elif platform.system() == "Darwin":
                        subprocess.Popen(["open", vid_path])
                    else:
                        subprocess.Popen(["xdg-open", vid_path])
                else:
                    tk.messagebox.showerror("Error", f"File not found:\n{vid_path}")

            # Malayalam Video Button
            tk.Button(body, text="Malayalam Video", font=("Consolas", 18, "bold"),
                    bg="#0D47A1", fg="white", activebackground="#62A4FA",
                    command=lambda: open_video("malayalam")).place(relx=0.5, y=160, anchor="center", width=260, height=46)

            # Hindi Video Button
            tk.Button(body, text="Hindi Video", font=("Consolas", 18, "bold"),
                    bg="#0D47A1", fg="white", activebackground="#62A4FA",
                    command=lambda: open_video("hindi")).place(relx=0.5, y=220, anchor="center", width=260, height=46)

        def show_register():
            for widget in body.winfo_children():
                widget.destroy()

            tk.Label(body, text="Register New Patient", font=("Consolas",30,"bold"), bg="#62A4FA", fg="#0D47A1").place(x=5,y=10)

            # --- Form Inputs ---
            tk.Label(body, text="Name:", font=("Consolas",16,"bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=70)
            entry_name = tk.Entry(body, font=("Consolas",16))
            entry_name.place(x=200, y=70)

            tk.Label(body, text="Age:", font=("Consolas",16,"bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=110)
            entry_age = tk.Entry(body, font=("Consolas",16))
            entry_age.place(x=200, y=110)

            tk.Label(body, text="Gender:", font=("Consolas",16,"bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=150)
            gender_options = ["", "Male", "Female", "Other"]
            gender_var = tk.StringVar()
            gender_dropdown = ttk.Combobox(body, textvariable=gender_var, values=gender_options, state="readonly", font=("Consolas",16))
            gender_dropdown.place(x=200, y=150)
            gender_dropdown.current(0)

            tk.Label(body, text="Contact:", font=("Consolas",16,"bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=190)
            entry_contact = tk.Entry(body, font=("Consolas",16))
            entry_contact.place(x=200, y=190)

            tk.Label(body, text="Address:", font=("Consolas",16,"bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=230)
            address_text = tk.Text(body, font=("Consolas",12), width=25, height=4)
            address_text.place(x=200, y=230)

            tk.Label(body, text="Nationality:", font=("Consolas",16,"bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=320)
            entry_nationality = tk.Entry(body, font=("Consolas",16))
            entry_nationality.place(x=200, y=320)

            tk.Label(body, text="Medical Remarks:", font=("Consolas",16,"bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=360)
            remarks_text = tk.Text(body, font=("Consolas",12), width=40, height=5)
            remarks_text.place(x=200, y=400)

            # --- Migrant Photo Frame ---
            img_frame = tk.Frame(body, width=220, height=220, bg="white", bd=2, relief="sunken")
            img_frame.place(x=670, y=70)
            tk.Label(img_frame, text="Photo", bg="white", fg="#0D47A1", font=("Consolas", 14, "bold")).place(relx=0.5, rely=0.05, anchor="n")

            imgmig = tk.Label(img_frame, bg="white")
            imgmig.place(relx=0.5, rely=0.5, anchor="center", width=200, height=200)

            # --- ID Proof Upload Frame ---
            id_frame = tk.Frame(body, width=220, height=220, bg="white", bd=2, relief="sunken")
            id_frame.place(x=670, y=320)
            tk.Label(id_frame, text="ID Proof", bg="white", fg="#0D47A1", font=("Consolas", 14, "bold")).place(relx=0.5, rely=0.05, anchor="n")

            idproof = tk.Label(id_frame, bg="white")
            idproof.place(relx=0.5, rely=0.5, anchor="center", width=200, height=200)

            # Variables to store in-memory images (PIL Image objects)
            imgmig.current_img = None
            idproof.current_img = None

            def display_image_from_pil(pil_img, target_label):
                pil_img = pil_img.copy()
                pil_img.thumbnail((200, 200))
                img_tk = ImageTk.PhotoImage(pil_img)
                target_label.image = img_tk
                target_label.config(image=img_tk)

            def display_image_from_path(img_path, target_label):
                pil_img = Image.open(img_path)
                display_image_from_pil(pil_img, target_label)
                return pil_img

            def upload_image():
                file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
                if file_path:
                    pil_img = display_image_from_path(file_path, imgmig)
                    imgmig.current_img = pil_img

            def upload_id():
                file_path = filedialog.askopenfilename(title="Select ID Proof", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
                if file_path:
                    pil_img = display_image_from_path(file_path, idproof)
                    idproof.current_img = pil_img

            def capture_image():
                try:
                    import cv2
                    cam = cv2.VideoCapture(0)
                    cv2.namedWindow("Capture Image")

                    while True:
                        ret, frame = cam.read()
                        if not ret:
                            break
                        cv2.imshow("Capture Image", frame)
                        key = cv2.waitKey(1) & 0xFF
                        if key == 13:
                            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                            pil_img = Image.fromarray(rgb_frame)
                            display_image_from_pil(pil_img, imgmig)
                            imgmig.current_img = pil_img
                            break
                        elif key == 27:  # ESC to cancel
                            break

                    cam.release()
                    cv2.destroyAllWindows()
                except ImportError:
                    tk.messagebox.showerror("Error", "OpenCV not installed.")

            def generate_unique_migrant_id():
                import pandas as pd
                import random
                base = "MIG"
                filename = "migrant_data.csv"
                existing_ids = set()
                if os.path.exists(filename):
                    try:
                        df = pd.read_csv(filename)
                        existing_ids = set(df["Migrant ID"].astype(str).tolist())
                    except Exception:
                        pass

                while True:
                    random_number = "".join(str(random.randint(0,9)) for _ in range(5))
                    migrant_id = base + random_number
                    if migrant_id not in existing_ids:
                        return migrant_id

            def clear_all_fields():
                entry_name.delete(0, "end")
                entry_age.delete(0, "end")
                gender_dropdown.current(0)
                entry_contact.delete(0, "end")
                address_text.delete("1.0", "end")
                entry_nationality.delete(0, "end")
                remarks_text.delete("1.0", "end")
                imgmig.config(image="")
                imgmig.current_img = None
                idproof.config(image="")
                idproof.current_img = None

            def register_patient():
                

                name = entry_name.get().strip()
                age = entry_age.get().strip()
                gender = gender_var.get()
                contact = entry_contact.get().strip()
                address = address_text.get("1.0", "end").strip()
                nationality = entry_nationality.get().strip()
                remarks = remarks_text.get("1.0", "end").strip()

                # Validation: all fields and images required
                if not all([name, age, gender, contact, address, nationality, remarks]):
                    tk.messagebox.showwarning("Input Error", "Please fill in all fields.")
                    return
                if imgmig.current_img is None:
                    tk.messagebox.showwarning("Input Error", "Please upload or capture a photo.")
                    return
                if idproof.current_img is None:
                    tk.messagebox.showwarning("Input Error", "Please upload an ID proof image.")
                    return

                # Generate unique Migrant ID
                csv_file = "migrant_data.csv"
                existing_ids = set()
                if os.path.exists(csv_file):
                    try:
                        df = pd.read_csv(csv_file)
                        existing_ids = set(df["Migrant ID"].astype(str).str.strip())
                    except:
                        df = pd.DataFrame()
                else:
                    df = pd.DataFrame()

                while True:
                    migrant_id = generate_unique_migrant_id()
                    if migrant_id not in existing_ids:
                        break

                # Create folder
                migrant_folder = os.path.join(os.getcwd(), "migrant_details", migrant_id)
                os.makedirs(migrant_folder, exist_ok=True)

                # Save details text
                details_path = os.path.join(migrant_folder, f"{migrant_id}_details.txt")
                with open(details_path, "w", encoding="utf-8") as f:
                    f.write(f"Migrant ID: {migrant_id}\n")
                    f.write(f"Name: {name}\n")
                    f.write(f"Age: {age}\n")
                    f.write(f"Gender: {gender}\n")
                    f.write(f"Contact: {contact}\n")
                    f.write(f"Address: {address}\n")
                    f.write(f"Nationality: {nationality}\n")
                    f.write(f"Medical Remarks: {remarks}\n")

                # Save images
                imgmig.current_img.save(os.path.join(migrant_folder, "mig_photo.jpg"))
                idproof.current_img.save(os.path.join(migrant_folder, "mig_id.jpg"))

                # Prepare data dict
                data = {
                    "Migrant ID": migrant_id,
                    "Name": name,
                    "Age": age,
                    "Gender": gender,
                    "Contact": contact,
                    "Address": address,
                    "Nationality": nationality,
                    "Medical Remarks": remarks,
                    "Folder Path": migrant_folder.replace("\\", "/")
                }

                # Append new row
                new_row = pd.DataFrame([data])
                df = pd.concat([df, new_row], ignore_index=True)
                df.to_csv(csv_file, index=False)

                tk.messagebox.showinfo("Success", f"Patient Registered with ID: {migrant_id}")

                clear_all_fields()

            # --- Buttons ---
            tk.Button(body, text="Upload Photo", font=("Consolas", 14), command=upload_image).place(x=630, y=30)
            tk.Button(body, text="Capture Photo(enter)", font=("Consolas", 14), command=capture_image).place(x=770, y=30)
            tk.Button(body, text="Upload ID Proof", font=("Consolas", 14), command=upload_id).place(x=700, y=550)

            tk.Button(body, text="Register", font=("Consolas", 18, "bold"), bg="#0D47A1", fg="white", command=register_patient).place(x=120, y=560)

            tk.Button(body, text="Clear All", font=("Consolas", 14), bg="#FF5722", fg="white", command=clear_all_fields).place(x=250, y=565)

        def show_search():
            for widget in body.winfo_children():
                widget.destroy()

            import pandas as pd
            import os
            import shutil
            from PIL import Image, ImageTk
            from tkinter import ttk, filedialog

            def slide_in_message(text, bg_color):
                msg = tk.Label(body, text=text, font=("Consolas", 12), bg=bg_color, fg="white", padx=10, pady=5)
                body.update_idletasks()
                body_width = body.winfo_width()
                msg_width = 250
                y_pos = 60
                x_pos = body_width
                final_x = body_width - msg_width - 10

                def slide_in():
                    nonlocal x_pos
                    if x_pos > final_x:
                        x_pos -= 15
                        msg.place(x=x_pos, y=y_pos)
                        body.after(10, slide_in)
                    else:
                        msg.place(x=final_x, y=y_pos)
                        body.after(1000, slide_out)

                def slide_out():
                    nonlocal x_pos
                    if x_pos < body_width:
                        x_pos += 15
                        msg.place(x=x_pos, y=y_pos)
                        body.after(10, slide_out)
                    else:
                        msg.destroy()

                slide_in()

            # Heading
            tk.Label(body, text="Search and Update Migrant", font=("Consolas", 30, "bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=10)

            # Search Bar (Migrant ID)
            tk.Label(body, text="Enter Migrant ID:", font=("Consolas", 16, "bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=80)
            entry_search_id = tk.Entry(body, font=("Consolas", 16))
            entry_search_id.place(x=230, y=80, width=250)

            # Form fields for migrant data
            y_start = 130
            spacing = 40

            tk.Label(body, text="Name:", font=("Consolas", 16, "bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=y_start)
            entry_name = tk.Entry(body, font=("Consolas", 16))
            entry_name.place(x=230, y=y_start, width=300)

            tk.Label(body, text="Age:", font=("Consolas", 16, "bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=y_start+spacing)
            entry_age = tk.Entry(body, font=("Consolas", 16))
            entry_age.place(x=230, y=y_start+spacing, width=300)

            tk.Label(body, text="Gender:", font=("Consolas", 16, "bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=y_start+spacing*2)
            gender_options = ["Male", "Female", "Other"]
            gender_var = tk.StringVar()
            gender_dropdown = ttk.Combobox(body, textvariable=gender_var, values=gender_options, state="readonly", font=("Consolas", 16))
            gender_dropdown.place(x=230, y=y_start+spacing*2, width=300)

            tk.Label(body, text="Contact:", font=("Consolas", 16, "bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=y_start+spacing*3)
            entry_contact = tk.Entry(body, font=("Consolas", 16))
            entry_contact.place(x=230, y=y_start+spacing*3, width=300)

            tk.Label(body, text="Address:", font=("Consolas", 16, "bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=y_start+spacing*4)
            address_text = tk.Text(body, font=("Consolas", 12), width=30, height=4)
            address_text.place(x=230, y=y_start+spacing*4, width=300)

            tk.Label(body, text="Nationality:", font=("Consolas", 16, "bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=y_start+spacing*6 + 20)
            entry_nationality = tk.Entry(body, font=("Consolas", 16))
            entry_nationality.place(x=230, y=y_start+spacing*6 + 20, width=270)

            tk.Label(body, text="Medical Remarks:", font=("Consolas", 16, "bold"), bg="#62A4FA", fg="#0D47A1").place(x=5, y=y_start+spacing*7 + 20)
            remarks_text = tk.Text(body, font=("Consolas", 12), width=40, height=5)
            remarks_text.place(x=230, y=y_start+spacing*8 + 20, width=420, height=120)

            # Photo Frame
            img_frame = tk.Frame(body, width=220, height=220, bg="white", bd=2, relief="sunken")
            img_frame.place(x=680, y=80)
            tk.Label(img_frame, text="Photo", bg="white", fg="#0D47A1", font=("Consolas", 14, "bold")).place(relx=0.5, rely=0.05, anchor="n")

            img_label = tk.Label(img_frame, bg="white")
            img_label.place(relx=0.5, rely=0.5, anchor="center", width=200, height=200)
            img_label.current_img = None

            def display_image_from_path(img_path):
                try:
                    pil_img = Image.open(img_path)
                    pil_img.thumbnail((200, 200))
                    img_tk = ImageTk.PhotoImage(pil_img)
                    img_label.config(image=img_tk)
                    img_label.image = img_tk
                    img_label.current_img = pil_img
                except Exception:
                    img_label.config(image="")
                    img_label.image = None
                    img_label.current_img = None

            def search_migrant():
                migrant_id = entry_search_id.get().strip()
                if not migrant_id:
                    slide_in_message("Please enter a Migrant ID", "red")
                    return

                csv_file = "migrant_data.csv"
                if not os.path.exists(csv_file):
                    slide_in_message("No data available", "red")
                    return

                try:
                    df = pd.read_csv(csv_file)
                except Exception:
                    slide_in_message("Error reading data", "red")
                    return

                # Check column names to avoid KeyErrors
                expected_cols = ["Migrant ID", "Name", "Age", "Gender", "Contact", "Address", "Nationality", "Medical Remarks", "Folder Path"]
                for col in expected_cols:
                    if col not in df.columns:
                        slide_in_message(f"CSV missing column: {col}", "red")
                        return

                row = df[df["Migrant ID"] == migrant_id]
                if row.empty:
                    slide_in_message(f"No data found for ID {migrant_id}", "red")
                    return

                row = row.iloc[0]

                # Fill input fields
                entry_name.delete(0, "end")
                entry_name.insert(0, row["Name"])

                entry_age.delete(0, "end")
                entry_age.insert(0, row["Age"])

                gender_dropdown.set(row["Gender"])

                entry_contact.delete(0, "end")
                entry_contact.insert(0, row["Contact"])

                address_text.delete("1.0", "end")
                address_text.insert("1.0", row["Address"])

                entry_nationality.delete(0, "end")
                entry_nationality.insert(0, row["Nationality"])

                remarks_text.delete("1.0", "end")
                remarks_text.insert("1.0", row["Medical Remarks"])

                # Load photo from folder
                folder_path = row.get("Folder Path", "")
                if folder_path and os.path.exists(folder_path):
                    photo_path = os.path.join(folder_path, "mig_photo.jpg")
                    if os.path.exists(photo_path):
                        display_image_from_path(photo_path)
                    else:
                        img_label.config(image="")
                        img_label.image = None
                        img_label.current_img = None
                else:
                    img_label.config(image="")
                    img_label.image = None
                    img_label.current_img = None

                slide_in_message(f"Data loaded for {migrant_id}", "green")

            import datetime

            def update_migrant():
                migrant_id = entry_search_id.get().strip()
                if not migrant_id:
                    slide_in_message("Please enter a Migrant ID", "red")
                    return

                csv_file = "migrant_data.csv"
                if not os.path.exists(csv_file):
                    slide_in_message("No data file found", "red")
                    return

                try:
                    df = pd.read_csv(csv_file)
                except Exception:
                    slide_in_message("Error reading data", "red")
                    return

                if migrant_id not in df["Migrant ID"].values:
                    slide_in_message(f"No record found for ID {migrant_id}", "red")
                    return

                # Collect updated data
                name = entry_name.get().strip()
                age = entry_age.get().strip()
                gender = gender_var.get()
                contact = entry_contact.get().strip()
                address = address_text.get("1.0", "end").strip()
                nationality = entry_nationality.get().strip()
                remarks = remarks_text.get("1.0", "end").strip()

                if not all([name, age, gender, contact, address, nationality, remarks]):
                    slide_in_message("Please fill all fields before updating", "red")
                    return

                idx = df.index[df["Migrant ID"] == migrant_id][0]
                df.at[idx, "Name"] = name
                df.at[idx, "Age"] = age
                df.at[idx, "Gender"] = gender
                df.at[idx, "Contact"] = contact
                df.at[idx, "Address"] = address
                df.at[idx, "Nationality"] = nationality
                df.at[idx, "Medical Remarks"] = remarks

                try:
                    df.to_csv(csv_file, index=False)
                except Exception:
                    slide_in_message("Failed to update CSV", "red")
                    return

                folder_path = df.at[idx, "Folder Path"]
                if not os.path.exists(folder_path):
                    slide_in_message("Folder path missing, cannot update files", "red")
                    return

                try:
                    details_path = os.path.join(folder_path, f"{migrant_id}_details.txt")

                    # --- Preserve previous updates ---
                    previous_updates = []
                    if os.path.exists(details_path):
                        with open(details_path, "r", encoding="utf-8") as f:
                            lines = f.readlines()
                        for line in lines:
                            if line.startswith("Updated by:"):
                                # Extract existing history (split into user - time pairs)
                                updates_str = line.replace("Updated by:", "").strip()
                                if updates_str:
                                    previous_updates = [u.strip() for u in updates_str.split(",")]

                    # --- Update current user only with fresh timestamp ---
                    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    new_entry = f"{current_user_name} - {timestamp}"

                    # Remove any older record of the same user
                    previous_updates = [u for u in previous_updates if not u.startswith(current_user_name + " -")]

                    # Add this update
                    previous_updates.append(new_entry)

                    # --- Write file back ---
                    with open(details_path, "w", encoding="utf-8") as f:
                        f.write(f"Migrant ID: {migrant_id}\n")
                        f.write(f"Name: {name}\n")
                        f.write(f"Age: {age}\n")
                        f.write(f"Gender: {gender}\n")
                        f.write(f"Contact: {contact}\n")
                        f.write(f"Address: {address}\n")
                        f.write(f"Nationality: {nationality}\n")
                        f.write(f"Medical Remarks: {remarks}\n")
                        f.write(f"Updated by: {', '.join(previous_updates)}\n")

                    if img_label.current_img:
                        img_label.current_img.save(os.path.join(folder_path, "mig_photo.jpg"))

                    slide_in_message(f"Data updated for {migrant_id}", "green")

                except Exception as e:
                    slide_in_message(f"Failed to update details file: {e}", "red")

            def upload_file():
                    folder_path = ""  # initialize variable to avoid undefined warning
                    migrant_id = entry_search_id.get().strip()
                    if not migrant_id:
                        slide_in_message("Enter Migrant ID before uploading file", "red")
                        return

                    csv_file = "migrant_data.csv"
                    if not os.path.exists(csv_file):
                        slide_in_message("No data file found", "red")
                        return

                    try:
                        df = pd.read_csv(csv_file)
                    except Exception:
                        slide_in_message("Error reading data", "red")
                        return

                    row = df[df["Migrant ID"] == migrant_id]
                    if row.empty:
                        slide_in_message(f"No data found for ID {migrant_id}", "red")
                        return

                    folder_path = row.iloc[0].get("Folder Path", "")
                    if not folder_path or not os.path.exists(folder_path):
                        slide_in_message("Migrant folder not found", "red")
                        return

                    # Multiple file selection
                    file_paths = filedialog.askopenfilenames(title="Select Files")
                    if file_paths:
                        success_count = 0
                        for file_path in file_paths:
                            try:
                                filename = os.path.basename(file_path)
                                dest_path = os.path.join(folder_path, filename)
                                shutil.copy(file_path, dest_path)
                                success_count += 1
                            except Exception:
                                continue
                        if success_count > 0:
                            slide_in_message(f"{success_count} file(s) uploaded!", "green")
                        else:
                            slide_in_message("File upload failed!", "red")


            # Buttons with fixed visible placement
            tk.Button(body, text="Search", font=("Consolas", 14, "bold"), bg="#0D47A1", fg="white", command=search_migrant).place(x=540, y=78, width=100, height=35)

            tk.Button(body, text="Update", font=("Consolas", 18, "bold"), bg="#0D47A1", fg="white", command=update_migrant).place(x=450, y=600, width=200, height=50)

            tk.Button(body, text="Upload File", font=("Consolas", 18, "bold"), bg="#0D47A1", fg="white", command=upload_file).place(x=750, y=600, width=200, height=50)
        def show_dashboard():
            for widget in body.winfo_children():
                widget.destroy()

            import pandas as pd
            import os
            import matplotlib.pyplot as plt
            from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

            tk.Label(body, text="📊 Migrant Dashboard", font=("Consolas", 18, "bold"), 
                    bg="#62A4FA", fg="#0D47A1").place(x=10, y=10)

            csv_file = "migrant_data.csv"
            if not os.path.exists(csv_file):
                tk.Label(body, text="No data available yet.", font=("Consolas", 18), 
                        bg="#62A4FA", fg="red").place(x=10, y=80)
                return

            df = pd.read_csv(csv_file)
            if df.empty:
                tk.Label(body, text="No records found.", font=("Consolas", 18), 
                        bg="#62A4FA", fg="red").place(x=10, y=80)
                return

            # --- Prepare the figure with 2x2 subplots (only 3 used) ---
            fig, axs = plt.subplots(2, 2, figsize=(12, 8))
            fig.subplots_adjust(hspace=0.4, wspace=0.4)  # spacing between plots

            # --- Gender Distribution Pie Chart ---
            df["Gender"].value_counts().plot(
                kind="pie", ax=axs[0,0], autopct='%1.1f%%', startangle=90,
                colors=["#2196F3","#FF5722","#4CAF50"]
            )
            axs[0,0].set_title("Gender Distribution", fontsize=11, fontweight='bold')
            axs[0,0].set_ylabel("")  # remove y-label for pie chart

            # --- Age Distribution Bar Chart ---
            df["Age"].astype(str).value_counts().sort_index().plot(
                kind="bar", ax=axs[0,1], color="#FFC107"
            )
            axs[0,1].set_title("Age Distribution", fontsize=11, fontweight='bold')
            axs[0,1].set_xlabel("Age")
            axs[0,1].set_ylabel("Number of Patients")

            # --- Disease Frequency Analysis ---
            disease_counts = {}
            for remark in df["Medical Remarks"].astype(str):
                diseases = [d.strip().lower() for d in remark.split(",") if d.strip()]
                for disease in diseases:
                    disease_counts[disease] = disease_counts.get(disease, 0) + 1

            if disease_counts:
                sorted_diseases = dict(sorted(disease_counts.items()))
                axs[1,0].bar(sorted_diseases.keys(), sorted_diseases.values(), color="#9C27B0")
                axs[1,0].set_title("Patients by Disease (Medical Remarks)", fontsize=11, fontweight='bold')
                axs[1,0].set_xlabel("Disease")
                axs[1,0].set_ylabel("Number of Patients")
                axs[1,0].tick_params(axis='x', rotation=30)
            else:
                axs[1,0].text(0.5, 0.5, "No disease data available", ha='center', va='center', fontsize=12)
                axs[1,0].set_axis_off()

            # --- Remove 4th subplot and show count as text ---
            axs[1,1].set_axis_off()  # remove the axis
            total_patients = len(df)
            axs[1,1].text(0.5, 0.5, f"Total Migrants Registered:\n{total_patients}",
                        ha='center', va='center', fontsize=14, fontweight='bold', color="blue")

            # --- Embed figure in Tkinter ---
            canvas = FigureCanvasTkAgg(fig, master=body)
            canvas.draw()
            canvas.get_tk_widget().place(x=20, y=50, width=900, height=650)

        l=tk.Tk()
        l.title("MedCareVault")
        w= l.winfo_screenwidth()
        h = l.winfo_screenheight()
        l.geometry(f"{w}x{h}+0+0")#dimensions 1536 864
        l.config(bg="#A9CBF9")
        
        logo = Image.open("logo.png")   
        logo = logo.resize((50, 50))    
        logo_img = ImageTk.PhotoImage(logo)
        heading=tk.Label(l,text=" MedCareVault",font=("rockwell extra bold",40,"bold"),background="#62A4FA",anchor="center",foreground = "#0D47A1",bd=1.5, relief="raised",image=logo_img,compound="left")
        heading.pack(side='top',fill ='x')
        navbar=tk.Frame(l,width=int(w*0.25),height=int(h*0.81),background="#62A4FA",relief="groove",border=7.5)
        navbar.place(x=15, y=80)
        body=tk.Frame(l,width=int(w*0.72),height=int(h*0.81),background="#62A4FA",relief="groove",border=7.5)
        body.place(x=25+int(w*0.25),y=80)

        tk.Label(navbar,text="MENU",font=("Calisto MT",24,"bold"),background="#62A4FA",foreground="#0D47A1").place(x=10,y=10)
        def logout():
            l.quit()   # closes Tkinter mainloop
            l.destroy()  # destroys root window completely
            import sys
            sys.exit()    # ensures Python process ends


        # Register (all positions can register)
        if current_user_position in [1, 2, 3]:
            bregister = tk.Button(navbar, text="\u2794 Register", font=("Consolas",16,"bold"),
                background="#62A4FA", foreground="#0D47A1",
                activebackground="#0D47A1", activeforeground="white",
                width=28, height=1, anchor="w", command=show_register)
            bregister.place(x=10, y=60)

        # Search & Update (only position 1 and 2)
        if current_user_position in [1, 2]:
            bsearch = tk.Button(navbar, text="\u2794 Search/Update", font=("Consolas",16,"bold"),
                background="#62A4FA", foreground="#0D47A1",
                activebackground="#0D47A1", activeforeground="white",
                width=28, height=1, anchor="w", command=show_search)
            bsearch.place(x=10, y=120)

        # Dashboard (only position 1)
        if current_user_position == 1:
            bdashboard = tk.Button(navbar, text="\u2794 Dashboard", font=("Consolas",16,"bold"),
                background="#62A4FA", foreground="#0D47A1",
                activebackground="#0D47A1", activeforeground="white",
                width=28, height=1, anchor="w", command=show_dashboard)
            bdashboard.place(x=10, y=180)
        # 🔹 Logout button (always visible)
        blogout = tk.Button(navbar, text="\u2794 Logout", font=("Consolas",16,"bold"),
            background="#62A4FA", foreground="#0D47A1",
            activebackground="#0D47A1", activeforeground="white",
            width=28, height=1, anchor="w", command=logout)
        blogout.place(x=10, y=560)  # placed above Back button

        # Back (always visible)
        bback=tk.Button(navbar, text="\u2794 Back", font=("Consolas",16,"bold"),
            background="#62A4FA", foreground="#0D47A1",
            activebackground="#0D47A1", activeforeground="white",
            width=28, height=1, anchor="w", command=show_default)
        bback.place(x=10, y=620)



        show_default()
        l.mainloop()
logscreen()