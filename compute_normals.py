import pymeshlab as pml
import argparse

pml.replace_pymeshlab_filter_names('/path/to/my/script.py')

parser = argparse.ArgumentParser(description='Do computing normals for point sets')
parser.add_argument('inp_mesh', type=str)
parser.add_argument('out_mesh', type=str)
parser.add_argument('-k', type=int, default=10)
parser.add_argument('-si', '--smoothiter', type=int, default=0)
parser.add_argument('-ff', '--flipflag', type=bool, default=False)
parser.add_argument('-vpx', '--viewpos_x', type=bool, default=0)
parser.add_argument('-vpy', '--viewpos_y', type=bool, default=0)
parser.add_argument('-vpz', '--viewpos_z', type=bool, default=0)

args = parser.parse_args()

ms = pml.MeshSet()
ms.load_new_mesh(args.inp_mesh)
ms.compute_normal_for_point_clouds(k=args.k, smoothiter=args.smoothiter, flipflag=args.flipflag,
                                   viewpos=[args.viewpos_x, args.viewpos_y, args.viewpos_z])
ms.save_current_mesh(args.out_mesh)
