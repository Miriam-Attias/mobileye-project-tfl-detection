
import numpy as np
import matplotlib.pyplot as plt

from Model import SFM


class Output:
    
    @staticmethod
    def visualize(data, img_id):
        norm_prev_pts, norm_curr_pts, R, norm_foe, tZ = SFM.prepare_3D_data(data.prev, data.curr, data.focal, data.pp)
        norm_rot_pts = SFM.rotate(norm_prev_pts, R)
        rot_pts = SFM.unnormalize(norm_rot_pts, data.focal, data.pp)
        foe = np.squeeze(SFM.unnormalize(np.array([norm_foe]), data.focal, data.pp))

        fig, (curr_sec, prev_sec) = plt.subplots(1, 2, figsize=(12, 6))
        prev_sec.set_title('prev frame (' + str(img_id - 1) + ')')
        prev_sec.imshow(data.prev.img)
        prev_sec.plot(rot_pts[:, 0], rot_pts[:, 1], 'b+')

        curr_sec.set_title('curr frame (' + str(img_id) + ')')
        curr_sec.imshow(data.curr.img)

        for i in range(len(rot_pts)):
            curr_sec.plot([rot_pts[i, 0], foe[0]], [rot_pts[i, 1], foe[1]], 'b')

            if data.curr.valid[i]:
                curr_sec.text(rot_pts[i, 0], rot_pts[i, 1],
                              r'{0:.1f}'.format(data.curr.traffic_lights_3d_location[i, 2]), color='r')
        curr_sec.plot(foe[0], foe[1], 'r+')
        curr_sec.plot(rot_pts[:, 0], rot_pts[:, 1], 'g+')
        plt.show()
