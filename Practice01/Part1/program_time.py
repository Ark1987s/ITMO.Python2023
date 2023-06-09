from calculate_time import calculate

dist1 = float(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) => "))
dist2 = float(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы) => "))
offset = float(input("Боковое смещение между спасателем и утопающим, h (ярды) => "))
v_sand = float(input("Скорость движения спасателя по песку, Vsand (мили в час) => "))
ratio = float(input("Введите коэффициент замедления спасателя при движении в воде, n => "))
theta1 = float(input("Введите направление движения спасателя по песку, theta1 (градусы) => "))

time = calculate(dist1, dist2, offset, v_sand, ratio, theta1)
print("Если спасатель начнет движение под углом theta1, равным ", round(theta1), " градусам, он достигнет утопающего "
                                                                             "через ", round(time, 1), " секунды")