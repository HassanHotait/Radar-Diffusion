import os

import numpy as np
import open3d as o3d
import pypatchworkpp

cur_dir = os.path.dirname(os.path.abspath(__file__))
input_cloud_filepath = os.path.join(cur_dir, "../../data/000000.bin")


def read_bin(bin_path):
    scan = np.fromfile(bin_path, dtype=np.float32)
    scan = scan.reshape((-1, 4))

    return scan


if __name__ == "__main__":
    # Patchwork++ initialization
    params = pypatchworkpp.Parameters()
    params.verbose = True

    PatchworkPLUSPLUS = pypatchworkpp.patchworkpp(params)

    # Load point cloud
    pointcloud = read_bin(input_cloud_filepath)

    # Estimate Ground
    PatchworkPLUSPLUS.estimateGround(pointcloud)

    # Get Ground and Nonground
    ground = PatchworkPLUSPLUS.getGround()
    nonground = PatchworkPLUSPLUS.getNonground()
    time_taken = PatchworkPLUSPLUS.getTimeTaken()

    ground_idx = PatchworkPLUSPLUS.getGroundIndices()
    nonground_idx = PatchworkPLUSPLUS.getNongroundIndices()

    # Get centers and normals for patches
    centers = PatchworkPLUSPLUS.getCenters()
    normals = PatchworkPLUSPLUS.getNormals()

    print("Origianl Points  #: ", pointcloud.shape[0])
    print("Ground Points    #: ", ground.shape[0])
    print("Nonground Points #: ", nonground.shape[0])
    print("Time Taken : ", time_taken / 1000000, "(sec)")
    print("Press ... \n")
    print("\t H  : help")
    print("\t N  : visualize the surface normals")
    print("\tESC : close the Open3D window")

    # Visualize
    vis = o3d.visualization.VisualizerWithKeyCallback()
    vis.create_window(width=600, height=400)

    mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()

    ground_o3d = o3d.geometry.PointCloud()
    ground_o3d.points = o3d.utility.Vector3dVector(ground)
    ground_o3d.colors = o3d.utility.Vector3dVector(
        np.array([[0.0, 1.0, 0.0] for _ in range(ground.shape[0])], dtype=float)  # RGB
    )

    nonground_o3d = o3d.geometry.PointCloud()
    nonground_o3d.points = o3d.utility.Vector3dVector(nonground)
    nonground_o3d.colors = o3d.utility.Vector3dVector(
        np.array(
            [[1.0, 0.0, 0.0] for _ in range(nonground.shape[0])], dtype=float
        )  # RGB
    )

    centers_o3d = o3d.geometry.PointCloud()
    centers_o3d.points = o3d.utility.Vector3dVector(centers)
    centers_o3d.normals = o3d.utility.Vector3dVector(normals)
    centers_o3d.colors = o3d.utility.Vector3dVector(
        np.array([[1.0, 1.0, 0.0] for _ in range(centers.shape[0])], dtype=float)  # RGB
    )

    vis.add_geometry(mesh)
    vis.add_geometry(ground_o3d)
    vis.add_geometry(nonground_o3d)
    vis.add_geometry(centers_o3d)

    vis.run()
    vis.destroy_window()
