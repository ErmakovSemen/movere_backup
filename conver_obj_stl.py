import trimesh


def convert_obj_to_stl(input_obj_file: str, output_stl_file: str) -> None:
    """
    Converts a 3D model from .obj format to .stl format.

    Parameters:
    input_obj_file (str): Path to the input .obj file.
    output_stl_file (str): Path to the output .stl file.

    Returns:
    None: Saves the .stl file at the specified location.
    """
    # Load the .obj file using trimesh
    mesh = trimesh.load(input_obj_file)

    # Export the mesh to an .stl file
    mesh.export(output_stl_file)

    print(f"Successfully converted {input_obj_file} to {output_stl_file}")


# Usage example

# path to .obj file to be converted to .stl format
input_obj_file = '/Users/sashats/Documents/Проект /1311/source/Модели/TripoSR/output/0/mesh.obj'
# path to save in
output_stl_file = '/Users/sashats/Documents/Проект /1311/source/Модели/TripoSR/output/0/output_file.stl'

convert_obj_to_stl(input_obj_file, output_stl_file)
