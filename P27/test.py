import unittest

import main


class Test(unittest.TestCase):
    def test_group3(self):
        groups = main.group3(['aldo', 'beat', 'carla', 'david', 'evi', 'flip', 'gary', 'hugo', 'ida'])
        self.assertEqual(len(groups), 1260)

    def test_group_size(self):
        # 9C9
        self.assertEqual(
            len(main.group([9], ['aldo', 'beat', 'carla', 'david', 'evi', 'flip', 'gary', 'hugo', 'ida'])),
            1)

        # 9C5 * 4C4
        self.assertEqual(
            len(main.group([5, 4], ['aldo', 'beat', 'carla', 'david', 'evi', 'flip', 'gary', 'hugo', 'ida'])),
            126)

        # 9C2 * 7C3 * 4C4
        self.assertEqual(
            len(main.group([2, 3, 4], ['aldo', 'beat', 'carla', 'david', 'evi', 'flip', 'gary', 'hugo', 'ida'])),
            1260)

    def test_group(self):
        groups = main.group([2, 3, 4], ['aldo', 'beat', 'carla', 'david', 'evi', 'flip', 'gary', 'hugo', 'ida'])

        self.assertEqual(len(groups), 1260)
        self.assertTrue([['aldo', 'beat'], ['carla', 'david', 'evi'], ['flip', 'gary', 'hugo', 'ida']] in groups)
        self.assertTrue([['hugo', 'ida'], ['evi', 'flip', 'gary'], ['aldo', 'beat', 'carla', 'david']] in groups)


if __name__ == "__main__":
    unittest.main()
