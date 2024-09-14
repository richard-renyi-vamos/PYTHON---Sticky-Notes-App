import tkinter as tk
from tkinter import simpledialog

class StickyNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Sticker App")
        self.root.geometry("600x400")
        
        self.notes = []
        
        # Create a button to add a new note
        self.add_note_button = tk.Button(root, text="Add Note", command=self.create_note)
        self.add_note_button.pack()

    def create_note(self):
        # Create a new frame (note) that can be moved around
        note_frame = tk.Frame(self.root, bg='yellow', width=150, height=100, relief='raised', bd=2)
        note_frame.place(x=100, y=100)  # Default position
        self.notes.append(note_frame)
        
        # Create text widget for the note content
        text_widget = tk.Text(note_frame, wrap='word', height=5, width=18)
        text_widget.pack(expand=True, fill='both')
        text_widget.insert('1.0', 'New Note')

        # Bind mouse events for dragging
        note_frame.bind("<Button-1>", self.start_move)
        note_frame.bind("<B1-Motion>", self.do_move)

        # Create right-click menu for options like delete
        note_frame.bind("<Button-3>", lambda event, frame=note_frame: self.create_context_menu(event, frame))

    def start_move(self, event):
        self._drag_data = {"x": event.x, "y": event.y}

    def do_move(self, event):
        x = self.root.winfo_pointerx() - self.root.winfo_rootx() - self._drag_data["x"]
        y = self.root.winfo_pointery() - self.root.winfo_rooty() - self._drag_data["y"]
        event.widget.place(x=x, y=y)

    def create_context_menu(self, event, frame):
        context_menu = tk.Menu(self.root, tearoff=0)
        context_menu.add_command(label="Edit Note", command=lambda: self.edit_note_content(frame))
        context_menu.add_command(label="Delete Note", command=lambda: self.delete_note(frame))
        context_menu.post(event.x_root, event.y_root)

    def edit_note_content(self, note_frame):
        # Find the Text widget inside the note_frame
        text_widget = note_frame.winfo_children()[0]
        current_text = text_widget.get('1.0', 'end-1c')
        new_text = simpledialog.askstring("Edit Note", "Enter new content:", initialvalue=current_text)
        if new_text:
            text_widget.delete('1.0', 'end')
            text_widget.insert('1.0', new_text)

    def delete_note(self, note_frame):
        note_frame.destroy()
        self.notes.remove(note_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = StickyNoteApp(root)
    root.mainloop()
