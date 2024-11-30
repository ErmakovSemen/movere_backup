import trimesh
import numpy as np
import os

def compute_iou(mesh1, mesh2):
    # Проверяем, что объекты действительно являются 3D-объектами
    if not isinstance(mesh1, trimesh.Trimesh) or not isinstance(mesh2, trimesh.Trimesh):
        raise ValueError("Оба объекта должны быть экземплярами trimesh.Trimesh.")
    
    # Устанавливаем одинаковый размер вокселей для обоих объектов
    voxel_size = 0.3  # Размер вокселя (можно настроить для точности)

    # Преобразуем объекты в сетки вокселей
    mesh1_voxels = mesh1.voxelized(pitch=voxel_size)
    mesh2_voxels = mesh2.voxelized(pitch=voxel_size)
    
    # Приводим обе сетки к одинаковому размеру, используя рескейлинг
    # Паддинг или обрезка сеток до одного размера
    shape1 = mesh1_voxels.matrix.shape
    shape2 = mesh2_voxels.matrix.shape
    
    # Выбираем максимальные размеры для создания одинаковых сеток
    max_shape = np.maximum(shape1, shape2)

    # Изменяем размер вокселей в обеих сетках
    voxels1_rescaled = np.zeros(max_shape, dtype=bool)
    voxels2_rescaled = np.zeros(max_shape, dtype=bool)
    
    # Применяем рескейлинг
    voxels1_rescaled[:shape1[0], :shape1[1], :shape1[2]] = mesh1_voxels.matrix
    voxels2_rescaled[:shape2[0], :shape2[1], :shape2[2]] = mesh2_voxels.matrix
    
    # Пересечение и объединение
    intersection = np.logical_and(voxels1_rescaled, voxels2_rescaled)
    union = np.logical_or(voxels1_rescaled, voxels2_rescaled)
    
    # Вычисление метрики IOU
    iou = np.sum(intersection) / np.sum(union)
    
    return iou

# Убедитесь, что файлы STL существуют
file1 = 'object1.stl'
file2 = 'object2.stl'

if not os.path.exists(file1) or not os.path.exists(file2):
    raise FileNotFoundError("Один или оба STL файла не найдены. Убедитесь, что файлы существуют по указанному пути.")

# Загрузка объектов STL
mesh1 = trimesh.load_mesh(file1)
mesh2 = trimesh.load_mesh(file2)

# Вычисление IOU
iou_value = compute_iou(mesh1, mesh2)
print(f"IOU между объектами: {iou_value:.4f}")
