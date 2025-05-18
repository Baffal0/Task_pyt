import os
import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from xml.dom import minidom

A = 9.66459

x_values = np.linspace(-10, 10, 1000)  

y_values = -np.abs(np.sin(x_values) * np.cos(A) * np.exp(np.abs(1 - np.sqrt(x_values**2 + A**2) / np.pi)))

root = ET.Element("data")
xdata = ET.SubElement(root, "xdata")
ydata = ET.SubElement(root, "ydata")

for x, y in zip(x_values, y_values):
    ET.SubElement(xdata, "x").text = f"{x:.6f}"
    ET.SubElement(ydata, "y").text = f"{y:.6f}"

results_dir = "results"
os.makedirs(results_dir, exist_ok=True)

tree = ET.ElementTree(root)
output_path = os.path.join(results_dir, "function_results.xml")
xml_str = ET.tostring(root, encoding="utf-8")
parsed = minidom.parseString(xml_str)
pretty_xml_as_str = parsed.toprettyxml(indent="    ")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(pretty_xml_as_str)

plt.plot(x_values, y_values, label="f(x)", color='blue')
plt.title("График функции f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
