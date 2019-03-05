#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as plt



def main():
    # 1: 並行, 2: クロス, 3: 両方(布)

    for mode in [1, 2, 3]:

        if mode == 1:
            tendon_start = [[10., 200.], [10., 200.], [-10., 200.], [-10., 200.]]
            tendon_end = [[10., 0.], [10., 0.], [-10., 0.], [-10., 0.]]
        elif mode == 2:
            tendon_start = [[10., 200.], [10., 200.], [-10., 200.], [-10., 200.]]
            tendon_end = [[-10., 0.], [-10., 0.], [10., 0.], [10., 0.]]
        elif mode == 3:
            tendon_start = [[10., 200.], [10., 200.], [-10., 200.], [-10., 200.]]
            tendon_end = [[10., 0.], [-10., 0.], [10., 0.], [-10., 0.]]
        K = 0.8 # T=exp(k*dl)

        initial_length = []
        for i in range(len(tendon_start)):
            start = np.array(tendon_start[i])
            end = np.array(tendon_end[i])
            initial_length.append(np.linalg.norm(start-end))

        xs = [] # xの列
        xs_f = [] # xを動かした際にそれを妨げる力の列
        for x in range(1, 11):
            # x = x/2.
            Fs = 0
            for i in range(len(tendon_start)):
                start = np.array(tendon_start[i])
                end = np.array(tendon_end[i])+np.array([x, 0.])
                length = np.linalg.norm(start-end)
                # T = np.exp(K*max(0., length-initial_length[i])) # 張力
                T = np.exp(K*max(0., length-initial_length[i]-0.5)) # 張力
                F = T*(end[0]-start[0])/length
                Fs += F
            xs.append(float(x))
            xs_f.append(float(Fs))
        plt.subplot(1, 2, 1)
        plt.title("x")
        plt.plot(xs, xs_f)

        ys = [] # yの列
        ys_f = [] # yを動かした際にそれを妨げる力の列
        for y in range(200, 201):
            # y = y/2.
            Fs = 0
            for i in range(len(tendon_start)):
                start = np.array(tendon_start[i])
                end = np.array(tendon_end[i])+np.array([0, -y])
                length = np.linalg.norm(start-end)
                # T = np.exp(K*max(0., length-initial_length[i])) # 張力
                T = np.exp(K*max(0., length-initial_length[i]-0.5)) # 張力
                F = T*(start[1]-end[1])/length
                Fs += F
            ys.append(float(y))
            ys_f.append(float(Fs))
        plt.subplot(1, 2, 2)
        plt.title("y")
        plt.plot(ys, ys_f)

    plt.show()


if __name__ == '__main__':
    main()
