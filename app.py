import gradio as gr
gr.close_all()

def greet(name):
  return "Hello," +name +"!"

demo=gr.Interface(
  fn=greet,
  input=[gr.Textbook(label="Namw:")],
  outputs=[gr.Textbook()],
)
demo.launch()
  
