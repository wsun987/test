#!/usr/bin/env python3
"""
Simple Desktop Application Example
A basic desktop app using Tkinter (Python's built-in GUI library)
"""

import tkinter as tk
from tkinter import messagebox, ttk


class DesktopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Desktop App")
        self.root.geometry("500x400")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title label
        title_label = ttk.Label(
            main_frame, 
            text="Welcome to My Desktop App!", 
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Name input
        name_label = ttk.Label(main_frame, text="Enter your name:")
        name_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.name_entry = ttk.Entry(main_frame, width=30)
        self.name_entry.grid(row=1, column=1, pady=5)
        
        # Greeting button
        greet_button = ttk.Button(
            main_frame, 
            text="Greet Me!", 
            command=self.show_greeting
        )
        greet_button.grid(row=2, column=0, columnspan=2, pady=20)
        
        # Text area for output
        output_label = ttk.Label(main_frame, text="Output:")
        output_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        
        self.output_text = tk.Text(main_frame, height=8, width=50)
        self.output_text.grid(row=4, column=0, columnspan=2, pady=5)
        
        # Clear button
        clear_button = ttk.Button(
            main_frame, 
            text="Clear Output", 
            command=self.clear_output
        )
        clear_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
    
    def show_greeting(self):
        """Display a greeting message"""
        name = self.name_entry.get()
        if name:
            greeting = f"Hello, {name}! Welcome to this desktop application.\n"
            self.output_text.insert(tk.END, greeting)
            messagebox.showinfo("Greeting", f"Hello, {name}!")
        else:
            messagebox.showwarning("Warning", "Please enter your name first!")
    
    def clear_output(self):
        """Clear the output text area"""
        self.output_text.delete(1.0, tk.END)


def main():
    """Main entry point for the application"""
    root = tk.Tk()
    app = DesktopApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
