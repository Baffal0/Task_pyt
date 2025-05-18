import os
import json
import math
import matplotlib.pyplot as plt

def f(x, A=0.0):
    numerator = math.sin(x**2 - A**2)**2 - 0.5
    denominator = abs(1 + 0.001 * (x**2 + A**2))
    return 0.5 + numerator / denominator

results_dir = "results"
os.makedirs(results_dir, exist_ok=True)

data = []
x_values = [x * 0.5 for x in range(-20, 21)]  # Из условия x от -10 до 10. Шаг - 0.5
for x in x_values:
    y = f(x, A=0)  # A=0 из условия
    data.append({"x": x, "y": y})

output_file = os.path.join(results_dir, "function_results_A0.json")
with open(output_file, "w", encoding="utf-8") as f_out:
    json.dump({"data": data}, f_out, indent=4)

print(f"Результаты сохранены в файл: {output_file}")

plt.figure(figsize=(10, 6))
plt.plot(x_values, [d["y"] for d in data], label="f(x) при A=0", color="red")
plt.title("График функции f(x) = 0.5 + sin²(x²) / (1 + 0.001x²)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

plot_file = os.path.join(results_dir, "function_plot_A0.png")
plt.savefig(plot_file)
print(f"График сохранён в файл: {plot_file}")

plt.show()
