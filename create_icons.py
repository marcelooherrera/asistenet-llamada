from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, output_path):
    # Crear imagen con fondo verde
    img = Image.new('RGB', (size, size), color='#2D5016')
    draw = ImageDraw.Draw(img)
    
    # Dibujar círculo blanco en el centro
    margin = size // 8
    circle_bbox = [margin, margin, size - margin, size - margin]
    draw.ellipse(circle_bbox, fill='white')
    
    # Agregar emoji de teléfono en el centro
    font_size = int(size * 0.5)
    text = "📞"
    
    # Calcular posición centrada (aproximada para emoji)
    text_bbox = draw.textbbox((0, 0), text, font=None)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    position = ((size - text_width) // 2, (size - text_height) // 2 - size // 10)
    
    # Dibujar el texto
    draw.text(position, text, fill='#2D5016')
    
    img.save(output_path, 'PNG')
    print(f"Icono creado: {output_path}")

# Crear iconos
create_icon(192, 'icon-192.png')
create_icon(512, 'icon-512.png')
