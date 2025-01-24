import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageGrab

class VectorGraphicsEditor:
    def __init__(self,root):
        self.root = root
        self.root.title("Vector Graphics Editor")
        self.root.geometry("800x600")
        
        self.shapes = []
        self.selected_shape = None
        self.offset_x = 0
        self.offset_y = 0

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

        # Rectangle Controls
        tk.Label(root, text="Rectangle").pack()
        self.rect_x = self.create_entry("X:", 50)
        self.rect_y = self.create_entry("Y:", 50)
        self.rect_width = self.create_entry("Width:", 100)
        self.rect_height = self.create_entry("Height:", 80)
        self.rect_color = self.create_entry("Color:", "blue")
        tk.Button(root, text="Draw Rectangle", command=self.draw_rectangle).pack()

        # Triangle Controls
        tk.Label(root, text="Triangle").pack()
        self.tri_x1 = self.create_entry("X1:", 100)
        self.tri_y1 = self.create_entry("Y1:", 200)
        self.tri_x2 = self.create_entry("X2:", 200)
        self.tri_y2 = self.create_entry("Y2:", 100)
        self.tri_x3 = self.create_entry("X3:", 300)
        self.tri_y3 = self.create_entry("Y3:", 200)
        self.tri_color = self.create_entry("Color:", "green")
        tk.Button(root, text="Draw Triangle", command=self.draw_triangle).pack()

        # Circle Controls
        tk.Label(root, text="Circle").pack()
        self.circ_x = self.create_entry("X Center:", 200)
        self.circ_y = self.create_entry("Y Center:", 200)
        self.circ_radius = self.create_entry("Radius:", 60)
        self.circ_color = self.create_entry("Color:", "red")
        tk.Button(root, text="Draw Circle", command=self.draw_circle).pack()
        
        # Button for Removing Shapes
        tk.Button(root,text="Remove Last Shape",command=self.remove_last_shape).pack(pady=5)
        # Save button
        tk.Button(root, text="Save Image", command=self.save_image).pack(pady=20)
        
        self.canvas.bind("<ButtonPress-1>",self.on_shape_click)
        self.canvas.bind("<B1-Motion>",self.on_shape_drag)
        self.canvas.bind("<ButtonRelease-1>",self.on_shape_release)

    def create_entry(self, label, default_value):
        frame = tk.Frame(self.root)
        tk.Label(frame, text=label).pack(side=tk.LEFT)
        entry = tk.Entry(frame)
        entry.insert(0, str(default_value))
        entry.pack(side=tk.LEFT)
        frame.pack()
        return entry

    def draw_rectangle(self):
        try:
            x = int(self.rect_x.get())
            y = int(self.rect_y.get())
            width = int(self.rect_width.get())
            height = int(self.rect_height.get())
            color = self.rect_color.get()

            rect =  self.canvas.create_rectangle(x, y, x + width, y + height, fill=color)
            self.shapes.append(rect)

        except ValueError:
            messagebox.showerror("Error", "Invalid input for rectangle. Please use numbers")

    def draw_triangle(self):
        try:
            x1 = int(self.tri_x1.get())
            y1 = int(self.tri_y1.get())
            x2 = int(self.tri_x2.get())
            y2 = int(self.tri_y2.get())
            x3 = int(self.tri_x3.get())
            y3 = int(self.tri_y3.get())
            color = self.tri_color.get()

            tri =  self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color)
            self.shapes.append(tri)
        
        except ValueError:
            messagebox.showerror("Error", "Invalid input for triangle. Please use numbers")
    
    def draw_circle(self):
        try:
            x = int(self.circ_x.get())
            y = int(self.circ_y.get())
            radius = int(self.circ_radius.get())
            color = self.circ_color.get()
           
            circ =  self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)
            self.shapes.append(circ)
        
        except ValueError:
            messagebox.showerror("Error", "Invalid input for circle. Please use numbers")
            
    def on_shape_click(self,event): 
        item = self.canvas.find_closest(event.x,event. y)
        if item:
            self.selected_shape = item
            coords = self.canvas.coords(item)
            if len(coords) ==4: #Rectangle or oval
                self.offset_x = event.x - coords[0]
                self.offset_y = event.y - coords[1]
            elif len(coords) == 6: #Triangle
                self.offset_x = event.x - coords[0]
                self.offset_y = event.y - coords[1]
                
    def on_shape_drag(self,event):
         if self.selected_shape:
             coords = self.canvas.coords(self.selected_shape)
             if len(coords) == 4: #Rectangle or oval
                 self.canvas.coords(self.selected_shape,event.x - self.offset_x,event.y - self.offset_y,
                                    event.x - self.offset_x+(coords[2] - coords[0]),
                                    event.y - self.offset_y+(coords[3] - coords[1]))
             elif len(coords) == 6: #Triangle
                     dx = event.x - self.offset_x
                     dy = event.y - self.offset_y
                     self.canvas.coords(self.selected_shape,dx,dy,
                                        dx+(coords[2] - coords[0]), dy + (coords[3] - coords[1]),
                                        dx+(coords[4] - coords[0]), dy + (coords[5] - coords[1]))
         
             
    def on_shape_release(self,event):
          self.selected_shape = None
    
    def remove_last_shape(self):
        if self.shapes:
            last_shape = self.shapes.pop()
            self.canvas.delete(last_shape)
        
    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                                  filetypes=[("PNG files", "*.png"), 
                                                             ("JPEG files", "*.jpg;*.jpeg"),
                                                             ("All files", "*.*")])
        if file_path:
            self.save_canvas_as_image(file_path)
            
    def save_canvas_as_image(self, file_path):
        # Get the canvas dimensions
        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Grab the canvas content
        image = ImageGrab.grab((x, y, x + width, y + height))
        image.save(file_path)

if __name__=='__main__':
    root = tk.Tk()
    app = VectorGraphicsEditor(root)
    root.mainloop()


