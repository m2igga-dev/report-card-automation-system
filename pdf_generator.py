from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
import os

def generate_pdf(name, df, output_dir):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report.html")

    html = template.render(
        name=name,
        subjects=df.to_dict(orient="records"),
        average=round(df["cumulative_average"].iloc[0], 2),
        position=df["position"].iloc[0]
    )

    filename = f"{name.replace(' ', '_')}.pdf"
    HTML(string=html).write_pdf(os.path.join(output_dir, filename))
