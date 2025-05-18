import argparse
import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    x_elements = root.find("xdata").findall("x")
    y_elements = root.find("ydata").findall("y")

    x_values = [float(x.text) for x in x_elements]
    y_values = [float(y.text) for y in y_elements]

    return x_values, y_values


def main():
    parser = argparse.ArgumentParser(description="График функции из XML-файла")
    parser.add_argument("filename", type=str, help="Имя XML-файла (в папке 'results')")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--grid", action="store_true", help="Включить сетку на графике")
    group.add_argument("--no-grid", action="store_true", help="Отключить сетку на графике")

    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "results", args.filename)

    if not os.path.isfile(file_path):
        print(f"Файл не найден: {file_path}")
        return

    x, y = parse_xml(file_path)

    plt.plot(x, y, label="f(x)", color='blue')
    plt.title("График функции f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(args.grid)  # по умолчанию False

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
