class Solution:
    def displayTable(self, orders):
        """

        :type orders: list[list[str]]
        :return: list[list[str]]
        """
        dishes = set()
        tables = set()

        for order in orders:
            tables.add(order[1])
            dishes.add((order[2]))

        dishes = list(dishes)
        dishes.sort()

        table_dish = {}
        for table in tables:
            table_dish[table] = [0 for i in range(len(dishes))]

        for order in orders:
            table_dish[order[1]][dishes.index(order[2])] += 1

        table_dish = list(table_dish.items())
        table_dish.sort(key=lambda x:int(x[0]))

        display = []
        first_line = ["Table"]
        for dish in dishes:
            first_line.append(dish)
        display.append(first_line)

        for table, dish_count in table_dish:
            line = [table]
            for count in dish_count:
                line.append(str(count))
            display.append(line)

        return display

test = Solution()
order = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
print(test.displayTable(order))
