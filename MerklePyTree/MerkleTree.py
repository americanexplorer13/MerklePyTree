# -*- coding: utf-8 -*-
"""
:authors: AmericanExplorer13
:license: GNU general Public License v3.0, see LICENSE file
:copyright: (c) 2019 AmericanExplorer13
"""

import hashlib
from MerklePyTree.MerkleTree import *


class tree_init(object):

    def __init__(self, init_blocks=None, encrypt_mode="sha256"):
        self.init_blocks = init_blocks
        self.encrypt_mode = encrypt_mode

    def create_tree(self):

        nod_tree = []

        def init_nod(init_blocks):
            nod_lst = []

            for i in range(init_blocks):
                txt = input("Write message: ")
                txt = hashlib.sha256(txt.encode()).hexdigest()
                nod_lst.append(txt)

            return nod_lst

        def nod_create(nod_user):
            nod_lst = []

            for i in range(0, len(nod_user), 2):

                try:
                    nod_user[i + 1]
                except IndexError:
                    return nod_lst

                txt = hashlib.sha256((nod_user[i] + nod_user[i + 1]).encode()).hexdigest()
                nod_lst.append(txt)

            return nod_lst

        def check_list(nod_mod):
            if len(nod_mod) % 2 == 0:
                pass
            else:
                nod_mod.append(nod_mod[len(nod_mod) - 1])

            return nod_mod

        nod = init_nod(init_blocks=self.init_blocks)

        while len(nod) > 1:
            nod_tree.append(check_list(nod))
            nod = nod_create(check_list(nod))

        nod_tree.append(nod)
        return nod_tree

    @staticmethod
    def tree_depth(nod_tree):
        return str(len(nod_tree))

    @staticmethod
    def final_hash(nod_tree):
        return str(nod_tree[len(nod_tree) - 1])