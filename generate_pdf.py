import os
import urllib.request
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Definir datos de cada sección: título, contenido y URL de la imagen de ejemplo
sections = [
    {
        "title": "1. Descripción de la Tecnología",
        "content": ("Los recursos digitales para NEE son herramientas diseñadas para facilitar el aprendizaje y la comunicación en niños "
                    "con dificultades en el desarrollo. Ejemplos: PictogramAgenda, Proloquo2Go y Smile and Learn."),
        "image_url": "http://wwwhatsnew.com/wp-content/uploads/2012/12/ZAC.jpg",
        "image_filename": "desc_tecnologia.jpg",
        "bg_color": colors.lightpink
    },
    {
        "title": "2. Función y Finalidad",
        "content": ("Facilitar la comunicación de niños con dificultades en el habla, proporcionar materiales interactivos adaptados, "
                    "mejorar la inclusión en el aula y potenciar la independencia y el desarrollo social."),
        "image_url": "https://via.placeholder.com/400x300.png?text=Funci%C3%B3n+y+Finalidad",
        "image_filename": "funcion_finalidad.jpg",
        "bg_color": colors.lightblue
    },
    {
        "title": "3. Requerimientos para su Implementación",
        "content": ("Infraestructura tecnológica (tablets o computadoras con acceso a internet), software adaptativo, "
                    "formación del personal y colaboración con terapeutas y especialistas."),
        "image_url": "https://via.placeholder.com/400x300.png?text=Requerimientos",
        "image_filename": "requerimientos.jpg",
        "bg_color": colors.lightgreen
    },
    {
        "title": "4. Recursos Necesarios",
        "content": ("Para el centro educativo: dispositivos tecnológicos, formación y planes de enseñanza inclusivos. "
                    "Para las familias: dispositivos compatibles, participación en la formación y coordinación con el centro."),
        "image_url": "https://via.placeholder.com/400x300.png?text=Recursos+Necesarios",
        "image_filename": "recursos_necesarios.jpg",
        "bg_color": colors.lavender
    },
    {
        "title": "5. Ejemplo de Implementación",
        "content": ("En un centro de educación infantil se implementó PictogramAgenda para ayudar a niños con dificultades en la comunicación "
                    "verbal, facilitando la interacción y fomentando la autonomía."),
        "image_url": "https://via.placeholder.com/400x300.png?text=Ejemplo+de+Implementaci%C3%B3n",
        "image_filename": "ejemplo_implementacion.jpg",
        "bg_color": colors.mistyrose
    },
    {
        "title": "Conclusión",
        "content": ("El uso de recursos digitales para NEE mejora la comunicación y el aprendizaje en niños con dificultades, "
                    "requerido dispositivos adecuados, formación docente y colaboración especializada para una inclusión exitosa."),
        "image_url": "https://via.placeholder.com/400x300.png?text=Conclusi%C3%B3n",
        "image_filename": "conclusion.jpg",
        "bg_color": colors.lightyellow
    }
]

# Función para descargar imagen si no existe
def download_image(url, filename):
    if not os.path.exists(filename):
        try:
            urllib.request.urlretrieve(url, filename)
            print(f"Descargada imagen: {filename}")
        except Exception as e:
            print(f"Error al descargar {url}: {e}")

# Descargar todas las imágenes de ejemplo
for sec in sections:
    download_image(sec["image_url"], sec["image_filename"])

# Crear el documento PDF
doc = SimpleDocTemplate("Tarea_Digitalizacion_Educacion.pdf", pagesize=letter,
                        rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)

# Obtener estilos básicos y definir estilos personalizados
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'TitleStyle',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.darkblue,
    alignment=1,  # centrado
    spaceAfter=10,
    backColor=colors.whitesmoke  # color de fondo para la página de título
)
section_title_style = ParagraphStyle(
    'SectionTitleStyle',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=colors.white,
    alignment=0,
    leftIndent=6,
    spaceAfter=6
)
content_style = ParagraphStyle(
    'ContentStyle',
    parent=styles['BodyText'],
    fontSize=12,
    spaceAfter=12
)

story = []

# Título del documento
story.append(Paragraph("Digitalización Aplicada al Sector Educativo (0-3 Años)", title_style))
story.append(Spacer(1, 20))
story.append(Paragraph("Nombre: Ana Maria da Cunha Goncalves | Curso Académico: 2024/2025", styles['Normal']))
story.append(Spacer(1, 20))

# Agregar cada sección al documento
for sec in sections:
    # Crear un cuadro con el título de la sección (usando Table para dar fondo color pastel y formas redondeadas)
    title_data = [[Paragraph(sec["title"], section_title_style)]]
    title_table = Table(title_data, colWidths=[doc.width])
    title_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), sec["bg_color"]),
        ('BOX', (0, 0), (-1, -1), 1, colors.darkgray),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(title_table)
    story.append(Spacer(1, 10))
    # Agregar contenido de la sección
    story.append(Paragraph(sec["content"], content_style))
    story.append(Spacer(1, 10))
    # Agregar imagen
    try:
        img = Image(sec["image_filename"], width=400, height=300)
        img.hAlign = 'CENTER'
        story.append(img)
    except Exception as e:
        story.append(Paragraph("No se pudo cargar la imagen.", styles['Normal']))
    story.append(Spacer(1, 20))

# Final del documento
story.append(PageBreak())
story.append(Paragraph("Fin del documento", title_style))

# Generar el PDF
doc.build(story)
print("PDF generado: Tarea_Digitalizacion_Educacion.pdf")
