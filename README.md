MerklePyTree
=================================================================================================================================================================================
**MerklePyTree** – Python модуль для построение дерева Меркля

```python

from MerklePyTree.MerkleTree import *

MTree = tree_init(init_blocks=NEEDED_BLOCKS, encrypt_mode="sha256")
MTree.create_tree()

```

Показать глубину дерева
------------
    tree_depth(MTree)

Показать последний (корневой) хэш дерева
------------
    final_hash(MTree)
