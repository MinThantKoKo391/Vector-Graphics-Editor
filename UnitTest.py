import unittest
import tkinter as tk
from VectorGraphicsEditor import VectorGraphicsEditor

class TestVectorGraphicsEditor(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = VectorGraphicsEditor(self.root)
        
    def tearDown(self):
        self.root.destroy()
        
    def test_draw_rectangle(self):
        # Simulate input for drawing a rectangle
        self.app.rect_x.delete(0,tk.END)
        self.app.rect_y.delete(0,tk.END)
        self.app.rect_width.delete(0,tk.END)
        self.app.rect_height.delete(0,tk.END)
        self.app.rect_color.delete(0,tk.END)
        self.app.rect_x.insert(0,'50')
        self.app.rect_y.insert(0,'50')
        self.app.rect_width.insert(0,'100')
        self.app.rect_height.insert(0,'80')
        self.app.rect_color.insert(0,'blue')
        self.app.draw_rectangle()
        
        self.assertEqual(len(self.app.shapes),1,"Rectangle not drawn correctly")
        
    def test_draw_triangle(self):
        # Simulate input for drawing a triangle
        self.app.tri_x1.delete(0,tk.END)
        self.app.tri_y1.delete(0,tk.END)
        self.app.tri_x2.delete(0,tk.END)
        self.app.tri_y2.delete(0,tk.END)
        self.app.tri_x3.delete(0,tk.END)
        self.app.tri_y3.delete(0,tk.END)
        self.app.tri_color.delete(0,tk.END)
        self.app.tri_x1.insert(0,'100')
        self.app.tri_y1.insert(0,'200')
        self.app.tri_x2.insert(0,'200')
        self.app.tri_y2.insert(0,'100')
        self.app.tri_x3.insert(0,'300')
        self.app.tri_y3.insert(0,'200')
        self.app.tri_color.insert(0,'green')
        self.app.draw_triangle()
        
        self.assertEqual(len(self.app.shapes),1,"Triangle not drawn correctly")
        
    def test_draw_circle(self):
        # Simulate input for drawing a circle
        self.app.circ_x.delete(0,tk.END)
        self.app.circ_y.delete(0,tk.END)
        self.app.circ_radius.delete(0,tk.END)
        self.app.circ_color.delete(0,tk.END)
        self.app.circ_x.insert(0,'200')
        self.app.circ_y.insert(0,'200')
        self.app.circ_radius.insert(0,'60')
        self.app.circ_color.insert(0,'red')
        self.app.draw_circle()
        
        self.assertEqual(len(self.app.shapes),1,"Circle not drawn correctly")
        
    def test_remove_last_shape(self):
        # Draw a rectangle and then remove it
        self.app.rect_x.delete(0,tk.END)
        self.app.rect_y.delete(0,tk.END)
        self.app.rect_width.delete(0,tk.END)
        self.app.rect_height.delete(0,tk.END)
        self.app.rect_color.delete(0,tk.END)
        self.app.rect_x.insert(0,'50')
        self.app.rect_y.insert(0,'50')
        self.app.rect_width.insert(0,'100')
        self.app.rect_height.insert(0,'80')
        self.app.rect_color.insert(0,'blue')
        self.app.draw_rectangle()
        
        self.assertEqual(len(self.app.shapes),1,"Shape not drawn correctly")
        # Remove the last shape
        self.app.remove_last_shape()
        self.assertEqual(len(self.app.shapes),0,"Shape not removed correctly")
        
    def test_move_shape(self):
         # Draw a rectangle
         self.app.rect_x.delete(0,tk.END)
         self.app.rect_y.delete(0,tk.END)
         self.app.rect_width.delete(0,tk.END)
         self.app.rect_height.delete(0,tk.END)
         self.app.rect_color.delete(0,tk.END)
         self.app.rect_x.insert(0,'50')
         self.app.rect_y.insert(0,'50')
         self.app.rect_width.insert(0,'100')
         self.app.rect_height.insert(0,'80')
         self.app.rect_color.insert(0,'blue')
         self.app.draw_rectangle()
         
         # Ensure the rectangle is drawn correctly
         item = self.app.shapes[0]
         initial_coords = self.app.canvas.coords(item)
         expected_initial_coords = [50,50,150,130]
         self.assertEqual(initial_coords,expected_initial_coords,"Initial coordinates do not match")
         
         # Simulate clicking and dragging the rectangle
         self.app.canvas.event_generate('<ButtonPress-1>',x=50,y=50)
         self.app.canvas.event_generate('<B1-Motion>',x=100,y=100)
         self.app.canvas.event_generate('<ButtonRelease-1>',x=100,y=100)
         
         # Check if the rectangle moved to the new position
         coords = self.app.canvas.coords(item)
         expected_coords = [50,50,150,130]
         self.assertEqual(coords,expected_coords,"Shape not moved correctly")
         
if __name__ == '__main__':
    unittest.main()         
         
    
    





