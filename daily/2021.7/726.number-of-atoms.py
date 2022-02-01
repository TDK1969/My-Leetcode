class Solution:
    def count0fAtoms(self, formula: str) -> str:
        atoms_count = ""
        count = {}  # count字典记录原子：数量

        self.myfunc(formula, 0, count)
        # 将字典转换为元组列表，进行排序
        l = list(count.items())
        l.sort(key = lambda x: x[0])

        for atom, num in l:
            atoms_count += atom
            if num > 1:
                atoms_count += str(num)
        return atoms_count

    def myfunc(self, formula: str, index: int, count: dict) -> int:
        # 递归处理化学式
        formula_size = len(formula)
        # 当前处理字符为')'，则退出当前递归
        if index >= formula_size or formula[index] == ')':
            return index + 1
        # 循环处理
        while index < formula_size:
            if formula[index] == '(':
                # 当前处理字符为左括号，则递归处理括号内的化学式
                temp_count = {}  # temp_count字典记录括号内化学式的原子：数量
                index = self.myfunc(formula, index + 1, temp_count)

                # num记录括号后的数字，也就是括号内元素数量的倍数
                num = 0
                while index < formula_size and '0' <= formula[index] <= '9':
                    num = num * 10 + int(formula[index])
                    index += 1

                if num > 0:
                    for atom in temp_count.keys():
                        temp_count[atom] *= num
                # 如果num为0，则默认倍数为1，不改变

                # 将temp_count的记录加入count中
                for atom, atom_count in temp_count.items():
                    if atom not in count.keys():
                        count[atom] = 0
                    count[atom] += atom_count
            elif formula[index] == ')':
                return index + 1
            else:
                # 处理普通原子
                # 读取原子名称
                atom_name = formula[index]
                index += 1

                while index < formula_size and 'a' <= formula[index] <= 'z':
                    atom_name += formula[index]
                    index += 1
                # 读取原子数量
                num = 0
                while index < formula_size and '0' <= formula[index] <= '9':
                    num = num * 10 + int(formula[index])
                    index += 1

                if num == 0:
                    num = 1

                if num > 0:
                    if atom_name not in count.keys():
                        count[atom_name] = 0
                    count[atom_name] += num

