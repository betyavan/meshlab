import pymeshlab as pml
import argparse

parser = argparse.ArgumentParser(description='Doing remesh model')
parser.add_argument('inp_mesh', type=str)
parser.add_argument('out_mesh', type=str)
parser.add_argument('targetfacenum', type=int)
parser.add_argument('-q', '--quadringulation', type=int, default=-1,
                    help="-1: None\n0: Fewest triangles\n1: (in between)\n 2: Better quad shape")
parser.add_argument('--qualitythr', type=float, default=1.)
parser.add_argument('--preserveboundary', type=bool, default=True)
parser.add_argument('--preservenormal', type=bool, default=True)
parser.add_argument('--planarquadric', type=bool, default=True)

args = parser.parse_args()

ms = pml.MeshSet()
ms.load_new_mesh(args.inp_mesh)
ms.meshing_decimation_quadric_edge_collapse(qualitythr=args.qualitythr, preserveboundary=args.preserveboundary,
                                            preservenormal=args.preservenormal, planarquadric=args.planarquadric)
if args.quadringulation != -1:
    ms.meshing_tri_to_quad_dominant(level=args.quadringulation)
ms.save_current_mesh(args.out_mesh)
